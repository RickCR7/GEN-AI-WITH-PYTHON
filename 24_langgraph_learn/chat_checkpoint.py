from dotenv import load_dotenv
from typing_extensions import TypedDict
from typing import Annotated
from langgraph.graph.message import add_messages
from langgraph.graph import StateGraph, START, END
from langchain.chat_models import init_chat_model
from langgraph.checkpoint.mongodb import MongoDBSaver



load_dotenv()

llm = init_chat_model(
    model="gpt-4.1-mini",
    model_provider="openai"
)

# Creating States
class State(TypedDict):
    messages: Annotated[list, add_messages]

def chatbot(state: State):
    response = llm.invoke(state.get("messages"))
    return {"messages": [response]}



graph_builder = StateGraph(State)

# Adding nodes
graph_builder.add_node("chatbot", chatbot)

# Adding edges
graph_builder.add_edge(START, "chatbot")
graph_builder.add_edge("chatbot", END)



graph = graph_builder.compile()


def compile_graph_with_checkpointer(checkpointer):
    return graph_builder.compile(checkpointer=checkpointer)
    
    

DB_URI = "mongodb://admin:admin@127.0.0.1:27017/langgraph?authSource=admin"

with MongoDBSaver.from_conn_string(DB_URI) as checkpointer: 

    graph_with_checkpointer = compile_graph_with_checkpointer(checkpointer=checkpointer)

    config = {
            "configurable": {
                "thread_id": "akash"
            }
        }

    updated_state = graph_with_checkpointer.invoke(State({"messages": ["What is my name?"]}),
    config,)

    print("\n\nUpdated State: ", updated_state)

# (START) -> Chatbot  -> (END)

# state = {messages: ["Hey there"]}
# node runs: chatbot(state: ["Hey there"]) -> ["Hi, This is a message from Chatbot Node"]
# state = {messages: ["Hey there","Hi, This is a message from Chatbot Node"]}