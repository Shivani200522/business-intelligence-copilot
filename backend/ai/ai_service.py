import os

from dotenv import load_dotenv
from google import genai

load_dotenv()


class AIService:

    def __init__(self):
        api_key = os.getenv("GEMINI_API_KEY")

        self.client = genai.Client(
            api_key=api_key
        )

    def generate_sql(
        self,
        question: str,
        table_name: str,
        schema: list,
    ):

        prompt = f"""
    You are a PostgreSQL SQL generator.

    CRITICAL RULES:
    - ALWAYS wrap table name and column names in double quotes ""
    - PostgreSQL is CASE-SENSITIVE
    - Never use lowercase column names
    - Use ONLY provided schema columns

    Table Name:
    "{table_name}"

    Columns:
    {", ".join([f'"{col}"' for col in schema])}

    User Question:
    {question}

    Return ONLY SQL.
    No explanation.
    No markdown.
    """

        response = self.client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
        )

        return response.text.strip()