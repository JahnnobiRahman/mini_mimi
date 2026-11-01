from typing import Annotated , Sequence, TypedDict #python er nijer typing system theke ei tinta jinish
from langchain_core.messages import BaseMessage  #langchain er message er base type er jonno ei jinish
from langgraph.graph import add_messages  #langgraph er puran message er shathe notun message add kore



class AgentState(TypedDict):
    """Agent state is a dictionary that contains the state of the agent."""
    messages:Annotated[Sequence[BaseMessage], add_messages] #add_messages is part of langgraph not langchain_core
    user_id : str
    session_id: str
    

   