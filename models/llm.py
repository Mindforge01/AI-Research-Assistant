from openai import OpenAI
from app.config import OPENAI_API_KEY, LLM_MODEL

client = OpenAI(api_key=OPENAI_API_KEY)


def generate_answer(context, question):
    prompt = f"""
You are an AI research assistant.
Use only the context below to answer.

Context:
{context}

Question:
{question}

Answer clearly and cite sources like [1], [2].
"""

    response = client.chat.completions.create(
        model=LLM_MODEL, messages=[{"role": "user", "content": prompt}], temperature=0.2
    )

    return response.choices[0].message.content
