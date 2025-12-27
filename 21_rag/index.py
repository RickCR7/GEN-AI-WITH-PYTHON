from dotenv import load_dotenv
from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.document_loaders import UnstructuredPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_qdrant import QdrantVectorStore

load_dotenv()

pdf_path = Path(__file__).parent / "English.pdf"

# Load this file in python program
loader = UnstructuredPDFLoader(file_path=pdf_path, mode="elements")
docs = loader.load()

print("Total pages loaded:", len(docs))

# Split the docs into smaller chunks
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size = 1000,
    chunk_overlap = 200,
) 

chunks = text_splitter.split_documents(documents=docs)

print("Total chunks:", len(chunks))
print("Distinct page numbers in chunks:",
      sorted({c.metadata.get("page") for c in chunks}))

# Vector Embeddings 
embedding_model = OpenAIEmbeddings(
    model="text-embedding-3-large"
)

vector_store = QdrantVectorStore.from_documents(
    documents=chunks,
    embedding=embedding_model,
    url="http://localhost:6333",
    collection_name="learning_rag"
)

print("Indexing of documents done...")