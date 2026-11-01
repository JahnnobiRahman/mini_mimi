from langchain_core.messages import HumanMessage

from riri.graph import build_graph

agent = build_graph()

config = {"configurable":{"thread_id":"session-1"} }

while True:

    text = input("Tumi: ").strip()

    if not text : 
        continue

    if text == "exit":
        break
  
    
    result = agent.invoke({"messages":[HumanMessage(content=text)]}, config)
    print("Riri:", result["messages"][-1].text)


    