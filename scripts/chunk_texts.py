from langchain.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.docstore.document import Document
import os

DATA_DIR = "./data"
CHUNK_SIZE = 500
CHUNK_OVERLAP = 50

def load_documents(path):
    documents = []
    for file in os.listdir(path):
        if file.endswith(".txt"):
            loader = TextLoader(os.path.join(path, file), encoding="utf-8")
            documents.extend(loader.load())
    return documents

def split_documents(docs, chunk_size=CHUNK_SIZE, overlap=CHUNK_OVERLAP):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=overlap
    )
    return splitter.split_documents(docs)

if __name__ == "__main__":
    print("[*] Carregando documentos...")
    docs = load_documents(DATA_DIR)
    print(f"[+] {len(docs)} documentos carregados.")

    print("[*] Gerando chunks...")
    chunks = split_documents(docs)
    print(f"[+] {len(chunks)} chunks gerados.")

    print("\nExemplo de chunk:\n")
    print(chunks[0].page_content)
