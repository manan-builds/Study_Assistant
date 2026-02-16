from ingest import load_pdfs, chunk_docs
from rag import build_vectorstore, save_vectorstore
from config import DOCS_PATH

print("Loading PDFs...")
docs = load_pdfs(DOCS_PATH)

print("Chunking documents...")
chunks = chunk_docs(docs)

print("Building FAISS vector store...")
db = build_vectorstore(chunks)

print("Saving vector store to disk...")
save_vectorstore(db)

print("Vector DB built successfully!")
