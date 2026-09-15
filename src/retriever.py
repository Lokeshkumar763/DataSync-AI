import os
import chromadb

from dotenv import load_dotenv
from google import genai
from google.genai import types


load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY not found in .env")


client = genai.Client(api_key=api_key)

chroma_client = chromadb.PersistentClient(path="chromadb")

collection = chroma_client.get_collection(
    name="datasync_handbook"
)


def create_query_embedding(query):
    """Create an embedding for the user's question."""

    result = client.models.embed_content(
        model="gemini-embedding-001",
        contents=query,
        config=types.EmbedContentConfig(
            task_type="RETRIEVAL_QUERY"
        )
    )

    return result.embeddings[0].values


def retrieve_documents(query, n_results=3):
    """Retrieve the most relevant document chunks."""

    query_embedding = create_query_embedding(query)

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=n_results
    )

    return results["documents"][0]


if __name__ == "__main__":

    question = "How many days per week can employees work remotely after probation?"

    print(f"Question: {question}\n")

    documents = retrieve_documents(question)

    print("Retrieved Documents:\n")

    for i, document in enumerate(documents, start=1):
        print(f"--- Result {i} ---")
        print(document)
        print()