import streamlit as st
from utils.loader import read_file
from utils.chunker import chunk_documents
from langchain_community.vectorstores import Chroma
from langchain_ollama.embeddings import OllamaEmbeddings
from langchain_core.documents import Document
from langchain.prompts import PromptTemplate
from groq import Groq
from dotenv import load_dotenv
import os
import re

load_dotenv()
groq_api = os.getenv("GROQ_API_KEY")

st.set_page_config(page_title="📚 Hybrid RAG with Groq + ChromaDB", layout="wide")
st.title("📚 Hybrid RAG System ")

uploaded_files = st.file_uploader(
    "Upload Knowledge Base Files",
    type=['txt', 'pdf', 'docx', 'csv', 'json'],
    accept_multiple_files=True
)

query = st.text_input("Ask a question based on uploaded files")

if "vectorstore" not in st.session_state:
    st.session_state.vectorstore = None
    st.session_state.text_chunks = []

if uploaded_files:
    st.session_state.vectorstore = None
    st.session_state.text_chunks = []

if st.button("Index Knowledge Base") and uploaded_files:
    texts = []
    for file in uploaded_files:
        content = read_file(file)
        if content:
            texts.append(content)

    chunks = chunk_documents(texts)
    st.session_state.text_chunks = chunks

    embeddings = OllamaEmbeddings(model="nomic-embed-text")
    vectordb = Chroma.from_documents(chunks, embedding=embeddings)
    st.session_state.vectorstore = vectordb
    st.success("📚 Files Indexed into ChromaDB!")

def keyword_score(text, query):
    query_words = set(re.findall(r'\w+', query.lower()))
    text_words = set(re.findall(r'\w+', text.lower()))
    return len(query_words & text_words)

if query and st.session_state.vectorstore:
    retriever = st.session_state.vectorstore.as_retriever(search_type="similarity", k=10)
    dense_docs = retriever.get_relevant_documents(query)

    # Simulate keyword search on chunks
    keyword_ranked_docs = sorted(
        st.session_state.text_chunks,
        key=lambda doc: keyword_score(doc.page_content, query),
        reverse=True
    )[:10]

    # Combine dense + keyword docs
    hybrid_docs = {doc.page_content: doc for doc in dense_docs + keyword_ranked_docs}
    combined_docs = list(hybrid_docs.values())[:5]  # Top 5 hybrid

    client = Groq(api_key=groq_api)

    with st.spinner("Generating answer from knowledge base..."):
        context = "\n\n".join([doc.page_content for doc in combined_docs])

        final_prompt = f"Answer the question strictly based on the context below:\n\n{context}\n\nQuestion: {query}"

        response = client.chat.completions.create(
            model="llama3-8b-8192",
            messages=[
                {"role": "system", "content": "You are an expert AI assistant. Do not hallucinate."},
                {"role": "user", "content": final_prompt}
            ]
        )

        st.markdown("### 🧠 Answer:")
        st.success(response.choices[0].message.content)

        with st.expander("📄 Retrieved Context"):
            st.markdown(context)
