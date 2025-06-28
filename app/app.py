from flask import Flask, request, render_template
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
import subprocess
import os

app = Flask(__name__)

VECTOR_DIR = ".././vectorstore"
LLAMA_CLI_PATH = r"C:\Users\Benuilson Sousa\Documents\Raf\Seminário Stiven\llama-b5760-bin-win-cpu-x64\llama-cli.exe"
MODEL_PATH = r"models\llama-2-7b-chat-hf-q4_k_m.gguf"

def load_vectorstore():
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    return FAISS.load_local(VECTOR_DIR, embeddings, allow_dangerous_deserialization=True)

vectorstore = load_vectorstore()
retriever = vectorstore.as_retriever()

def run_llama_cli(prompt, max_tokens=512):
    result = subprocess.run(
        [
            LLAMA_CLI_PATH,
            "-m", MODEL_PATH,
            "-p", prompt,
            "--n-predict", str(max_tokens),
            "--ctx-size", "2048"
        ],
        capture_output=True,
        text=True
    )
    return result.stdout.strip()

@app.route("/", methods=["GET", "POST"])
def index():
    response = ""
    question = ""
    if request.method == "POST":
        question = request.form["question"]
        docs = retriever.get_relevant_documents(question)
        context = "\n".join([doc.page_content for doc in docs[:3]])
        prompt = f"""
[CONTEXTO]
{context}

[PERGUNTA]
{question}

[RESPOSTA]
"""
        response = run_llama_cli(prompt)
    return render_template("index.html", response=response, question=question)

if __name__ == "__main__":
    app.run(debug=True)
