import faiss
import numpy as np


class VectorStore:
    def __init__(self, dim):
        self.index = faiss.IndexFlatL2(dim)
        self.texts = []
        self.metadata = []

    def add(self, embeddings, texts, metadata):
        if len(texts) == 0:
            return

        self.index.add(embeddings)
        self.texts.extend(texts)
        self.metadata.extend(metadata)

    def search(self, query_embedding, k=5):
        if len(self.metadata) == 0:
            return []

        D, I = self.index.search(query_embedding, k)
        results = []

        for idx in I[0]:
            results.append({"text": self.texts[idx], "metadata": self.metadata[idx]})

        return results
