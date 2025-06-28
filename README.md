# 🧠 Chatbot RAG sobre Phishing em Cibersegurança

Este projeto implementa um chatbot baseado em **RAG (Retrieval-Augmented Generation)** utilizando um modelo LLM local (**LLaMA 2**) via `llama.cpp`, com interface web em Flask. O sistema responde exclusivamente com base em documentos sobre **phishing**, sem qualquer fallback genérico do modelo.

---

# RAG (Retrieval-Augmented Generation)

RAG é uma técnica que combina geração de texto com recuperação de informação. Em vez de depender apenas da memória do modelo, ele busca informações em documentos externos relevantes para responder uma pergunta. O pipeline básico é:
•	Consulta → Recuperação de documentos relevantes → Geração com base nos documentos.

---


# Tema: Phishing em cibersegurança

A escolha do tema Phishing em Cibersegurança justifica-se pela sua elevada relevância prática, uma vez que o phishing continua a ser uma das ameaças mais recorrentes no cenário de segurança digital. Trata-se de um domínio rico em conteúdo informativo, como artigos técnicos, relatórios de incidentes, manuais de prevenção e diretrizes institucionais. A técnica de RAG (Retrieval-Augmented Generation) encaixa-se perfeitamente nesse contexto, pois permite que o chatbot gere respostas fundamentadas exclusivamente em documentos atualizados — como relatórios de ameaças recentes ou orientações oficiais —, dispensando o re-treinamento do modelo sempre que novas informações são integradas.

Entre os exemplos de aplicação deste chatbot, destacam-se perguntas como:
•	“Como identificar um e-mail de phishing?”
•	“Qual é a diferença entre spear phishing e whaling?”
•	“Como configurar SPF e DKIM para mitigar phishing?”
•	“Casos de phishing em Portugal nos últimos anos?”
Esses casos demonstram o valor da abordagem RAG na resposta precisa e confiável sobre tópicos críticos da cibersegurança.

---

## 🎯 Objetivo

Construir um sistema funcional, leve e privado para responder a perguntas sobre phishing em cibersegurança, usando documentos reais e tecnologia RAG, ideal para projetos acadêmicos ou protótipos em ambientes controlados.

---

## ⚙️ Tecnologias Utilizadas

- `LangChain`
- `llama.cpp` (binário Windows)
- `Flask` (interface web)
- `FAISS` (armazenamento vetorial local)
- `HuggingFaceEmbeddings` (MiniLM)

---

## 🗂️ Estrutura do Projeto

```plaintext
chatbot-rag/
├── app/                  # Interface web Flask
│   ├── app.py
│   └── templates/
│       └── index.html
├── data/                 # Arquivos .txt sobre phishing
├── models/               # Modelo LLaMA .gguf
├── scripts/              # Scripts auxiliares (chunks, vetores, chatbot)
│   ├── chunk_texts.py
│   ├── generate_vectorstore.py
│   └── chatbot.py
├── vectorstore/          # Armazenamento FAISS
└── README.md
```

---

## 🔧 Instalação

1. **Pré-requisitos**:
   - Windows 10
   - Python 3.10+
   - `llama.cpp` binário (ex: `llama-b5760-bin-win-cpu-x64.zip`)

2. **Ambiente virtual**:
   ```cmd
   python -m venv ragenv
   ragenv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Modelo**:
   - Baixe `.gguf` de [TheBloke/Llama-2-7B-Chat-GGUF](https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGUF)
   - Coloque em `models/`

4. **Documentos**:
   - Arquivos `.txt` sobre phishing em `data/`

---

## 🧩 Execução

### 🔹 Gerar Chunks
```cmd
python scripts\chunk_texts.py
```

### 🔹 Criar Vetor FAISS
```cmd
python scripts\generate_vectorstore.py
```

### 🔹 Testar via Terminal
```cmd
python scripts\chatbot.py
```

### 🔹 Interface Web
```cmd
cd app
python app.py
```
Abra `http://127.0.0.1:5000/` no navegador.

---

## 🧠 Exemplo de Uso

> **Pergunta**: Quais os tipos de phishing mais comuns?  
> **Resposta**: Spear phishing, whaling, vishing e smishing são os principais tipos, cada um explorando diferentes meios e alvos...

---

## 🛡️ Segurança

Este projeto **não envia dados para a internet**. Toda a inferência e recuperação são locais. O modelo não gera respostas fora do escopo dos documentos.

---

## ⚠️ Limitações

- Pode não responder se os documentos não contiverem a resposta.
- Utiliza apenas 3 chunks mais relevantes.
- Modelo LLaMA roda com desempenho limitado em CPUs mais antigos.
