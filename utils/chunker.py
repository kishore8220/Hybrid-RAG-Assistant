# Recurise Character Chunking   
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document

def chunk_documents(texts, chunk_size=1500, chunk_overlap=200):
    splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    docs = splitter.create_documents(texts)
    return docs

# # Semantic Chunking
# from langchain_experimental.text_splitter import SemanticChunker
# from langchain_core.documents import Document
# from langchain_ollama.embeddings import OllamaEmbeddings
# def chunk_documents_semantic(texts, embedding_model=None):
#     if embedding_model is None:
#         embedding_model = OllamaEmbeddings(model="nomic-embed-text")

#     # SemanticChunker works on list[Document], so convert your texts
#     documents = [Document(page_content=text) for text in texts]

#     # Initialize SemanticChunker
#     splitter = SemanticChunker(embeddings=embedding_model)

#     # Split the documents semantically
#     chunked_docs = splitter.split_documents(documents)

#     return chunked_docs


# from langchain.output_parsers.openai_tools import JsonOutputToolsParser
# from langchain_groq import ChatGroq
# from langchain_core.prompts import ChatPromptTemplate
# from langchain_core.runnables import RunnableLambda
# from langchain.chains import create_extraction_chain_pydantic
# from langchain_core.pydantic_v1 import BaseModel
# from typing import List
# from .agentic_chunker import AgenticChunker


# # Define pydantic schema for LLM extraction
# class Sentences(BaseModel):
#     sentences: List[str]


# def extract_propositions(text: str, llm=None) -> List[str]:
#     if llm is None:
#         llm = ChatGroq(model="llama3-8b-8192", temperature=0)

#     extraction_chain = create_extraction_chain_pydantic(
#         pydantic_schema=Sentences,
#         llm=llm
#     )

#     try:
#         extracted = extraction_chain.invoke({"input": text})
#         return extracted["text"][0].sentences
#     except Exception as e:
#         print(f"Extraction failed: {e}")
#         return []


# def chunk_documents_agentic(texts: List[str], llm=None, max_chunk_len=5, return_type="documents"):
#     if llm is None:
#         llm = ChatGroq(model="llama3-8b-8192", temperature=0)

#     all_props = []
#     for i, text in enumerate(texts):
#         props = extract_propositions(text, llm=llm)
#         all_props.extend(props)
#         print(f"✅ Extracted {len(props)} propositions from paragraph {i+1}")

#     ac = AgenticChunker(max_chunk_len=max_chunk_len)
#     ac.add_propositions(all_props)

#     if return_type == "documents":
#         return ac.get_chunks(as_documents=True)
#     return ac.get_chunks(as_documents=False)
