from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate, HumanMessagePromptTemplate
from langchain_core.output_parsers import StrOutputParser

import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()

os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")

##LangSMith tracking
os.environ["LANGCHAIN_TRACING_V2"] = "true"

## Prompt Template

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant. Please response to the user queries."),
    ("user","Question: {question}")
])

## streamlit framework

st.title("Chat with Groq LLM")
input_text = st.text_input("Search the topic you want")

# groq LLM model
llm = ChatGroq(model="llama-3.1-8b-instant", temperature=0.7)
output_parser = StrOutputParser()
chain = prompt | llm | output_parser

if input_text:
    st.write(chain.invoke({"question": input_text}))

# print("model is used :", llm.model)