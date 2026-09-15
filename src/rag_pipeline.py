import os
import time
import chromadb

from dotenv import load_dotenv
from google import genai
from google.genai import types


# Load environment variables
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY not found in .env")


# Create Gemini client
client = genai.Client(api_key=api_key)


# Connect to existing ChromaDB
chroma_client = chromadb.PersistentClient(
    path="chromadb"
)

collection = chroma_client.get_or_create_collection(
    name="datasync_handbook"
)


def create_query_embedding(question):
    """Create an embedding for the user's question."""

    result = client.models.embed_content(
        model="gemini-embedding-001",
        contents=question,
        config=types.EmbedContentConfig(
            task_type="RETRIEVAL_QUERY"
        )
    )

    return result.embeddings[0].values


def retrieve_documents(question, n_results=3):
    """Retrieve the most relevant document chunks."""

    query_embedding = create_query_embedding(question)

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=n_results
    )

    return results["documents"][0]


def generate_answer_with_retry(prompt):
    """
    Generate an answer using Gemini.

    If Gemini temporarily returns a 503 error,
    retry up to two additional times.
    """

    for attempt in range(3):

        try:
            response = client.models.generate_content(
                model="gemini-3.5-flash",
                contents=prompt
            )

            return response.text.strip()

        except Exception as e:

            # Retry only for temporary 503 errors
            if "503" in str(e) and attempt < 2:

                print(
                    f"Gemini temporarily unavailable. "
                    f"Retrying ({attempt + 1}/2)..."
                )

                time.sleep(5)

            else:
                # If it is another error, or all retries failed,
                # send the error back to Flask
                raise


def answer_question(question):
    """Retrieve relevant context and generate a grounded answer."""

    print(f"Question: {question}")
    print("Searching policy handbook...")

    # Step 1: Retrieve relevant document chunks
    documents = retrieve_documents(question)

    print(
        f"Retrieved {len(documents)} relevant documents."
    )

    # Step 2: Combine retrieved chunks into context
    context = "\n\n".join(documents)

    # Step 3: Create grounded prompt
    prompt = f"""
You are a helpful assistant for the DataSync Technologies
Employee & Technology Policy Handbook.

Answer the user's question using ONLY the information provided
in the context below.

If the answer cannot be found in the context, say:
"I could not find this information in the policy handbook."

Do not invent or assume information.

Context:
{context}

Question:
{question}

Answer clearly and concisely.
"""

    # Step 4: Generate answer using Gemini
    answer = generate_answer_with_retry(prompt)

    return answer


# Allow direct testing from the terminal
if __name__ == "__main__":

    question = input("Question: ")

    answer = answer_question(question)

    print("\n--- RAG Answer ---")
    print(answer)