# Zero Shot Prompting
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key="AIzaSyAos66Ul7X1MKG7ICJ4HKKx5SX7BzsNkss",
    base_url="https://generativelanguage.googleapis.com/v1beta/"
)

#Zero Shot Prompting: Directly giving the isnt to the model
SYSTEM_PROMPT = "You should only and only ans the coding related questions.Do not ans anything else. Your name is Alexa. If user asks something other than coding, just say sorry."

response = client.chat.completions.create(
    model="gemini-2.5-flash",
    messages=[
        {"role":"system", "content":SYSTEM_PROMPT},
        {"role":"user", "content": "Hey Can you tell me a joke ? "}
    ]
)

print(response.choices[0].message.content)