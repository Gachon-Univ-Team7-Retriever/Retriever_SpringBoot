from dotenv import load_dotenv
import typing
import json, ast
from typing import Literal, Annotated, Sequence, TypedDict, Union, Optional

from langchain_core.documents import Document
from langchain_core.messages import HumanMessage, BaseMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate, ChatPromptTemplate
from langchain_core.tools import Tool, create_retriever_tool
from langchain_core.vectorstores import VectorStoreRetriever
from langchain_openai import ChatOpenAI
from langchain_teddynote.models import get_model_name, LLMs
from langgraph.constants import END, START
from langgraph.graph import StateGraph
from langgraph.graph.message import add_messages
from langgraph.graph.state import CompiledStateGraph
from langgraph.prebuilt import ToolNode, tools_condition
from pydantic import BaseModel, Field

from server.db import get_mongo_database, DB

load_dotenv()

if typing.TYPE_CHECKING:
    from watson.watson import Watson

# 최신 모델이름 가져오기
MODEL_NAME = get_model_name(LLMs.GPT4o)


# 에이전트 상태를 정의하는 타입 딕셔너리, 메시지 시퀀스를 관리하고 추가 동작 정의
class GraphState(TypedDict):
    # add_messages reducer 함수를 사용하여 메시지 시퀀스를 관리
    messages: Annotated[Sequence[BaseMessage], add_messages]
    question: Annotated[str, "Question"]  # 질문
    context: Annotated[str, "Context"]  # 문서의 검색 결과
    db_query: Annotated[str, "Query"] # 데이터베이스 쿼리
    answer: Annotated[str, "Answer"]  # 답변


def update_state(state: GraphState, node_name:str, **updates) -> GraphState:
    new_state: GraphState = state.copy()
    new_state.update(messages=[])
    new_state.update(**updates)
    return new_state


# 데이터 모델 정의
class Grade(BaseModel):
    """A binary score for relevance checks"""
    binary_classification: str = Field(
        description="Response 'metadata' if the question is based on metadata or 'data' if it is not."
    )


def load_from_dict(data: dict, content_key: str, metadata_keys=None) -> Document:
    if metadata_keys is None:
        metadata_keys = []
    return Document(page_content=data[content_key],
                    metadata={key: data[key] for key in data.keys() if key in metadata_keys})


# Root Nodes

def ask_question(state:GraphState) -> GraphState:
    print("\n=== NODE: question ===\n")
    return update_state(state, node_name="question", question=state["messages"][-1].content)


def classify_question(state:GraphState) -> str:
    """
        사용자의 초기 질문을 바탕으로 메타데이터 기반 질문인지, 데이터 기반 질문인지를 AI가 판단해서
        이진 분류(Binary Classification)을 수행하는 함수.
        메타데이터 기반일 경우 'metadata', 데이터 기반일 경우 'data'를 반환한다.
    """
    # LLM 모델 초기화
    llm = ChatOpenAI(temperature=0, model=MODEL_NAME, streaming=True)

    # 구조화된 출력을 위한 LLM 설정
    llm_with_structured_output = llm.with_structured_output(Grade)

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
        print("\n==== [DECISION: METADATA RELEVANT] ====\n")
        return "metadata"

    else:
        print("\n==== [DECISION: DATA RELEVANT] ====\n")
        return "data"


# 메타데이터 기반 질문에 대응하는 Graph Branch

def generate_db_query(state:GraphState) -> GraphState:
    print("\n=== NODE: generate db query ===\n")
    # LLM 모델 초기화
    llm = ChatOpenAI(temperature=0, model=MODEL_NAME, streaming=True)

    # SQL Query 프롬프트 템플릿 정의. 기본적으로 PromptTemplate에서 {}는 사용자 입력으로 인식되기 때문에, {{}}로 escape해야 한다.
    system_message = """You are a database manager responsible for answering user questions. 
        The database contains information about Telegram channels and all chat messages sent and received within each channel.
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
        - **`id`**: Integer. A unique ID that distinguishes each chat message within the channel.
        
        To retrieve the necessary information from the database to answer a user's question, determine which collection to query and construct the best aggregation pipeline. 
        Then, provide the result in the following JSON format:
        {{
          "collection": "<collection_name>", 
          "pipeline": [{{appropriate_query}}, {{appropriate_conditions}}, ...]
        }}
        
        If a question is asked without specifying a channel ID or any identifying information for a channel, assume that the data should be retrieved from all channels by default.
        YOU MUST RETURN ONLY JSON, without any code snippets or other Markdown formatting.
        Make sure your JSON has "collection" and "pipeline" as top-level keys.
        
        For example, if a user asks:
        "Show me the most viewed chat message in the channels after January 1, 2025."
        Then your exact response should be:
        
        {{
          "collection": "channel_data", 
          "pipeline": [
            {{
              "$match": {{
                "timestamp": {{ "$gte": ISODate("2025-01-01T00:00:00Z") }}
              }}
            }},
            {{ "$sort": {{ "views": -1 }} }},
            {{ "$limit": 1 }}
          ]
        }}"""

    prompts =  ChatPromptTemplate.from_messages([
        ("system", system_message),
        ("user", "{question}"),
    ])


    # prompt + llm 바인딩 체인 생성
    chain = prompts | llm

    # 최초 질문 추출
    question = state["question"]

    # 데이터베이스 쿼리 받기
    query = chain.invoke({"question": question}).content

    return update_state(state, node_name="generate_db_query", db_query=query)


def validate_db_query(state:GraphState) -> GraphState:
    print("\n=== NODE: validate db query ===\n")
    return update_state(state, node_name="validate_db_query")


