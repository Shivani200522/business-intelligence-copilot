from backend.ai.gemini_client import model


def generate_sql(
    schema: str,
    question: str
):

    prompt = f"""
You are an expert SQL analyst.

Convert the user's question into PostgreSQL SQL.

Rules:
- Return ONLY SQL.
- No explanation.
- No markdown.
- No code blocks.
- Use PostgreSQL syntax.

Schema:

{schema}

Question:

{question}
"""

    response = model.generate_content(
        prompt
    )

    return response.text.strip()