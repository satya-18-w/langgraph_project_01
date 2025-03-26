import streamlit as st
import json
from src.langgraphagenticai.ui.streamlitui.loadui import LoadStreamlitUI
from src.langgraphagenticai.llms.groq_llm import GroqLLM
from src.langgraphagenticai.graph.graph_builder import GraphBuilder
from src.langgraphagenticai.ui.streamlitui.display_result import DisplayResultStreamlit
 # MAIN Function START
class Main:
    def __init__(self):
        self.ui=LoadStreamlitUI()
        
        
    def load_langgraph_agenticai_app(self):
        """
        Loads and runs the LangGraph AgenticAI application with Streamlit UI.
        This function initializes the UI, handles user input, configures the LLM model,
        sets up the graph based on the selected use case, and displays the output while 
        implementing exception handling for robustness.
        """
    
        # Load UI
        ui = self.ui
        user_input = ui.load_streamlit_ui()
        

        if not user_input:
            st.error("Error: Failed to load user input from the UI.")
            return

        # Text input for user message
        if st.session_state.IsFetchButtonClicked:
            user_message = st.session_state.timeframe 
        else :
            user_message = st.chat_input("Enter your message:")
            
        
        if user_message:
            try:
                obj_llm_config=GroqLLM(user_controls=user_input)
                model=obj_llm_config.get_groq_llm()
                if not model:
                    st.error("Error: Failed to load the LLM model.")    
                    return
                usecase=user_input.get("selected_usecase")
                if not usecase:
                    st.error("Error: No use case selected.")
                    return
                
                graph_builder=GraphBuilder(model)
                graph=graph_builder.get_graph()
                
                dsiresult=DisplayResultStreamlit(usecase=usecase,graph=graph,user_message=user_message)
                dsiresult.display_result_on_ui()
                
                
                
            except Exception as e:
                raise ValueError(f"Error occured : {e}")
            return
                
            