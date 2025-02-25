import os
import threading
import typing
from datetime import datetime
from os import PathLike
from typing import Any, Optional, Union

from langchain_core.vectorstores import VST
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langgraph.graph.state import CompiledStateGraph

from server.logger import logger
from utils import generate_integer_id64
from .constants import chatbot_collection, chat_collection
from .local_vectorstore import __file__ as vectorstore_path

if typing.TYPE_CHECKING:
    from watson.watson import Watson


class BaseWatson:
    _instances: dict[int, Union['BaseWatson', 'Watson']] = {}
    _session_history = {}  # 세션 기록을 저장할 딕셔너리
    _lock: threading.Lock = threading.Lock()
    error_msg_for_empty_data: str = "죄송합니다. 요청하신 채널의 데이터가 없거나, 아직 수집되지 않아 답변을 드릴 수 없습니다."
    GLOBAL: str = "global"
    MULTI: str = "multi"
    LOCAL: str = "local"
    SQLITE_CONNECTION_STRING: str = f"chats.db"

    def __new__(cls, bot_id: int = None, channel_ids: list = None, scope: str = None):
        """
            싱글톤 객체의 변형 구현.
            입력받은 channel id에 대응하는 watson 챗봇이 없을 경우에 한해,
            고유한 watson 객체를 새로 만들고 반환하는 동시에 _instances에 내부적으로 저장한다.

            만약 해당 channel id에 대응하는 챗봇이 이미 생성되었을 경우,
            그 챗봇을 반환한다.
        """
        with cls._lock:
            logger.debug(f"챗봇이 호출되었습니다. Chatbot ID: {bot_id}, Channel IDs: {channel_ids}, Scope: {scope}")
            if bot_id:
                # 챗봇의 ID로 직접 챗봇을 호출할 때는, DB에 이미 해당 챗봇의 정보가 있음.
                if channel_ids or scope:
                    logger.warning(f"참고할 채널 정보 또는 참고 범위를 입력했지만, 챗봇 ID를 입력했기 때문에 ID를 제외한 정보는 무시됩니다. "
                                   f"Chatbot ID: {bot_id}, Channel IDs: {channel_ids}, Scope: {scope}")
            elif channel_ids and scope:  # 챗봇이 참조하는 채널 정보로 챗봇을 호출할 때는 DB에 해당하는 챗봇이 있으면 로드. 없으면 생성.
                # 채널 정보에 해당하는 봇이 있다면 _get_bot_id()가 그 봇의 ID 반환
                # -> 그 봇의 id를 이용하여 데이터베이스에서 로드한 정보를 가지고 생성 or 호출하도록 요청.
                # 채널 정보에 해당하는 봇이 없으면 _get_bot_id()가 None 반환
                # -> bot_id를 입력하지 않고 채널 정보만 입력해서 생성 or 호출하도록 요청.
                bot_id = cls._get_bot_id(channel_ids, scope)

            else:
                raise ValueError(f"챗봇을 호출할 때 챗봇의 ID 또는 채널 ID 목록과 범위 둘 중 하나는 입력해야 하지만, 모두 입력되지 않았습니다.")

            # 현재 메모리에 생성된 봇이 없다면, 새 객체를 메모리에 생성.
            if not cls._instances.get(bot_id):
                new_bot = super().__new__(cls)
                new_bot._bot_id = bot_id
                cls._instances[bot_id] = new_bot

        return cls._instances[bot_id]  # 이미 있거나 방금 생성된 봇 반환.

    @classmethod
    def _get_bot_id(cls, channel_ids: list, scope: str) -> typing.Optional[int]:
        """생성된 instance 중 참고하는 채널의 목록이 같으면 해당 봇의 ID를 반환하는 메서드."""
        for bot_id, bot_instance in cls._instances.items():
            # global 챗봇은 하나만 유지하므로 scope가 global이면 global 챗봇만 찾고, 아닐 경우에만 channel ids를 비교한다.
            if scope == cls.GLOBAL:
                if bot_instance.scope == scope:
                    return bot_id
            elif sorted(list(bot_instance.chats.keys())) == sorted(map(str, channel_ids)):
                return bot_id
        return None

    def _update_db(self: 'Watson'):
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



    def __init__(self: 'Watson', bot_id: int = None, channel_ids: list[int] = None, scope: str = None):

        with self._lock:
            if getattr(self, "_initialized", False):
                self.update()
                return
            self.chats: dict[str, Any]
            self.scope: str
            self._vectorstore: Optional[VST] = None
            self._graph: Optional[CompiledStateGraph] = None
            self._initialized: bool = False
            self._llm: Any = None
            self._vectorstore_path: Optional[Union[str, PathLike]] = None
            try:
                # 이미 객체가 초기화되어 있을 경우 객체를 초기화하지 않고 벡터스토어만 업데이트한 후 종료.

                logger.debug(f"메모리에 새로운 챗봇을 로드합니다. Chatbot ID: {self._bot_id}")
                if self._bot_id:  # bot_id가 입력되었을 경우: 이미 DB에 정보가 저장되어 있으므로 로드.
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
                            {} if self.scope == self.GLOBAL else {"channelId": channel_id}
                        )]
                    logger.debug(f"새로운 챗봇을 생성했습니다. Chatbot ID: {self._bot_id}")

                self._update_db()  # MongoDB에서 현재 챗봇의 정보 업데이트 (없을 경우 신규 생성)

                self._embedding = OpenAIEmbeddings()  # 임베딩(Embedding) 생성
                self._llm = ChatOpenAI(model_name="gpt-4o", temperature=0, streaming=True)  # 언어모델(LLM) 생성

                # watson/local_vectorstore/<bot id> 위치에 벡터스토어 저장.
                self._vectorstore_path = os.path.join(os.path.dirname(vectorstore_path), str(self._bot_id))

                self.update()

                self._initialized = True

            except Exception as e:
                logger.error(f"An error occurred while initializing instance: {e}")

    @staticmethod
    def load_chats(channel_ids: typing.Iterable[typing.Union[str, int]]):
        chats = {}
        for channel_id in channel_ids:
            # 채팅 데이터 collection에서, 참고하려는 채널에서 송수신된 모든 채팅의 채팅 id를 채널 id로 나누어서 저장.
            chats[channel_id] = [chat.get('id') for chat in chat_collection.find({"channelId": int(channel_id)})]
        return chats

    def _update_chats(self, new_chats:dict[str, Any]):
        self.chats = new_chats
