import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
# from src.langgraphagenticai.main import Main
import streamlit as st

class GroqLLM:
    def __init__(self,user_controls):
        self.user_controls = user_controls
        
    def get_groq_llm(self):
        try:
            groq_api_key=self.user_controls["CHATGROQ_API_KEY"]
            selected_groq_model=self.user_controls["selected_groq_model"]
            if groq_api_key == "":
                st.error("Please enter the groq api key")
                
            load_dotenv()
            os.environ["GROQ_API_KEY"]=groq_api_key
            llm=ChatGroq(model=selected_groq_model)
            return llm
        except Exception as e:
            raise ValueError(f"Error occured with Exception {e}")
        return
        
        