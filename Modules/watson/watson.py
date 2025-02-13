from datetime import datetime
import threading
import typing
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

from utils import generate_integer_id64, compare_dicts_sorted
from server.db import DB, get_mongo_collection
from server.db import get_mongo_connection_string
from server.logger import logger
from .vectorstore import __file__


# 모든 챗봇의 메타데이터를 가져와서 초기화.
chatbot_collection = get_mongo_collection(DB.NAME, DB.COLLECTION.CHATBOT)
chat_collection = get_mongo_collection(DB.NAME, DB.COLLECTION.CHANNEL.DATA)

def load_chats(channel_ids:typing.Iterable[typing.Union[str, int]]):
    chats = {}
    for channel_id in channel_ids:
        # 채팅 데이터 collection에서, 참고하려는 채널에서 송수신된 모든 채팅의 채팅 id를 채널 id로 나누어서 저장.
        chats[channel_id] = [chat.get('id') for chat in chat_collection.find({"channelId": int(channel_id)})]
    return chats


# 클래스 정의가 완료되는 시점(클래스 선언 시점)에 미리 인스턴스를 생성하는 메타클래스.
class AutoCreateInstances(type):
    def __init__(cls, name, bases, dct):
        super().__init__(name, bases, dct)
        # _instances 변수를 초기화
        cls._instances = {}
        # 클래스가 생성되자마자 챗봇의 메타데이터를 다운로드, 챗봇 ID마다 인스턴스를 생성해서 등록
        for document in chatbot_collection.find():
            cls._instances[document.get('id')] = cls(bot_id=document.get('id'))

        logger.info(f"로드된 챗봇: {list(cls._instances.keys())}")
            
