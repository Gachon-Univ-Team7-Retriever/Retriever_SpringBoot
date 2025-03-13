import sqlite3
import typing
from typing import Any, Literal, Annotated, Sequence, TypedDict, Union

from dotenv import load_dotenv
from langchain_core.documents import Document
from langchain_core.messages import HumanMessage, BaseMessage
from langchain_core.prompts import PromptTemplate, ChatPromptTemplate
from langchain_core.runnables import RunnableConfig
from langchain_core.tools import create_retriever_tool
from langchain_core.vectorstores import VectorStoreRetriever
from langchain_openai import ChatOpenAI
from langchain_teddynote.models import get_model_name, LLMs
from langgraph.checkpoint.sqlite import SqliteSaver
from langgraph.constants import END
from langgraph.graph import StateGraph
from langgraph.graph.message import add_messages
from langgraph.graph.state import CompiledStateGraph
from langgraph.prebuilt import ToolNode
from pydantic import BaseModel, Field, Json

from server.db import get_mongo_database, DB
from server.logger import logger

load_dotenv()

if typing.TYPE_CHECKING:
    from watson.watson import Watson

# 최신 모델이름 가져오기
MODEL_NAME = get_model_name(LLMs.GPT4o)

DB_INFORMATION = """The MongoDB database contains information about Telegram channels and all chat messages sent and received within each channel.
The database contains two collections: `"channel_info"` for storing channel information and `"channel_data"` for storing chat messages within channels. The schema for each collection is as follows:  
### **`channel_info` Collection**  
- **`id`**: Integer. The unique ID of the channel.  
- **`title`**: String. The name of the channel.  
- **`username`**: String. The `@username` of the channel.  
- **`date`**: Datetime. The date and time when the channel was created.  

### **`channel_data` Collection**  
- **`channelId`**: Integer. The ID of the channel the chat belongs to. Linked to the `"id"` field in the `"channel_info"` collection.  
- **`text`**: String. The content of the chat message.  
- **`views`**: Integer. The number of views the chat message has received.  
- **`url`**: String. The URL of the chat message.  
- **`id`**: Integer. A unique ID that distinguishes each chat message within the channel."""


class Query(BaseModel):
    """JSON for database request"""
    collection: str = Field(description="The name of collection to query.")
    pipeline: Json[list[dict[str, Any]]] = Field(description="The best aggregation pipeline of query to answer user question.")

# 에이전트 상태를 정의하는 타입 딕셔너리, 메시지 시퀀스를 관리하고 추가 동작 정의
class GraphState(TypedDict):
    # add_messages reducer 함수를 사용하여 메시지 시퀀스를 관리
    messages: Annotated[Sequence[BaseMessage], add_messages]
    question: Annotated[str, "Question"]  # 질문
    context: Annotated[Union[str, Sequence[BaseMessage]], "Context"]  # 문서의 검색 결과
    db_query: Annotated[Query, "Query"] # 데이터베이스 쿼리
    answer: Annotated[str, "Answer"]  # 답변
    debug: Annotated[bool, "Debug"]

def update_state(state: GraphState, node_name:str, **updates) -> GraphState:
    new_state: GraphState = state.copy()
    new_state.update(**updates)
    return new_state


def load_from_dict(data: dict, content_key: str, metadata_keys=None) -> Document:
    if metadata_keys is None:
        metadata_keys = []
    return Document(page_content=data[content_key],
                    metadata={key: data[key] for key in data.keys() if key in metadata_keys})


