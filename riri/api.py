from fastapi import FastAPI

from langchain_core.messages import HumanMessage
from pydantic import BaseModel

from riri.graph import build_graph

app  = FastAPI()
agent = build_graph()

class ChatRequest(BaseModel):
    message:str
    session_id:str

@app.post("/chat")

def chat (request:ChatRequest):
    config = {"configurable" : {"thread_id":request.session_id}}
    result = agent.invoke({"messages":[HumanMessage(content=request.message)]}, config)
    return {"reply" : result["messages"][-1].text}


