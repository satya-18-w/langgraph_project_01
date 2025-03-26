import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from src.langgraphagenticai.main import load_langgraph_agenticai_app
import streamlit as st

class GroqLLM:
    def __init__(self,user_controls):
        self.user_controls = user_controls
        
    def get_groq_llm(self):
        try:
            groq_api_key=self.user_controls["GROQ_API_KEY"]
            selected_groq_model=self.user_controls["selected_groq_model"]
            if groq_api_key == "" or os.environ["GROQ_API_KEY"] == "":
                st.error("Please enter the groq api key")
                
            llm=ChatGroq(api_key=groq_api_key,model=selected_groq_model)
            return llm
        except Exception as e:
            raise ValueError(f"Error occured with Exception {e}")
        
        