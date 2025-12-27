from google import genai

# The client gets the API key from the environment variable `GEMINI_API_KEY`.
client = genai.Client(
    api_key="AIzaSyAos66Ul7X1MKG7ICJ4HKKx5SX7BzsNkss"
)

response = client.models.generate_content(
    model="gemini-2.5-flash", contents="Explain how AI works in a few words"
)
print(response.text)