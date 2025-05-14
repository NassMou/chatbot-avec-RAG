import os
from dotenv import load_dotenv
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage

load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

def split_text(text):
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    return splitter.split_text(text)

def build_vector_store(text):
    chunks = split_text(text)
    embeddings = OpenAIEmbeddings(openai_api_key=openai_api_key)
    return FAISS.from_texts(chunks, embeddings)

def get_relevant_chunks(query, vectorstore, k=3):
    return vectorstore.similarity_search(query, k=k)

def generate_answer(question, context):
    system_prompt = (
        "Tu es un assistant IA. Réponds uniquement en te basant sur le contenu suivant :\n\n"
        f"{context}\n\nQuestion : {question}"
    )
    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo", openai_api_key=openai_api_key)
    response = llm([HumanMessage(content=system_prompt)])
    return response.content
