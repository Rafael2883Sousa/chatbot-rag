
# Implementação com o prompt

import subprocess
from langchain.chains import RetrievalQA
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings

import os

VECTOR_DIR = "vectorstore"
LLAMA_CLI_PATH = r"C:\Users\Benuilson Sousa\Documents\Raf\Seminário Stiven\llama-b5760-bin-win-cpu-x64\llama-cli.exe"  
MODEL_PATH = r"models\llama-2-7b-chat-hf-q4_k_m.gguf"

def load_vectorstore():
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    return FAISS.load_local(VECTOR_DIR, embeddings, allow_dangerous_deserialization=True)

def run_llama_cli(prompt, max_tokens=512):
    result = subprocess.run(
        [
            LLAMA_CLI_PATH,
            "-m", MODEL_PATH,
            "-p", prompt,
            "--n-predict", str(max_tokens),
            "--ctx-size", "2048",
        ],
        capture_output=True,
        text=True
    )
    return result.stdout.strip()

if __name__ == "__main__":
    print("[*] Iniciando Chatbot RAG com LLaMA via subprocess + LangChain...")

    vectorstore = load_vectorstore()

    retriever = vectorstore.as_retriever()

    while True:
        query = input("\nUsuário: ")
        if query.lower() in ["sair", "exit", "quit"]:
            break

        docs = retriever.get_relevant_documents(query)
        context = "\n".join([doc.page_content for doc in docs[:3]])

        prompt = f"""
[CONTEXTO]
{context}

[PERGUNTA]
{query}

[RESPOSTA]
"""

        resposta = run_llama_cli(prompt)
        print("\nChatbot:", resposta)

