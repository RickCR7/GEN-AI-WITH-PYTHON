from dotenv import load_dotenv
from typing_extensions import TypedDict
from typing import Annotated
from langgraph.graph.message import add_messages
from langgraph.graph import StateGraph, START, END
from langchain.chat_models import init_chat_model

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

def sample_node(state: State):
    print("\n\nInside sample node", state)
    return {"messages": ["Sample message Appended"]}

graph_builder = StateGraph(State)

# Adding nodes
graph_builder.add_node("chatbot", chatbot)
graph_builder.add_node("sample_node", sample_node)

# Adding edges
graph_builder.add_edge(START, "chatbot")
graph_builder.add_edge("chatbot", "sample_node")
graph_builder.add_edge("sample_node", END)


graph = graph_builder.compile()

updated_state = graph.invoke(State({"messages": ["Hi, My name is Akash Sen"]}))

print("\n\nUpdated State: ", updated_state)

# (START) -> Chatbot -> Sample -> (END)

# state = {messages: ["Hey there"]}
# node runs: chatbot(state: ["Hey there"]) -> ["Hi, This is a message from Chatbot Node"]
# state = {messages: ["Hey there","Hi, This is a message from Chatbot Node"]}