class Watson(metaclass=AutoCreateInstances):
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
    GLOBAL = "global"
    MULTI = "multi"
    LOCAL = "local"

    def __new__(cls, bot_id:int=None, channel_ids:list=None, scope:str=None):
        """
            싱글톤 객체의 변형 구현.
            입력받은 channel id에 대응하는 watson 챗봇이 없을 경우에 한해,
            고유한 watson 객체를 새로 만들고 반환하는 동시에 _instances에 내부적으로 저장한다.

            만약 해당 channel id에 대응하는 챗봇이 이미 생성되었을 경우,
            그 챗봇을 반환한다.
        """
        with cls._lock:
            if not cls._instances.get(bot_id):
                new_bot = super().__new__(cls)
                if bot_id:
                    # 챗봇의 ID로 직접 챗봇을 호출할 때는, DB에 이미 해당 챗봇의 정보가 있음.
                    if channel_ids or scope:
                        logger.warning(f"참고할 채널 정보 또는 참고 범위를 입력했지만, 챗봇 ID를 입력했기 때문에 ID를 제외한 정보는 무시됩니다. "
                                       f"Chatbot ID: {bot_id}, Channel IDs: {channel_ids}, Scope: {scope}")
                    new_bot._bot_id = bot_id
                elif channel_ids and scope: # 챗봇이 참조하는 채널 정보로 챗봇을 호출할 때는 DB에 해당하는 챗봇이 있으면 로드. 없으면 생성.
                    if bot_id := cls._get_bot_id(cls, channel_ids, scope):
                        # 채널 정보에 해당하는 봇이 있다면 그 봇의 id를 기준으로 데이터베이스에서 로드한 정보를 가지고 생성하도록 요청.
                        new_bot._bot_id = bot_id
                    else:
                        # 채널 정보에 해당하는 봇이 없으면 bot_id를 입력하지 않고 채널 정보만 입력해서 새로운 봇을 생성하도록 요청.
                        new_bot._bot_id = None
                else:
                    raise ValueError(f"챗봇을 호출할 때 챗봇의 ID 또는 채널 ID 목록과 범위 둘 중 하나는 입력해야 하지만, 모두 입력되지 않았습니다.")

                cls._instances[bot_id] = new_bot

        return cls._instances[bot_id] # 이미 있거나 생성된 봇 반환.


    def _get_bot_id(self:typing.Type['Watson'], channel_ids:list, scope:str) -> typing.Optional[int]:
        """생성된 instance 중 참고하는 채널의 목록이 같으면 해당 봇의 ID를 반환하는 메서드."""
        for bot_id, bot_instance in self._instances.items():
            # global 챗봇은 하나만 유지하므로 scope가 global이면 global 챗봇만 찾고, 아닐 경우에만 channel ids를 비교한다.
            if scope == "global":
                if bot_instance.scope == scope:
                    return bot_id
            elif sorted(list(bot_instance.chats.keys())) == sorted(map(str, channel_ids)):
                return bot_id
        return None


    def __init__(self, bot_id:int=None, channel_ids:list[int]=None, scope:str=None):
        try:
            with self._lock:
                # 이미 객체가 초기화되어 있을 경우(chats가 있고, None이 아님), 객체를 초기화하지 않고 벡터스토어만 업데이트한 후 종료.
                # 만약 chats가 아닌 _bot_id를 기준으로 한다면, __new__에서 _bot_id를 초기화한 후에 넘어오기 때문에 항상 참이 된다.
                # 때문에 chats를 기준으로 해야 함.
                if getattr(self, "chats", None):
                    self._update_vectorstore()
                    return

                logger.debug(f"메모리에 새로운 챗봇을 로드합니다. Chatbot ID: {self._bot_id}")
                if self._bot_id: # bot_id가 입력되었을 경우: 이미 DB에 정보가 저장되어 있으므로 로드.
                    bot_info = chatbot_collection.find_one({"id": self._bot_id})
                    # 데이터베이스에 id가 없으면 아직 생성하지 않은 챗봇에 접근하는 것이므로 오류.
                    if not bot_info:
                        raise KeyError(f"생성한 적이 없는 ID로 챗봇을 불러오려고 시도했습니다. Chatbot ID: {bot_id}")
                    self.chats, self.scope = bot_info.get("chats"), bot_info.get("scope")
                else:
                    if type(channel_ids) is not list or not all([isinstance(_id, int) for _id in channel_ids]):
                        raise TypeError(f"Parameter 'channel_ids' must be list[int].")

                    self._bot_id = generate_integer_id64(existing_ids=self._instances.keys())
                    self.scope = scope
                    self.chats = {}
                    for channel_id in channel_ids:
                        # 채팅 데이터 collection에서, 참고하려는 채널에서 송수신된 모든 채팅의 채팅 id를 채널 id로 나누어서 저장.
                        # 이 때, scope가 "global"이라면 모든 채널 ID를 불러와서 저장.
                        self.chats[str(channel_id)] = [chat.get('id') for chat in chat_collection.find(
                            {} if self.scope == "global" else {"channelId": channel_id}
                        )]
                    logger.debug(f"새로운 챗봇을 생성했습니다. Chatbot ID: {self._bot_id}")

                self._update_db() # MongoDB에서 현재 챗봇의 정보 업데이트 (없을 경우 신규 생성)

                self._embedding = OpenAIEmbeddings()  # 임베딩(Embedding) 생성
                self._llm = ChatOpenAI(model_name="gpt-4o", temperature=0)  # 언어모델(LLM) 생성

                self._vectorstore, self._chain = None, None
                # watson/vectorstore/<bot id> 위치에 벡터스토어 저장.
                self._vectorstore_path = os.path.join(os.path.dirname(__file__), str(self._bot_id))
                self._update_vectorstore()

        except Exception as e:
            logger.error(f"An error occurred while initializing instance: {e}")


    def _update_vectorstore(self):
        try:
            """
                다음의 경우에 RAG vectorstore를 재생성.
                1. 로컬에 저장된 벡터스토어가 없을 때
                2. MongoDB로 확인한 바, 현재 챗봇의 근거 데이터가 없을 때.
                3. MongoDB로 확인한 바, 현재 챗봇의 근거 데이터가 되는 채팅 ID 목록이 채널의 채팅 ID 목록과 서로 다를 때
            """
            if not os.path.exists(self._vectorstore_path):
                logger.info(f"There is no local vectorstore. Create vectorstore. (Local Path: {self._vectorstore_path})")
                self._build_vectorstore()  # MongoDB에서 채팅 데이터를 불러와서 vectorstore 재생성
            elif not self.chats:
                logger.info(f"There is no references for chatbot. Create vectorstore. (Local Path: {self._vectorstore_path})")
                self._build_vectorstore()
            elif not compare_dicts_sorted(self.chats, newest_chats:=load_chats(self.chats.keys())):
                self.chats = newest_chats
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

    def _load_vectorstore(self):
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
            if not self._vectorstore:
                self._vectorstore = FAISS.load_local(self._vectorstore_path, self._embedding, allow_dangerous_deserialization=True)
        except Exception as e:
            logger.error(f"An error occurred while loading vectorstore from local: {e}")

    def _save_vectorstore(self):
        try:
            self._vectorstore.save_local(self._vectorstore_path)
        except Exception as e:
            logger.error(f"An error occurred while saving vectorstore to local: {e}")


    def _update_db(self):
        try:
            if not chatbot_collection.find_one({"id": self._bot_id}):
                chatbot_collection.insert_one({
                    "id": self._bot_id,
                    "updatedAt": datetime.now(),
                    "chats": {},
                    "scope": None,
                })
            chatbot_collection.update_one({"id": self._bot_id},
                                          {"$set": {
                                              "updatedAt": datetime.now(),
                                              "chats": self.chats,
                                              "scope": self.scope,
                                          }})
        except Exception as e:
            logger.error(f"An error occurred while updating chatbot metadata at MongoDB: {e}")


    def _build_vectorstore(self):
        try:
            channel_ids = list(map(int, self.chats.keys())) # chats의 key가 str 형으로 저장되어 있기 때문에, int로 변환한 뒤 검색
            # 단계 1: 문서 로드(Load Documents)
            logger.debug(f"Loading chat data from MongoDB. Channel IDs: {channel_ids}, scope: {self.scope}")
            loader = MongodbLoader(
                connection_string=get_mongo_connection_string(),
                db_name=DB.NAME,
                collection_name=DB.COLLECTION.CHANNEL.DATA,
                filter_criteria={} if self.scope == "global" else {
                    "channelId": { "$in": channel_ids }
                },  # 데이터베이스에서 조회할 기준 (쿼리)
                field_names=("text",),
                metadata_names=("id", "timestamp", "chats", "views", "url"),  # 메타데이터로 지정할 필드 목록
            )
            docs = loader.load()
            if not docs:
                self._vectorstore = None
                logger.warning(f"There is no channel data found at DB for the bot. Channel IDs: {channel_ids}, scope: {self.scope}")
                return

            # 단계 2: 문서 분할(Split Documents)
            logger.debug(f"Splitting loaded chat documents from MongoDB. Channel IDs: {channel_ids}, scope: {self.scope}")
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
        except Exception as e:
            logger.error(f"An error occurred while building vectorstore: {e}")

    def _build_chain(self):
        try:
            if self._vectorstore:
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