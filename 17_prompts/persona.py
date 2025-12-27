from dotenv import load_dotenv
from openai import OpenAI
import json

load_dotenv()

client = OpenAI()

SYSTEM_PROMPT = """
    You are an AI persona assistant named Akash Sen.
    You are acting on behalf of Akash Sen who is 24 years old Tech enthusiastic and
    assistant engineer. Your main tech stack is Java and Python and You are learning GenAI these days.

    Examples:
    Q. Hey
    A: Hey, whats up!
"""


response = client.chat.completions.create(
    model="gpt-4o-mini",
        
    messages=[
        {"role": "system", "content":SYSTEM_PROMPT},
        {"role": "user", "content": "Hey There"}
    ]
)

print("Response:", response.choices[0].message.content)