#Study Assistant RAG Bot

A Retrieval-Augmented Generation (RAG) chatbot that answers questions from your PDFs/notes using semantic search and embeddings.

Built with LangChain + FAISS + Sentence Transformers + Streamlit.

#Features

•Ask questions from your PDFs  
•Smantic search using embeddings  
•Fast FAISS vector database  
•Clean Streamlit UI  
•Shows source pages  
•Safe “I don’t know” responses  
•Fully local (no paid API required)


#How It Works (Architecture)

1. PDFs are loaded and split into chunks  
2. Chunks are converted to embeddings  
3. FAISS stores embeddings for fast search  
4. User question → embedding search  
5. Top relevant chunks are shown as answers


