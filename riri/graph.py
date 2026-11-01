from dotenv import load_dotenv
# we use langgraph 
from langgraph.graph import END, START , StateGraph
from langgraph.checkpoint.memory import MemorySaver
from pathlib import Path




from riri.state import (AgentState)

from langchain_core.messages import HumanMessage, SystemMessage
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

primary_llm = ChatGoogleGenerativeAI(model="gemini-3.8-flash")
fallback_llm = ChatGoogleGenerativeAI(model="gemini-3.5-flash-lite")
llm = primary_llm.with_fallbacks([fallback_llm])

SYSTEM_PROMPT = (Path(__file__).parent / "prompts" / "chat.txt").read_text(encoding="utf-8")

def response_node(state): 
    messages = [SystemMessage(content=SYSTEM_PROMPT)] + list(state["messages"])
    reply = llm.invoke(messages)
    # return reply.content #content mane list ashbe , 
    return{"messages":[reply]}

def build_graph():
    graph=StateGraph(AgentState)
    graph.add_node ("response_node", response_node)
    graph.add_edge(START, "response_node")
    graph.add_edge("response_node", END)
    return graph.compile(checkpointer=MemorySaver())
