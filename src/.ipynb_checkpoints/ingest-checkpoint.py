from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from pathlib import Path
from config import CHUNK_SIZE, CHUNK_OVERLAP

def load_pdfs(folder_path: str):
    docs = []
    for pdf_file in Path(folder_path).glob("*.pdf"):
        loader = PyPDFLoader(str(pdf_file))
        docs.extend(loader.load())
    return docs

def chunk_docs(documents):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP
    )
    return splitter.split_documents(documents)

if __name__ == "__main__":
    docs = load_pdfs("data/docs")
    chunks = chunk_docs(docs)
    print("Total chunks:", len(chunks))
