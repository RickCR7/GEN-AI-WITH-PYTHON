from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings
from langchain_qdrant import QdrantVectorStore
from openai import OpenAI

load_dotenv()

client = OpenAI()

# Vector Embeddings 
embedding_model = OpenAIEmbeddings(
    model="text-embedding-3-large"
)

# Connection
vector_Db = QdrantVectorStore.from_existing_collection(
    url="http://localhost:6333",
    collection_name="learning_rag",
    embedding=embedding_model
)

# Take the user input
user_query = input("Ask Something: ")

# Relevant chunks from the vector DB
search_results = vector_Db.similarity_search(query=user_query, k=8)

context = "\n\n\n".join(
    [
        f"Page content: {result.page_content}\n"
        f"Page Number: {result.metadata.get('page_number', 'Unknown')}\n"
        f"File Location: {result.metadata.get('source', 'Unknown')}"
        for result in search_results
    ]
)


SYSTEM_PROMPT = f"""
    You are a helpful AI assistant who answers user query based on the available context retrieved from a PDF file along with page contents and page number.

    You should only answer the user based on the following context and navigate the user to open the right page number to know more.

    Context: {context}
"""

response = client.chat.completions.create(
    model="gpt-5.1",
    messages=[
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content":user_query},
    ]
)

print(f"🤖: {response.choices[0].message.content}")