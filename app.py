import streamlit as st
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_google_genai import ChatGoogleGenerativeAI
#Gen Ai is called as LLM-> Large Language Model
load_dotenv()
llm=ChatGoogleGenerativeAI(
model='gemini-2.0-flash',
temparature=0,
max_tokens=500,
Timeout=None,
max_retries=2 #parameters
)
#creating prompt
prompt=ChatPromptTemplate.from_messages(
    [
      ("system","you are a chat bot"),
      ("human","question:{question}")
    ]
)
#application
st.title('This is a chatbot by praveen')
input_text=st.text_input("enter you question here sir")

output_parser=StrOutputParser()
chain=prompt | llm | output_parser

if input_text:
  st.write(chain.invoke({'question':input_text}))
