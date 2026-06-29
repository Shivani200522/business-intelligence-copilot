import os
from dotenv import load_dotenv
from google import genai

load_dotenv()


class SummaryService:

    def __init__(self):
        self.client = genai.Client(
            api_key=os.getenv("GEMINI_API_KEY")
        )

    def generate_summary(self, data, insights):

        prompt = f"""
You are a Business Intelligence Analyst.

Dataset Result:
{data}

Insights:
{insights}

Write:
1. Executive Summary (3-5 lines)
2. Business Recommendations (3 bullet points)

Keep it professional.
"""

        response = self.client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        return response.text