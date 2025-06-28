from langchain.chains import RetrievalQA
from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.llms import LlamaCpp
import os

MODEL_PATH = "models/llama-2-7b-chat-hf-q4_k_m.gguf"
VECTOR_DIR = "vectorstore"
N_CTX = 2048
MAX_TOKENS = 512

def load_llm():
    return LlamaCpp(
        model_path=MODEL_PATH,
        temperature=0.7,
        max_tokens=MAX_TOKENS,
        n_ctx=N_CTX,
        verbose=True
    )

def load_vectorstore():
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    return FAISS.load_local(VECTOR_DIR, embeddings)

if __name__ == "__main__":
    print("[*] Iniciando Chatbot RAG com LLaMA + LangChain...")

    llm = load_llm()
    vectorstore = load_vectorstore()

    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=vectorstore.as_retriever(),
        return_source_documents=True
    )

    while True:
        query = input("\nUsuário: ")
        if query.lower() in ["sair", "exit", "quit"]:
            break
        resposta = qa_chain.run(query)
        print("\nChatbot:", resposta)
