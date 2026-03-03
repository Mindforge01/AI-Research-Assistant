from models.llm import generate_answer


def summarize(text):
    return generate_answer(text, "Summarize this document.")
