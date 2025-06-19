# agentic_chunker.py

from typing import List

class AgenticChunker:
    def __init__(self, max_chunk_len=5):
        self.propositions = []
        self.chunks = []
        self.max_chunk_len = max_chunk_len

    def add_propositions(self, propositions: List[str]):
        self.propositions = propositions
        self._chunkify()

    def _chunkify(self):
        for i in range(0, len(self.propositions), self.max_chunk_len):
            chunk = " ".join(self.propositions[i:i + self.max_chunk_len])
            self.chunks.append(chunk)

    def get_chunks(self, as_documents=False):
        if as_documents:
            from langchain_core.documents import Document
            return [Document(page_content=chunk, metadata={"source": "agentic"}) for chunk in self.chunks]
        return self.chunks
