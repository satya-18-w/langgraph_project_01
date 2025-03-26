from langgraph.graph import StateGraph,START,END
from typing_extensions import TypedDict
from typing import Annotated
from langgraph.prebuilt import tool_condition,ToolNode
from langchain_core.prompts import ChatPromptTemplate
import datetime
from src.langgraphagenticai.state.state import State
from src.langgraphagenticai.node.node import BasicChatbotNode


class GraphBuilder:
    def __init__(self,model):
        self.model=model
        self.graph_builder=StateGraph(State)
        self.nodes=BasicChatbotNode(self.model)
        
    def get_graph(self):
        self.graph_builder.add_node("process",self.nodes.process)
        self.graph_builder.add_edge(START,"process")
        self.graph_builder.add_edge("process",END)
        self.graph=self.graph_builder.compile()
        return self.graph
        