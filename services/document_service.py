from utils.file_loader import load_pdf, load_text
from utils.logger import logger


class DocumentService:
    def __init__(self, rag_service):
        self.rag_service = rag_service

    def process_upload(self, file):
        filename = file.filename

        if filename.endswith(".pdf"):
            text = load_pdf(file.file)
        else:
            content = file.file.read()
            text = content.decode("utf-8")

        if not text.strip():
            raise ValueError("Uploaded document is empty.")

        logger.info(f"Ingesting document: {filename}")
        self.rag_service.ingest(text, filename)

        return {"message": f"{filename} uploaded successfully"}