def evaluate_db_query(state:GraphState) -> str:
    print("\n=== BRANCH: evaluate db query ===\n")
    decision = "end"
    return decision


def rewrite_db_query(state:GraphState) -> GraphState:
    print("\n=== NODE: rewrite db query ===\n")
    return update_state(state, node_name="rewrite_db_query")


def execute_db_query(state:GraphState) -> GraphState:
    print("\n=== NODE: execute db query ===\n")
    query_info = json.loads(state["db_query"])
    collection_name, pipeline = query_info["collection"], query_info["pipeline"]
    cursor = get_mongo_database(DB.NAME)[collection_name].aggregate(pipeline)
    context = [load_from_dict(doc, content_key="text", metadata_keys=["views", "url", "id", "timestamp"]) for doc in cursor] if collection_name == "channel_data" else list(cursor)

    return update_state(state, node_name="execute_db_query", context=context)


# 데이터 기반 질문에 대응하는 Graph Branch

def execute_retriever(state:GraphState) -> GraphState:
    print("\n=== NODE: execute retriever ===\n")
    return update_state(state, node_name="execute_retriever")


def validate_retrieved_context(state:GraphState) -> GraphState:
    print("\n=== NODE: validate retrieved context ===\n")
    return update_state(state, node_name="validate_retrieved_context")


def evaluate_retrieved_context(state:GraphState) -> str:
    print("\n=== BRANCH: evaluate retrieved context ===\n")
    decision = "generate"
    return decision


def rewrite_question(state:GraphState) -> GraphState:
    print("\n=== NODE: rewrite question ===\n")
    return update_state(state, node_name="rewrite_question")


def handle_error(state:GraphState) -> GraphState:
    print("\n=== NODE: handle error ===\n")
    return update_state(state, node_name="handle_error")

# 모든 것이 검증된 후 context를 기반으로 답변을 생성하는 Graph Branch

def generate(state:GraphState) -> GraphState:
    print("\n=== NODE: generate ===\n")
    prompt_template = PromptTemplate.from_template(
        """You are an AI assistant helping an investigator trying to investigate a drug-selling channel. You are specialized in Question-Answering (QA) tasks within a Retrieval-Augmented Generation (RAG) system. 
        Your primary mission is to answer questions based on provided context or chat history.
        Provided context is chat data collected from a Telegram channel where drugs are sold.
        Ensure your response is concise and directly addresses the question without any additional narration.

        ###

        Your final answer should be written concisely (but include important numerical values, technical terms, jargon, and names), followed by the source of the information.

        # Steps

        1. Carefully read and understand the context provided.
        2. Identify the key information related to the question within the context.
        3. Formulate a concise answer based on the relevant information.
        4. Ensure your final answer directly addresses the question.
        5. List the source of the answer in bullet points, which must be a url of the document, followed by brief part of the context. Omit if the source cannot be found.

        # Output Format:
        [Your final answer here, with numerical values, technical terms, jargon, and names in their original language]

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

        # Here is the user's QUESTION that you should answer:
        {question}

        # Here is the CONTEXT that you should use to answer the question:
        {context}

        # Your final ANSWER to the user's QUESTION:"""
    )

    # RAG 체인 구성
    rag_chain = prompt_template | ChatOpenAI(model_name=MODEL_NAME, temperature=0, streaming=True) | StrOutputParser()

    # 답변 생성 실행
    response = rag_chain.invoke({"context": state["context"], "question": state["question"]})

    return update_state(state, node_name="generate", messages=[response])


def build_graph(retriever_tool) -> CompiledStateGraph:
    retriever_tool_node = ToolNode([retriever_tool])

    workflow = StateGraph(GraphState)

    workflow.add_node("ask_question", ask_question)
    workflow.add_node("generate_db_query", generate_db_query)
    workflow.add_node("validate_db_query", validate_db_query)
    workflow.add_node("rewrite_db_query", rewrite_db_query)
    workflow.add_node("execute_db_query", execute_db_query)
    workflow.add_node("execute_retriever", execute_retriever)
    workflow.add_node("retrieve", retriever_tool_node)
    # workflow.add_node("validate_retrieved_context", retriever_tool_node)
    workflow.add_node("rewrite_question", rewrite_question)
    workflow.add_node("generate", generate)
    # workflow.add_node("handle_error", handle_error)

    # 시작점 설정
    workflow.set_entry_point("ask_question")
    # 첫 분기(메타데이터 기반인지/데이터 기반인지 분류)
    workflow.add_conditional_edges(
        "ask_question",
        classify_question,
        {
            # 조건 출력을 그래프 노드에 매핑
            "metadata": "generate_db_query",
            "data": "execute_retriever",
        }
    )

    # 메타데이터 기반일 경우 Branch
    workflow.add_edge("generate_db_query", "validate_db_query")
    workflow.add_conditional_edges(
        "validate_db_query",
        evaluate_db_query,
        {
            "rewrite_query": "rewrite_db_query",
            "end": "execute_db_query",
        }
    )
    workflow.add_edge("rewrite_db_query", "validate_db_query")
    workflow.add_edge("execute_db_query", "generate")

    # 데이터 기반일 경우의 Branch
    workflow.add_edge("execute_retriever", "retrieve")
    workflow.add_conditional_edges(
        "retrieve",
        evaluate_retrieved_context,
        {
            "rewrite_question": "rewrite_question",
            "generate": "generate",
        }
    )
    workflow.add_edge("rewrite_question", "retrieve")

    # 그래프 종료
    workflow.add_edge("generate", END)

    return workflow.compile()
