from sentence_transformers import SentenceTransformer
import numpy as np
from app.config import EMBEDDING_MODEL


class EmbeddingModel:
    def __init__(self):
        self.model = SentenceTransformer(EMBEDDING_MODEL)

    def embed(self, texts):
        return np.array(self.model.encode(texts))
