from dotenv import load_dotenv

load_dotenv()

from server.logger import logger

from .rag import BaseWatson, LangGraphMethods, VectorStoreMethods, chatbot_collection


# 클래스 정의가 완료되는 시점(클래스 선언 시점)에 미리 인스턴스를 생성하는 메타클래스.
class AutoCreateInstances(type):
    def __init__(cls, name, bases, dct):
        super().__init__(name, bases, dct)
        # _instances 변수를 초기화
        cls._instances = {}
        # 클래스가 생성되자마자 챗봇의 메타데이터를 다운로드, 챗봇 ID마다 인스턴스를 생성해서 등록
        for document in chatbot_collection.find():
            cls._instances[document.get('id')] = cls(bot_id=document.get('id'))

        logger.info(f"데이터베이스에 있는 챗봇을 모두 로드했습니다. 로드된 챗봇: {list(cls._instances.keys())}")


class Watson(BaseWatson, VectorStoreMethods, LangGraphMethods, metaclass=AutoCreateInstances):
    pass
