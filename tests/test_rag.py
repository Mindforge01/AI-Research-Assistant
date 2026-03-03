import unittest
from services.rag_service import RAGService


class TestRAGService(unittest.TestCase):

    def setUp(self):
        self.rag = RAGService()
        sample_text = """
        Artificial Intelligence is the simulation of human intelligence processes by machines.
        Machine Learning is a subset of AI.
        Deep Learning is a subset of Machine Learning.
        """
        self.rag.ingest(sample_text, "test_doc")

    def test_ingest(self):
        self.assertIsNotNone(self.rag.vector_store)
        self.assertTrue(len(self.rag.vector_store.texts) > 0)

    def test_query(self):
        answer = self.rag.query("What is Machine Learning?")
        self.assertIsInstance(answer, str)
        self.assertTrue(len(answer) > 0)

    def test_memory(self):
        self.rag.query("What is AI?")
        self.assertEqual(len(self.rag.history), 1)


if __name__ == "__main__":
    unittest.main()
