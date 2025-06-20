# 🤖 Hybrid-RAG-Assistant

A powerful document-based chatbot built using **Hybrid Retrieval-Augmented Generation (RAG)** combining **semantic similarity search (ChromaDB + Ollama Embeddings)** with **keyword matching**, and powered by **Groq’s LLaMA 3** for generating accurate, grounded answers.

---

## 🚀 Features

- 📄 **Supports multi-format knowledge ingestion**: `.txt`, `.pdf`, `.csv`, `.docx`, `.json`
- 🔍 **Hybrid search strategy**: Combines semantic + keyword-based document retrieval
- 🧠 **Groq LLM integration**: Fast, accurate answers using `llama3-8b-8192`
- 🧱 **ChromaDB + Ollama Embeddings**: Local vector database for fast retrieval
- 🐳 **Dockerized for production**: Run anywhere with one command
- 📚 **Built with Streamlit**: Simple, intuitive web interface

---

## 🛠️ Setup Instructions (Without Docker)

### 1. Clone the repo

```bash
git clone https://github.com/your-username/Hybrid-RAG-Assistant.git
cd Hybrid-RAG-Assistant
```

### 2. Create a virtual environment and activate it

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set up your environment variables

Create a `.env` file in the root directory:

```env
GROQ_API_KEY=your_groq_api_key_here
```

---

## 🧪 Run the App Locally

```bash
streamlit run main.py
```

Visit [http://localhost:8501](http://localhost:8501) in your browser.

---

## 🐳 Docker Setup (Recommended)

### 1. Build Docker image

```bash
docker build -t hybrid-rag-app .
```

### 2. Run the container

```bash
docker run -p 8501:8501 -e GROQ_API_KEY=your_groq_api_key_here hybrid-rag-app
```

> ⚠️ Ensure Ollama is running on the host system and `nomic-embed-text` model is available.
> You can start it with:
```bash
ollama run nomic-embed-text
```

If you’re on Linux, you can run the container with host networking:

```bash
docker run --network=host -e GROQ_API_KEY=your_groq_api_key_here hybrid-rag-app
```

---

## 📂 File Structure

```bash
Hybrid-RAG-Assistant/
├── main.py                      # Main Streamlit app
├── Dockerfile                   # Dockerfile to containerize the app
├── .env                         # Env variables (GROQ API)
├── requirements.txt             # Python dependencies
├── utils/
│   ├── loader.py                # File loader utilities
│   └── chunker.py               # Document chunking logic
└── README.md
```

---

## 💡 How It Works

1. **Upload Files** → `.txt`, `.pdf`, `.docx`, `.csv`, `.json`
2. **Indexing** → Files are chunked and embedded using Ollama's `nomic-embed-text`
3. **Hybrid Retrieval** → 
   - Dense vector similarity via ChromaDB
   - Keyword overlap scoring
4. **Answer Generation** → Groq's `llama3-8b-8192` model answers based strictly on the top retrieved content

---

## 🧠 Requirements

- Python 3.10+
- [Groq API Key](https://console.groq.com/keys)
- [Ollama](https://ollama.com/) running with `nomic-embed-text` model pulled
- Docker (for containerized deployment)

---

## 📝 License

MIT License — free to use, modify and share with attribution.

---

## 🙏 Acknowledgements

- [Groq](https://groq.com/)
- [Ollama](https://ollama.com/)
- [LangChain](https://www.langchain.com/)
- [ChromaDB](https://www.trychroma.com/)
- [Streamlit](https://streamlit.io/)

---

## ✨ Demo Preview

![screenshot](demo.png)
