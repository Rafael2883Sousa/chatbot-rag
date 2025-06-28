from langchain.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
import os

DATA_DIR = "./data"
VECTOR_DIR = "./vectorstore"
CHUNK_SIZE = 500
CHUNK_OVERLAP = 50

def load_and_chunk_documents():
    documents = []
    for file in os.listdir(DATA_DIR):
        if file.endswith(".txt"):
            loader = TextLoader(os.path.join(DATA_DIR, file), encoding="utf-8")
            documents.extend(loader.load())
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP
    )
    return splitter.split_documents(documents)

def generate_embeddings():
    return HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

if __name__ == "__main__":
    print("[*] Carregando e dividindo documentos...")
    chunks = load_and_chunk_documents()
    print(f"[+] {len(chunks)} chunks carregados.")

    print("[*] Gerando embeddings...")
    embeddings = generate_embeddings()

    print("[*] Criando índice FAISS...")
    db = FAISS.from_documents(chunks, embeddings)

    print(f"[*] Salvando vetor store em: {VECTOR_DIR}")
    db.save_local(VECTOR_DIR)
    print("[+] Vetor store salvo com sucesso.")
