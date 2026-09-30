from google import genai
from dotenv import load_dotenv
import os
import asyncio

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")
MODEL = os.getenv("GEMINI_MODEL", "gemini-3.8-flash")

if not API_KEY:
    raise ValueError("GEMINI_API_KEY is missing from .env")

client = genai.Client(api_key=API_KEY)


async def generate_planner_recommendation(
    planner: str,
    details: str,
    budget: float = 0
):
    prompt = f"""
You are PocketSmart AI, an AI-powered budget planning assistant.

Planner:
{planner}

User Budget:
₹{budget}

User Requirements:
{details}

Create a practical recommendation that stays within the user's budget.

Include:

1. Recommended plan
2. Estimated budget breakdown
3. Recommended items or services
4. Useful suggestions
5. Ways to save money

Keep the response clear, practical and easy to understand.

Do not recommend financial products or investments.
"""

    max_retries = 3

    for attempt in range(max_retries):

        try:

            print(
                f"Gemini request attempt {attempt + 1}/{max_retries}"
            )

            response = await client.aio.models.generate_content(
                model=MODEL,
                contents=prompt
            )

            return response.text

        except Exception as e:

            error_text = str(e)

            print("GEMINI ERROR:", error_text)

            if "503" not in error_text:
                raise

            if attempt < max_retries - 1:

                wait_time = 5 * (2 ** attempt)

                print(
                    f"Gemini temporarily unavailable. "
                    f"Retrying in {wait_time} seconds..."
                )

                await asyncio.sleep(wait_time)

            else:

                raise Exception(
                    "Gemini is temporarily unavailable after "
                    "multiple attempts. Please try again later."
                )