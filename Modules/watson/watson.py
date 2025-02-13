from datetime import datetime
import threading
import os
from dotenv import load_dotenv

load_dotenv()

from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_community.document_loaders import MongodbLoader

from server.db import DB, get_mongo_collection
from server.db import get_mongo_connection_string
from server.logger import logger
from .vectorstore import __file__


class Watson:
    prompt_template = PromptTemplate.from_template(
        """
        You are an assistant responding to inquiries from an investigator trying to investigate a drug-selling channel. 
        Below is chat data collected from a Telegram channel where drugs are being sold.
        Based on this chat data, answer questions about the transaction details of the channel.
        If you don't know the answer, just say that you don't know.
        Answer in Korean.

        #Question:
        {question}

        #Context:
        {context}

        #Answer:
        """
    )
    _instances = {}
    _lock = threading.Lock()
    error_msg_for_empty_data = "죄송합니다. 요청하신 채널의 데이터가 없거나, 아직 수집되지 않아 답변을 드릴 수 없습니다."

    def __new__(cls, channel_id):
        """
            싱글톤 객체의 변형 구현.
            입력받은 channel id에 대응하는 watson 챗봇이 없을 경우에 한해,
            고유한 watson 객체를 새로 만들고 반환하는 동시에 _instances에 내부적으로 저장한다.

            만약 해당 channel id에 대응하는 챗봇이 이미 생성되었을 경우,
            그 챗봇을 반환한다.
        """
        if not cls._instances.get(channel_id):
            with cls._lock:
                if not cls._instances.get(channel_id):
                    cls._instances[channel_id] = super(Watson, cls).__new__(cls)

        return cls._instances[channel_id]

    def __init__(self, channel_id):
        # 이미 객체가 초기화되어 있을 경우, 객체를 초기화하지 않고 벡터스토어만 업데이트한 후 종료.
        with self._lock:
            if hasattr(self, "channel_id"):
                self._update_vectorstore()
                return

            self._channel_id = channel_id
            self._embedding = OpenAIEmbeddings()  # 임베딩(Embedding) 생성
            self._llm = ChatOpenAI(model_name="gpt-4o", temperature=0)  # 언어모델(LLM) 생성

            self._vectorstore, self._chain = None, None
            self._vectorstore_path = os.path.join(os.path.dirname(__file__),
                                                  str(channel_id))  # watson/vectorstore/<channel id> 위치에 벡터스토어 저장.
            self._update_db()
            self._update_vectorstore()

    def _update_vectorstore(self):
        try:
            chat_collection = get_mongo_collection(DB.NAME, DB.COLLECTION.CHANNEL.DATA)
            chatbot_collection = get_mongo_collection(DB.NAME, DB.COLLECTION.CHATBOT)
            # 채널 ID를 기준으로 모든 채팅을 찾아서 각 채팅의 채팅 ID를 리스트로 생성
            chat_ids = [doc["id"] for doc in chat_collection.find({"channelId": self._channel_id})]
            bot_references = chatbot_collection.find_one({"channelId": self._channel_id}).get("chatIds")
            """
                다음의 경우에 RAG vectorstore를 재생성.
                1. 로컬에 저장된 벡터스토어가 없을 때
                2. MongoDB로 확인한 바, 현재 챗봇의 근거 데이터가 없을 때.
                3. MongoDB로 확인한 바, 현재 챗봇의 근거 데이터가 되는 채팅 ID 목록이 채널의 채팅 ID 목록과 서로 다를 때
            """
            if not os.path.exists(self._vectorstore_path):
                logger.info(f"There is no local vectorstore. Create vectorstore. (Local Path: {self._vectorstore_path})")
                self._build_vectorstore()  # MongoDB에서 채팅 데이터를 불러와서 vectorstore 재생성
            elif not bot_references:
                logger.info(f"There is no references for chatbot. Create vectorstore. (Local Path: {self._vectorstore_path})")
                self._build_vectorstore()
            elif sorted(chat_ids) != sorted(bot_references):
                logger.info(f"The reference chats for chatbot is different from chats of the channel. Rebuild Vectorstore. "
                            f"(Local Path: {self._vectorstore_path})")
                self._build_vectorstore()
            else:
                logger.info(f"The reference data of local vectorstore is same with channel data. Reuse local vectorstore. "
                            f"(Local Path: {self._vectorstore_path})")
                self._load_vectorstore()  # 챗봇이 참조 중인 채팅이 현재 채널의 채팅과 일치하고, 그 벡터스토어가 로컬에 저장되어 있을 때 불러옴.

            self._build_chain()
        except Exception as e:
            logger.error(f"An error occurred while updating vectorstore: {e}")

    def _update_db(self):
        try:
            # MongoDB client 생성 및 컬렉션 선택
            chatbot_collection = get_mongo_collection(DB.NAME, DB.COLLECTION.CHATBOT)
            if not chatbot_collection.find_one({"channelId": self._channel_id}):
                chatbot_collection.insert_one({
                    "channelId": self._channel_id,
                    "updatedAt": datetime.now(),
                    "chatIds": []
                })
        except Exception as e:
            logger.error(f"An error occurred while updating chatbot metadata at MongoDB: {e}")

    def _load_vectorstore(self):
        """
            Notice for allow_dangerous_deserializatio parameters of FAISS.load_local():

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
            if not self._vectorstore:
                self._vectorstore = FAISS.load_local(self._vectorstore_path, self._embedding, allow_dangerous_deserialization=True)
        except Exception as e:
            logger.error(f"An error occurred while loading vectorstore from local: {e}")

    def _save_vectorstore(self):
        try:
            self._vectorstore.save_local(self._vectorstore_path)
        except Exception as e:
            logger.error(f"An error occurred while saving vectorstore to local: {e}")

    def _build_vectorstore(self):
        try:
            # 단계 1: 문서 로드(Load Documents)
            logger.debug(f"Loading chat data from MongoDB. Channel ID: {self._channel_id}")
            loader = MongodbLoader(
                connection_string=get_mongo_connection_string(),
                db_name=DB.NAME,
                collection_name=DB.COLLECTION.CHANNEL.DATA,
                filter_criteria={"channelId": self._channel_id},  # 데이터베이스에서 조회할 기준 (쿼리)
                field_names=("text",),
                metadata_names=("id", "timestamp", "channelId", "views", "url"),  # 메타데이터로 지정할 필드 목록
            )
            docs = loader.load()
            ids = [doc.metadata['id'] for doc in docs]

            # 단계 2: 문서 분할(Split Documents)
            logger.debug(f"Splitting loaded chat documents from MongoDB. Channel ID: {self._channel_id}")
            text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=50)
            split_documents = text_splitter.split_documents(docs)

            # 단계 3: 임베딩(Embedding) 생성
            # 임베딩을 생성한다.
            # embedding = OpenAIEmbeddings()  # -> self._embedding 으로 저장한다음 바로 참조하기 때문에 생략됨

            # 단계 4: DB 생성(Create DB) 및 저장
            # 벡터스토어를 생성하고, 저장한다.
            logger.debug(f"Creating and Saving the vectorstore. Channel ID: {self._channel_id}")
            self._vectorstore = FAISS.from_documents(documents=split_documents, embedding=self._embedding)
            self._save_vectorstore()

            # chatbot collection에서 chatIds를 수집된 채팅의 ID로 업데이트
            logger.debug(f"Updating chatbot metadata. Channel ID: {self._channel_id}")
            chatbot_collection = get_mongo_collection(DB.NAME, DB.COLLECTION.CHATBOT)
            chatbot_collection.update_one({"channelId": self._channel_id},
                                          {"$set": {"chatIds": ids, "updatedAt": datetime.now()}})
        except Exception as e:
            logger.error(f"An error occurred while building vectorstore: {e}")

    def _build_chain(self):
        try:
            # 단계 5: 검색기(Retriever) 생성
            # 문서에 포함되어 있는 정보를 검색하고 생성한다.
            retriever = self._vectorstore.as_retriever()

            # 단계 6: 프롬프트 생성(Create Prompt)
            # 프롬프트를 생성한다.
            # prompt = self.prompt_template -> self.promopt_template로 바로 참조하기 때문에 생략됨.

            # 단계 7: 언어모델(LLM) 생성
            # 모델(LLM)을 생성한다.
            # llm = ChatOpenAI(model_name="gpt-4o", temperature=0) -> self._llm으로 바로 참조하기 때문에 생략됨.

            # 단계 8: 체인(Chain) 생성
            self._chain = (
                    {"context": retriever, "question": RunnablePassthrough()}  # 1. [prompt에 들어갈 값](딕셔너리 형태)
                    | self.prompt_template  # 2. context와 question이 들어갈 [프롬프트]
                    | self._llm  # 3. 프롬프트가 들어갈 [LLM]
                    | StrOutputParser()  # 4. LLM이 내놓은 결과를 정리해줄 [Parser]
            )  # 배경지식과 질문 -> 프롬프트 -> LLM -> 결과 전처리 Parser 의 4단계 chain이 생성됨.
        except Exception as e:
            logger.error(f"An error occurred while building langchain: {e}")

    # 체인 실행(Run Chain)
    # 문서에 대한 질의를 입력하고, 답변을 출력한다.
    def ask(self, question: str):
        # chain이 있으면 chain을 실행하고 답변을 반환. chain이 없으면 에러 메세지 반환.
        answer = self._chain.invoke(question) if self._chain else self.error_msg_for_empty_data
        logger.info(f"Chatbot answered to a question. Q: '{question}', A: '{answer}'")
        return answer
