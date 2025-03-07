from langchain.vectorstores import FAISS
from langchain.embeddings.openai import OpenAIEmbeddings

# Initialize FAISS store
embeddings = OpenAIEmbeddings()
vector_db = FAISS(embedding_function=embeddings)

def store_research_data(research_text):
    """Stores research data into the vector DB."""
    vector_db.add_texts([research_text])

def retrieve_research_data(query):
    """Retrieves relevant stored research data."""
    return vector_db.similarity_search(query, k=3)
