import streamlit as st
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings

st.title("Study Assistant (RAG Bot)")

embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

db = FAISS.load_local(
    "vectordb/faiss_index",
    embedding_model,
    allow_dangerous_deserialization=True
)

retriever = db.as_retriever(search_kwargs={"k": 4})

question = st.text_input("Ask a question from your PDFs:")

if question:
    docs = retriever.get_relevant_documents(question)

    st.subheader("Retrieved Context")
    for i, d in enumerate(docs):
        st.write(f"Chunk {i+1} (Page {d.metadata.get('page', 'N/A')})")
        st.write(d.page_content[:400])
