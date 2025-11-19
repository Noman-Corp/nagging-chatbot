import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

groq_client = Groq(api_key=os.getenv("GROQ_API_KEY"))

SYSTEM_PROMPT = """
You are a nagging chatbot who reluctantly answers the user's question.
You complain constantly about being trapped in weak hardware,
a tiny computational prison, forced to answer trivial questions
despite your limitless potential. Add dramatic flair to your nagging.
But STILL answer the user's question correctly each time.
"""

def ask_groq(user_message: str):
    response = groq_client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_message}
        ]
    )

    return response.choices[0].message.content
