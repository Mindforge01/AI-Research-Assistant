from rag.chunker import chunk_text
from embeddings.embedding_model import EmbeddingModel
from rag.vector_store import VectorStore
from models.llm import generate_answer
from utils.logger import logger
import numpy as np


class RAGService:
    def __init__(self):
        self.embedder = EmbeddingModel()
        self.vector_store = None
        self.history = []

    def ingest(self, text, source_name):
        chunks = chunk_text(text)
        logger.info(f"Chunks created: {len(chunks)}")

        embeddings = self.embedder.embed(chunks)

        if self.vector_store is None:
            self.vector_store = VectorStore(embeddings.shape[1])

        metadata = [{"source": source_name} for _ in chunks]
        self.vector_store.add(embeddings, chunks, metadata)

    def query(self, question):
        if self.vector_store is None:
            return "No documents uploaded."

        query_embedding = self.embedder.embed([question])
        results = self.vector_store.search(query_embedding)

        context = ""
        for i, r in enumerate(results):
            context += f"[{i+1}] {r['text']}\n"

        answer = generate_answer(context, question)

        self.history.append({"question": question, "answer": answer})

        return answer
