from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key="AIzaSyAos66Ul7X1MKG7ICJ4HKKx5SX7BzsNkss",
    base_url="https://generativelanguage.googleapis.com/v1beta/"
)

response = client.chat.completions.create(
    model="gemini-2.5-flash",
    messages=[
        {"role":"system", "content":"you are an expert in maths and only and only ans math related questions. That if the query is not related to maths then just say sorry."},
        {"role":"user", "content": "Hey There! Can you solve the a + b whole square formula"}
    ]
)

print(response.choices[0].message.content)