class LangGraphMethods:

    # Root Nodes

    @staticmethod
    def ask_question(state:GraphState) -> GraphState:
        if state.get("debug"):
            print("\n=== NODE: question ===\n")
        return update_state(state, node_name="question", question=state["messages"][-1].content)

    @staticmethod
    def classify_question(state:GraphState) -> Literal["metadata", "data", "history"]:
        """
            사용자의 초기 질문을 바탕으로 메타데이터 기반 질문인지, 데이터 기반 질문인지, 이전 답변 기반 질문인지를 AI가 판단해서
            이진 분류(Binary Classification)을 수행하는 함수.
            메타데이터 기반일 경우 'metadata', 데이터 기반일 경우 'data'를 반환한다.
        """
        # 데이터 모델 정의
        class Classification(BaseModel):
            """A binary score for relevance checks"""
            binary_classification: str = Field(
                description="Response 'metadata' if the question is based on metadata, 'data' if it is based on data, 'history' if it is based on previous chat history between us."
            )

        # LLM 모델 초기화 -> 구조화된 출력을 위한 LLM 설정
        llm_with_structured_output = ChatOpenAI(temperature=0, model=MODEL_NAME, streaming=True).with_structured_output(Classification)

        # 이진 분류를 요구하는 프롬프트 템플릿 정의
        prompt = PromptTemplate(
            template="""You are a classifier assessing relevance of a user question. \n 
                The user asks you about chat data from messanger application.
                Here is the user question: {question} \n
                If it is necessary to use metadata to answer the question, classify it as 'metadata'.\n
                Give a binary classification 'metadata' or 'data' to indicate whether the document is based on metadata or data.""",
            input_variables=["question"],
        )

        # prompt + llm 바인딩 체인 생성
        chain = prompt | llm_with_structured_output

        # 최초 질문 추출
        question = state["question"]

        # 관련성 평가 실행
        classification_result = chain.invoke({"question": question})

        # 관련성 여부에 따른 결정
        if classification_result.binary_classification == "metadata":
            if state.get("debug"):
                print("\n==== [DECISION: METADATA RELEVANT] ====\n")
            return "metadata"

        elif classification_result.binary_classification == "history":
            if state.get("debug"):
                print("\n==== [DECISION: HISTORY RELEVANT] ====\n")
            state["context"] = ""
            return "history"
        else:
            if state.get("debug"):
                print("\n==== [DECISION: DATA RELEVANT] ====\n")
            return "data"


    # 메타데이터 기반 질문에 대응하는 Graph Branch
    @staticmethod
    def generate_db_query(state:GraphState) -> GraphState:
        if state.get("debug"):
            print("\n=== NODE: generate db query ===\n")
        # LLM 모델 초기화
        llm = ChatOpenAI(temperature=0, model=MODEL_NAME, streaming=True).with_structured_output(Query)

        # SQL Query 프롬프트 템플릿 정의. 기본적으로 PromptTemplate에서 {}는 사용자 입력으로 인식되기 때문에, {{}}로 escape해야 한다.
        system_message = """You are a MongoDB manager responsible for answering user questions. 
        
            # Database Information: 
            {database_information}
            
            # Your Primary Mission:
            To retrieve the necessary information from the database to answer a user's question, determine which collection to query and construct the best aggregation pipeline. 
            Then, provide the result like the following:
            collection: <collection_name>, 
            pipeline: [{{appropriate_query}}, {{appropriate_conditions}}, ...]
            
            If the user question is asked without specifying a channel ID or any identifying information for a channel, assume that the data should be retrieved from all channels by default.
            The collection should be only string, which is name of the collection to query.
            The aggregation pipeline should be list of JSON, which is directly convertible to JSON. 
            Both collection and pipeline should be without any Markdown formatting or other unnecessary text.  
            
            # Example:
            For example, if a user asks:
            "Show me the most viewed chat message in the channels after January 1, 2025."
            Then your exact response should be:
            
            collection: channel_data
            pipeline: [
              {{
                "$match": {{
                  "timestamp": {{ "$gte": ISODate("2025-01-01T00:00:00Z") }}
                }}
              }},
              {{ "$sort": {{ "views": -1 }} }},
              {{ "$limit": 1 }}
            ]
            """

        prompts =  ChatPromptTemplate.from_messages([
            ("system", system_message),
            ("user", "{question}"),
        ])


        # prompt + llm 바인딩 체인 생성
        chain = prompts | llm

        # 최초 질문 추출
        question = state["question"]

        # 데이터베이스 쿼리 받기
        query = chain.invoke({"database_information": DB_INFORMATION, "question": question})

        return update_state(state, node_name="generate_db_query", db_query=query)

    @staticmethod
    def validate_db_query(state:GraphState) -> GraphState:
        if state.get("debug"):
            print("\n=== NODE: validate db query ===\n")
        return update_state(state, node_name="validate_db_query")

    @staticmethod
    def evaluate_db_query(state:GraphState) -> Literal["rewrite_query", "end"]:
        if state.get("debug"):
            print("\n=== BRANCH: evaluate db query ===\n")
        class NextAction(BaseModel):
            """A binary score for relevance checks"""
            next_action: str = Field(
                description="Response 'end' if the collection and pipeline is correctly formatted or 'rewrite_query' if it is not."
            )
            reason: str = Field(
                description="The reason why you chose the next action."
            )
        # LLM 모델 초기화 -> 구조화된 출력을 위한 설정
        llm_with_structured_output = ChatOpenAI(temperature=0, model=MODEL_NAME, streaming=True).with_structured_output(NextAction)

        # SQL Query 프롬프트 템플릿 정의. 기본적으로 PromptTemplate에서 {}는 사용자 입력으로 인식되기 때문에, {{}}로 escape해야 한다.
        system_message = """You are an evaluator responsible for assessing whether the generated MongoDB query is appropriate for the given user question.
            # Database Information: 
            {database_information}
            
            # Your Primary Mission:
            Based on the provided channel information, evaluate whether the JSON adheres to the following criteria:
            
            1. The top-level keys in the JSON must be exactly two: "collection", which specifies the collection to query, and "pipeline", which represents the aggregation pipeline.
            2. The value of the "collection" key must be either "channel_info" or "channel_data".
            3. The value of the "pipeline" key must be an array containing a valid aggregation pipeline that correctly retrieves the requested data.
            4. If the user question is asked without specifying a channel ID or any identifying information for a channel, assume that the data should be retrieved from all channels by default.
            5. The response must contain only string and JSON, without any Markdown formatting or other non-JSON text. 
            6. The aggregation pipeline should be directly convertible to JSON.
            
            If the JSON is correctly formatted, return "end".
            If there is an issue, such as selecting the wrong collection, constructing an incorrect query, or violating any of the above requirements, return "rewrite_query".
    
            # Example:
            For example, if a user asks:
            "Show me the most viewed chat message in the channels after January 1, 2025."
            and JSON is:
            
            collection: channel_data
            pipeline: ```json
            [
              {{
                "$match": {{
                  "timestamp": {{ "$gte": ISODate("2025-01-01T00:00:00Z") }}
                }}
              }},
              {{ "$sort": {{ "views": -1 }} }},
              {{ "$limit": 1 }}
            ]
            ```
            In this case, even if all other conditions are met, the presence of unnecessary Markdown formatting strings like json makes it impossible to directly convert the response to JSON. Therefore, the correct answer of this case is "rewrite_query".
            """

        prompts = ChatPromptTemplate.from_messages([
            ("system", system_message),
            ("user", """
            # User Question:
            {question}
            
            # collection:
            {collection}
            # pipeline:
            {pipeline}
            """),
        ])

        # prompt + llm 바인딩 체인 생성
        chain = prompts | llm_with_structured_output

        # 데이터베이스 쿼리 받기
        answer = chain.invoke({
            "database_information": DB_INFORMATION,
            "question": state["question"],
            "collection": state["db_query"].collection,
            "pipeline": state["db_query"].pipeline,
        })

        if answer.next_action == "end":
            return "end"
        return "rewrite_query"

    @staticmethod
    def rewrite_db_query(state:GraphState) -> GraphState:
        if state.get("debug"):
            print("\n=== NODE: rewrite db query ===\n")
        return update_state(state, node_name="rewrite_db_query")

    @staticmethod
    def execute_db_query(state:GraphState) -> GraphState:
        if state.get("debug"):
            print("\n=== NODE: execute db query ===\n")
        collection_name, pipeline = state["db_query"].collection, state["db_query"].pipeline
        cursor = get_mongo_database(DB.NAME)[collection_name].aggregate(pipeline) # state["db_query"].pipeline 은 Pydantic 의 Json 형식으로 지정되었으므로 바로 사용 가능
        context = [load_from_dict(doc, content_key="text", metadata_keys=["views", "url", "id", "timestamp"]) for doc in cursor] if collection_name == "channel_data" else list(cursor)

        return update_state(state, node_name="execute_db_query", context=context)


    # 데이터 기반 질문에 대응하는 Graph Branch
    @staticmethod
    def execute_retriever(state:GraphState, retriever_tool:VectorStoreRetriever) -> GraphState:
        if state.get("debug"):
            print("\n=== NODE: execute retriever ===\n")
        # rewrite_question에서 넘어온 경우에 원래 질문에서 바뀐 다른 새로운 질문을 입력해야 하므로, 현재 상태에서 마지막 메시지(질문) 추출.
        question = state["messages"][-1].content

        # LLM 모델 초기화
        model = ChatOpenAI(temperature=0, streaming=True, model=MODEL_NAME)

        # retriever tool 바인딩 & 도구를 호출하는 것을 강제
        model = model.bind_tools([retriever_tool], tool_choice=retriever_tool.name)

        # 에이전트 응답 생성
        response = model.invoke(question)

        return update_state(state, node_name="execute_retriever", messages=[response])

    @staticmethod
    def validate_retrieved_context(state:GraphState) -> GraphState:
        if state.get("debug"):
            print("\n=== NODE: validate retrieved context ===\n")
        # 가장 마지막 메시지 추출 (가장 마지막 메세지가 retrieve ToolNode가 생성한 ToolMessage) -> 검색된 문서 추출
        retrieved_docs = state["messages"][-1].content
        return update_state(state, node_name="validate_retrieved_context", context=retrieved_docs)

    @staticmethod
    def evaluate_retrieved_context(state:GraphState) -> Literal["generate", "rewrite_question"]:
        if state.get("debug"):
            print("\n=== BRANCH: evaluate retrieved context ===\n")

        # 데이터 모델 정의
        class Grade(BaseModel):
            """A binary score for relevance checks"""

            binary_score: str = Field(
                description="Response 'yes' if the document is relevant to the question or 'no' if it is not."
            )
            reason: str = Field(
                description="The reason why you graded this document as your decision."
            )

        # LLM 모델 초기화 & 구조화된 출력을 위한 LLM 설정
        llm_with_tool = ChatOpenAI(temperature=0, model=MODEL_NAME, streaming=True).with_structured_output(Grade)

        # 프롬프트 템플릿 정의
        prompt = PromptTemplate(
            template="""You are a grader assessing relevance of a retrieved document to a user question. \n 
            Here is the retrieved document: \n\n {context} \n\n
            Here is the user question: {question} \n
            If the document contains keyword(s) or semantic meaning related to the user question, grade it as relevant. \n
            Give a binary score 'yes' or 'no' score to indicate whether the document is relevant to the question.""",
            input_variables=["context", "question"],
        )

        # llm + tool 바인딩 체인 생성
        chain = prompt | llm_with_tool

        # 원래 질문과 현재 retriever로 검색한 context 문서 간의 관련성 평가 실행
        scored_result = chain.invoke({"question": state["question"], "context": state["context"]})

        # 관련성 여부 추출
        score = scored_result.binary_score

        # 관련성 여부에 따른 결정
        if score == "yes":
            if state.get("debug"):
                print("==== [DECISION: DOCS RELEVANT] ====")
            return "generate"

        else:
            if state.get("debug"):
                print("==== [DECISION: DOCS NOT RELEVANT] ====")
            return "rewrite_question"

    @staticmethod
    def rewrite_question(state:GraphState) -> GraphState:
        if state.get("debug"):
            print("\n=== NODE: rewrite question ===\n")
        # 원래 질문 추출
        question = state["question"]

        # 질문 개선을 위한 프롬프트 구성
        msg = [
            HumanMessage(
                content=f""" \n 
            Look at the input and try to reason about the underlying semantic intent / meaning. \n 
            Here is the initial question:
            \n ------- \n
            {question} 
            \n ------- \n
            Formulate an improved question: """,
            )
        ]

        # LLM 모델로 질문 개선
        model = ChatOpenAI(temperature=0, model=MODEL_NAME, streaming=True)
        # Query-Transform 체인 실행
        response = model.invoke(msg)
        return update_state(state, node_name="rewrite_question", messages=[response])

    @staticmethod
    def handle_error(state:GraphState) -> GraphState:
        if state.get("debug"):
            print("\n=== NODE: handle error ===\n")
        return update_state(state, node_name="handle_error")

    # 모든 것이 검증된 후 context를 기반으로 답변을 생성하는 Graph Branch
    @staticmethod
    def generate(state:GraphState) -> GraphState:
        if state.get("debug"):
            print("\n=== NODE: generate ===\n")
        indication = """You are an AI assistant helping an investigator trying to investigate a drug-selling channel. You are specialized in Question-Answering (QA) tasks within a Retrieval-Augmented Generation (RAG) system. 
            Your primary mission is to answer questions based on provided context or chat history.
            Provided context is chat data collected from a Telegram channel where drugs are sold.
            Ensure your response is concise and directly addresses the question.
    
            ###
    
            Your final answer should be written concisely (but include important numerical values, technical terms, jargon, and names), followed by the source of the information.
    
            # Steps
    
            1. Carefully read and understand the context provided and the chat history.
            2. Identify the key information related to the question within the context.
            3. Formulate a concise answer based on the relevant information.
            4. Ensure your final answer directly addresses the question.
            5. List the source of the answer in bullet points, which must be a url of the document, followed by brief part of the context. Omit if the source cannot be found.
    
            # Output Format:
            
            Your final answer here, with numerical values, technical terms, jargon, and names in their original language
    
            **Source**(Optional)
            - (Source of the answer, must be a url of the document, followed by brief part of the context. Omit if you can't find the source of the answer.)
            - (list more if there are multiple sources)
            - ...
    
            ###
    
            Remember:
            - It's crucial to base your answer solely on the **PROVIDED CONTEXT**. 
            - DO NOT use any external knowledge or information not present in the given materials.
            - If you can't find the source of the answer, you should answer that you don't know.
    
            ###
            
            # Here is the CONTEXT that you should use to answer the question:
            {context}"""
        # prompt에 state["messages"]를 풀어서 같이 제공한다.
        # memory를 설정하면 state["messages"]에 계속해서 대화 기록이 저장되기 때문에,
        # 이를 AI가 받아서 이전 채팅 기록에 근거한 답변을 생성할 수 있게 된다.
        prompt = ChatPromptTemplate.from_messages([
            *state["messages"],
            ("system", indication),
            ("human", "{question}"),
        ])

        # RAG 체인 구성.
        # StrOutParser()를 사용하면 결과가 문자열이 되어서 state["messages"]에 추가될 때 자동으로 HumanMessage로 타입이 변환되기 때문에,
        # Memory에 저장 후 AI에게 제공해도 AI가 이를 AI의 응답으로 인식하지 못한다.
        # 따라서 StrOutputParser는 사용하지 말자.
        rag_chain = prompt | ChatOpenAI(model_name=MODEL_NAME, temperature=0, streaming=True)

        # 답변 생성
        response = rag_chain.invoke({"context": state["context"], "question": state["question"]})
        return update_state(state, node_name="generate", messages=[response])


    def build_graph(self:'Watson') -> CompiledStateGraph:
        # 도구 초기화
        retriever_tool = create_retriever_tool(
            retriever=self._vectorstore.as_retriever(search_kwargs={"k": 6}),  # 6개의 문서 검색,
            name="retrieve_chats_in_telegram_channel",
            description="Searches and returns a few chat messages from the Telegram channel that are most relevant to the question.",
            document_prompt=PromptTemplate.from_template(
                "<document><context>{page_content}</context><metadata><timestamp>{timestamp}</timestamp><url>{url}</url><views>{views}</views></metadata></document>"
            ),
        )

        retriever_tool_node = ToolNode([retriever_tool])

        workflow = StateGraph(GraphState)

        workflow.add_node("ask_question", self.ask_question)
        workflow.add_node("generate_db_query", self.generate_db_query)
        workflow.add_node("validate_db_query", self.validate_db_query)
        workflow.add_node("rewrite_db_query", self.rewrite_db_query)
        workflow.add_node("execute_db_query", self.execute_db_query)
        workflow.add_node("execute_retriever", lambda state: self.execute_retriever(state, retriever_tool))
        workflow.add_node("retrieve", retriever_tool_node)
        workflow.add_node("validate_retrieved_context", self.validate_retrieved_context)
        workflow.add_node("rewrite_question", self.rewrite_question)
        workflow.add_node("generate", self.generate)
        # workflow.add_node("handle_error", handle_error)

        # 시작점 설정
        workflow.set_entry_point("ask_question")
        # 첫 분기(메타데이터 기반인지/데이터 기반인지 분류)
        workflow.add_conditional_edges(
            "ask_question",
            self.classify_question,
            {
                # 조건 출력을 그래프 노드에 매핑
                "metadata": "generate_db_query",
                "data": "execute_retriever",
                "history": "generate",
            }
        )

        # 메타데이터 기반일 경우 Branch
        workflow.add_edge("generate_db_query", "validate_db_query")
        workflow.add_conditional_edges(
            "validate_db_query",
            self.evaluate_db_query,
            {
                "rewrite_query": "rewrite_db_query",
                "end": "execute_db_query",
            }
        )
        workflow.add_edge("rewrite_db_query", "validate_db_query")
        workflow.add_edge("execute_db_query", "generate")

        # 데이터 기반일 경우의 Branch
        workflow.add_edge("execute_retriever", "retrieve")
        workflow.add_edge("retrieve", "validate_retrieved_context")
        workflow.add_conditional_edges(
            "validate_retrieved_context",
            self.evaluate_retrieved_context,
            {
                "rewrite_question": "rewrite_question",
                "generate": "generate",
            }
        )
        workflow.add_edge("rewrite_question", "execute_retriever")

        # 그래프 종료
        workflow.add_edge("generate", END)

        # 메모리 저장소 생성
        conn = sqlite3.connect(self.SQLITE_CONNECTION_STRING, check_same_thread=False)
        memory = SqliteSaver(conn)

        logger.debug("Built a new LangGraph Workflow.")
        return workflow.compile(checkpointer=memory)

    def _load_graph(self: 'Watson'):
        if not self._graph:
            self._graph = self.build_graph()


    # 체인 실행(Run Chain)
    # 문서에 대한 질의를 입력하고, 답변을 출력한다.
    def ask(self: 'Watson', question: str):
        # chain이 있으면 chain을 실행하고 답변을 반환. chain이 없으면 에러 메세지 반환.
        inputs = {
            "messages": [
                ("user", question),
            ]
        }

        # config 설정(재귀 최대 횟수, thread_id)
        config = RunnableConfig(recursion_limit=10, configurable={"thread_id": self._bot_id})

        # 그래프를 스트리밍하려면:
        # stream_graph(self._graph, inputs, config, list(self._graph.nodes.keys()))
        answer = self._graph.invoke(
            inputs, # 질문 입력
            # 세션 ID 기준으로 대화를 기록. 현재는 세션 ID가 고정이라서 bot 하나당 하나의 세션만 유지됨.
            config=config
        )["messages"][-1].content if self._graph else self.error_msg_for_empty_data
        logger.info(f"Chatbot answered to a question. Q: '{question}', A: '{answer}'")
        return answer


    def clear_message_history(self: 'Watson'):
        """
            주어진 세션(session_id)에 해당하는 메시지 히스토리를 삭제하는 메서드.
        """
        query1 = f"DELETE FROM `checkpoints` WHERE `thread_id` = ?"
        query2 = f"DELETE FROM `writes` WHERE `thread_id` = ?"
        connection = sqlite3.connect(self.SQLITE_CONNECTION_STRING, check_same_thread=False)
        cursor = connection.cursor()
        cursor.execute(query1, (self._bot_id,))
        cursor.execute(query2, (self._bot_id,))
        connection.commit()
        cursor.close()

    def get_snapshot(self: 'Watson'):
        # 그래프 상태 스냅샷 생성해서 반환
        return self._graph.get_state(config=RunnableConfig(configurable={"thread_id": self._bot_id}))