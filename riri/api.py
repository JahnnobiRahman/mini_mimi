from fastapi import FastAPI

from langchain_core.messages import HumanMessage
from pydantic import BaseModel
from fastapi.responses import StreamingResponse

from riri.graph import build_graph

app  = FastAPI()
agent = build_graph()

class ChatRequest(BaseModel):
    message:str
    session_id:str

@app.post("/chat")
def chat(request: ChatRequest):
    config = {"configurable": {"thread_id": request.session_id}}
    result = agent.invoke({"messages": [HumanMessage(content=request.message)]}, config)
    return {"reply": result["messages"][-1].text}


@app.post("/chat/stream")
def chat_stream(request: ChatRequest):
    config = {"configurable": {"thread_id": request.session_id}}
    inputs = {"messages": [HumanMessage(content=request.message)]}

    def generate():
        for chunk, metadata in agent.stream(inputs, config, stream_mode="messages"):
            if chunk.text:
                yield chunk.text

    return StreamingResponse(generate(), media_type="text/plain")