import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def query_model(context: str, question: str) -> str:
    try:
        model = genai.GenerativeModel("gemini-2.0-flash")

        # Combine context and question into a single user message
        user_input = f"You are a helpful assistant. Use the context below to answer the question.\n\nContext:\n{context}\n\nQuestion: {question}"

        print(f"🟡 Sending to Gemini:\n{user_input[:500]}...")

        response = model.generate_content(user_input)

        print("🟢 Gemini response:", response.text)
        return response.text
    except Exception as e:
        print("🔴 Gemini error:", e)
        return f"Gemini error: {e}"
