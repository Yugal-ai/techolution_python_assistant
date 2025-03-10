import os 
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI 

load_dotenv()

def generate_output(input_text, model):
    llm = ChatOpenAI(api_key=os.getenv("OPENAI_API_KEY"), model="o1-preview")
    response = llm.invoke(input_text)
    return response.content

