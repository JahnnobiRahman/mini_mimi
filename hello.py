from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_google_genai import ChatGoogleGenerativeAI


load_dotenv()

llm = ChatGoogleGenerativeAI(model="gemini-3.8-flash")

messages = [

    SystemMessage(content="Always reply in Banglish: Bangla language written in English letters. "
        "Never use Bangla script. Example: 'Ami bhalo achi, tumi kemon acho?'"
        ),
    HumanMessage(content="hello, k tumi kemon acho?"),

]

reply = llm.invoke(messages)
print(reply.text())