import PyPDF2


def load_pdf(file):
    reader = PyPDF2.PdfReader(file)
    text = ""
    for page in reader.pages:
        text += page.extract_text() or ""
    return text


def load_text(file):
    return file.read().decode("utf-8")
