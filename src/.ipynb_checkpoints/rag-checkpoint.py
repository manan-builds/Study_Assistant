from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings

def build_vectorstore(chunks):
    embedding_model = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )
    db = FAISS.from_documents(chunks, embedding_model)
    return db

def save_vectorstore(db, path="vectordb/faiss_index"):
    db.save_local(path)
