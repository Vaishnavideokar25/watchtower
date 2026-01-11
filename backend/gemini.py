import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load .env file
load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise RuntimeError("GEMINI_API_KEY not found in environment variables")

genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("gemini-pro")


def analyze_change(content: str) -> dict:
    prompt = f"""
A website update was detected with the following text:

\"{content}\"

Explain:
1. Why this change matters to the user
2. What action the user should take

Respond in clear, concise sentences.
"""

    try:
        response = model.generate_content(prompt)
        text = response.text.strip()

        # Very simple parsing (safe for hackathon)
        return {
            "why": text.split("\n")[0],
            "action": text.split("\n")[-1]
        }

    except Exception as e:
        return {
            "why": "An important update was detected.",
            "action": "Please review the update manually."
        }
