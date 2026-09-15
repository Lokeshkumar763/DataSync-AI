import os
import chromadb

from dotenv import load_dotenv
from google import genai
from google.genai import types

from src.document_loader import load_pdf
from chunker import chunk_text


# Load environment variables
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY not found in .env")


# Gemini client
client = genai.Client(api_key=api_key)


# ChromaDB local database
chroma_client = chromadb.PersistentClient(path="chromadb")

collection = chroma_client.get_or_create_collection(
    name="datasync_handbook"
)


def create_embeddings(chunks):
    """Create Gemini embeddings for document chunks."""

    result = client.models.embed_content(
        model="gemini-embedding-001",
        contents=chunks,
        config=types.EmbedContentConfig(
            task_type="RETRIEVAL_DOCUMENT"
        )
    )

    return [embedding.values for embedding in result.embeddings]


def store_chunks(chunks, embeddings):
    """Store chunks and embeddings in ChromaDB."""

    ids = [f"chunk_{i}" for i in range(len(chunks))]

    collection.upsert(
        ids=ids,
        documents=chunks,
        embeddings=embeddings
    )

    print(f"Stored {len(chunks)} chunks in ChromaDB.")


if __name__ == "__main__":

    print("Loading PDF...")

    text = load_pdf("documents/test.pdf")

    print(f"Extracted characters: {len(text)}")

    print("Creating chunks...")

    chunks = chunk_text(text)

    print(f"Created {len(chunks)} chunks.")

    print("Creating Gemini embeddings...")

    embeddings = create_embeddings(chunks)

    print(f"Created {len(embeddings)} embeddings.")

    print("Storing in ChromaDB...")

    store_chunks(chunks, embeddings)

    print("\nRAG vector database created successfully!")