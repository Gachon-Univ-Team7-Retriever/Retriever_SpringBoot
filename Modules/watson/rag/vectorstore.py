import os
import typing

from langchain_community.document_loaders import MongodbLoader
from langchain_community.vectorstores import FAISS
from langchain_text_splitters import RecursiveCharacterTextSplitter

from server.db import get_mongo_connection_string, DB
from server.logger import logger
from utils import compare_dicts_sorted

if typing.TYPE_CHECKING:
    from watson.watson import Watson


class VectorStoreMethods:
    def update(self: 'Watson'):
        """
            데이터베이스에서 채팅 데이터가 변경되었는지 확인하고,
            현재 메모리에 로드된 채팅 데이터에서 변경된 사항이 있다면 메모리의 벡터스토어를 업데이트한다.
            또한, 메모리의 벡터스토어에 기반하는 그래프(LangGraph)도 다시 구축한다.
        """
        try:
            """
                다음의 경우에 RAG vectorstore를 재생성.
                1. 로컬에 저장된 벡터스토어가 없을 때
                2. MongoDB로 확인한 바, 현재 챗봇의 근거 데이터가 없을 때.
                3. MongoDB로 확인한 바, 현재 챗봇의 근거 데이터가 되는 채팅 ID 목록이 채널의 채팅 ID 목록과 서로 다를 때
            """
            # 로컬에 저장된 벡터스토어가 없음
            if not os.path.exists(self._vectorstore_path):
                logger.info(
                    f"There is no local vectorstore. Create vectorstore. (Local Path: {self._vectorstore_path})")
                self._build_vectorstore()  # MongoDB에서 채팅 데이터를 불러와서 vectorstore 재생성
            # 현재 챗봇의 근거 데이터가 되는 채팅이 없음
            elif not self.chats:
                logger.info(
                    f"There is no references for chatbot. Create vectorstore. (Local Path: {self._vectorstore_path})")
                self._build_vectorstore()
            # 현재 챗봇의 근거 데이터가 되는 채팅이, 실제 채널의 최신화된 채팅과 다름
            elif not compare_dicts_sorted(self.chats, newest_chats := self.load_chats(self.chats.keys())):
                self._update_chats(newest_chats)
                logger.info(
                    f"The reference chats for chatbot is different from chats of the channel. Rebuild Vectorstore. "
                    f"(Local Path: {self._vectorstore_path})")
                self._build_vectorstore()
            # 챗봇이 참조 중인 채팅이 현재 채널의 채팅과 일치함 -> 기존 벡터스토어와 그래프 로드
            else:
                logger.info(
                    f"The reference data of local vectorstore is same with channel data. Reuse local vectorstore. "
                    f"(Local Path: {self._vectorstore_path})")
                self._load_vectorstore() # 메모리에 벡터스토어가 없으면 로컬 파일에서 로드
                self._load_graph() # 메모리에 그래프가 없으면 재구축
        except Exception as e:
            logger.error(f"An error occurred while updating vectorstore: {e}")

    def _load_vectorstore(self: 'Watson'):
        """
            Notice for allow_dangerous_deserialization parameters of FAISS.load_local():

            The de-serialization relies on loading a pickle file.
            Pickle files can be modified to deliver a malicious payload
            that results in execution of arbitrary code on your machine.
            You will need to set `allow_dangerous_deserialization` to `True` to enable deserialization.
            If you do this, make sure that you trust the source of the data.
            For example, if you are loading a file that you created, and know that no one else has modified the file,
            then this is safe to do.
            Do not set this to `True` if you are loading a file from an untrusted source
            (e.g., some random site on the internet.).
        """
        try:
            # load_vectorstore가 호출되었다면 변경사항이 없다는 뜻이므로, 객체에 저장된 vectorstore가 있다면 재사용 가능
            # 만약 객체에 저장된 vectorstore가 없다면, load_local로 불러오기 시도.
            if not self._vectorstore:
                self._vectorstore = FAISS.load_local(self._vectorstore_path, self._embedding,
                                                     allow_dangerous_deserialization=True)

        except Exception as e:
            logger.error(f"An error occurred while loading vectorstore from local: {e}")
            return None

    def _save_vectorstore(self: 'Watson'):
        try:
            self._vectorstore.save_local(self._vectorstore_path)
        except Exception as e:
            logger.error(f"An error occurred while saving vectorstore to local: {e}")

    def _build_vectorstore(self: 'Watson'):
        """
            원격 데이터베이스의 채팅 데이터를 바탕으로 벡터스토어를 업데이트하고,
            업데이트된 벡터스토어를 바탕으로 그래프(LangGraph)를 재구축하는 메서드.
        """
        try:
            channel_ids = list(map(int, self.chats.keys()))  # chats의 key가 str 형으로 저장되어 있기 때문에, int로 변환한 뒤 검색
            # 단계 1: 문서 로드(Load Documents)
            logger.debug(f"Loading chat data from MongoDB. Channel IDs: {channel_ids}, scope: {self.scope}")
            loader = MongodbLoader(
                connection_string=get_mongo_connection_string(),
                db_name=DB.NAME,
                collection_name=DB.COLLECTION.CHANNEL.DATA,
                filter_criteria={} if self.scope == "global" else {
                    "channelId": {"$in": channel_ids}
                },  # 데이터베이스에서 조회할 기준 (쿼리)
                field_names=("text",),
                metadata_names=("id", "timestamp", "chats", "views", "url"),  # 메타데이터로 지정할 필드 목록
            )
            docs = loader.load()
            if not docs:
                self._vectorstore = None
                logger.warning(
                    f"There is no channel data found at DB for the bot. Channel IDs: {channel_ids}, scope: {self.scope}")
                return

            # 단계 2: 문서 분할(Split Documents)
            logger.debug(
                f"Splitting loaded chat documents from MongoDB. Channel IDs: {channel_ids}, scope: {self.scope}")
            text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=50)
            split_documents = text_splitter.split_documents(docs)

            # 단계 3: 임베딩(Embedding) 생성
            # 임베딩을 생성한다.
            # embedding = OpenAIEmbeddings()  # -> self._embedding 으로 저장한다음 바로 참조하기 때문에 생략됨

            # 단계 4: DB 생성(Create DB) 및 저장
            # 벡터스토어를 생성하고, 저장한다.
            logger.debug(f"Creating and Saving the vectorstore. Channel IDs: {channel_ids}, scope: {self.scope}")
            self._vectorstore = FAISS.from_documents(documents=split_documents, embedding=self._embedding)
            self._save_vectorstore()

            # chatbot collection에서 chatIds를 수집된 채팅의 ID로 업데이트
            logger.debug(f"Updating chatbot metadata. Channel IDs: {channel_ids}, scope: {self.scope}")
            self._update_db()
            
            # LangGraph 재구축
            self._graph = self.build_graph()
        except Exception as e:
            logger.error(f"An error occurred while building vectorstore: {e}")
