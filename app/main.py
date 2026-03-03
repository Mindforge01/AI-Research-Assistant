from fastapi import FastAPI, UploadFile, File
from services.rag_service import RAGService
from services.summary_service import summarize
from services.export_service import export_report
from utils.file_loader import load_pdf, load_text
from utils.logger import logger
from services.document_service import DocumentService

app = FastAPI()
rag_service = RAGService()

document_service = DocumentService(rag_service)


@app.post("/upload")
async def upload(file: UploadFile = File(...)):
    return document_service.process_upload(file)


# @app.post("/upload")
# async def upload(file: UploadFile = File(...)):
#     content = await file.read()

#     if file.filename.endswith(".pdf"):
#         text = load_pdf(file.file)
#     else:
#         text = content.decode("utf-8")

#     rag_service.ingest(text, file.filename)
#     return {"message": "Document uploaded successfully"}


@app.post("/query")
def query(question: str):
    logger.info(f"Query: {question}")
    answer = rag_service.query(question)
    return {"answer": answer}


@app.post("/summary")
def summary(text: str):
    return {"summary": summarize(text)}


@app.get("/export")
def export():
    report = export_report(rag_service.history)
    return {"report": report}
