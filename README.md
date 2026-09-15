# DataSync AI – RAG Policy Assistant

DataSync AI is a document intelligence system built using **Retrieval-Augmented Generation (RAG)** to answer questions from an employee policy handbook. The system retrieves relevant information from the document using semantic search and provides grounded responses using Google's Gemini API.

## Internship Task 3 – RAG System

This project was developed as part of the **Generative AI Internship at Valentius Kryptix**.

## Objective

Build a RAG system that can process a real document, split it into meaningful chunks, generate embeddings, store them in a vector database, retrieve relevant information, and use the retrieved context to generate grounded answers.

## RAG Pipeline

```text
PDF Document
     ↓
Text Extraction
     ↓
Text Chunking
     ↓
Gemini Embeddings
     ↓
ChromaDB
     ↓
Semantic Retrieval
     ↓
Relevant Context
     ↓
Gemini LLM
     ↓
Grounded Answer

Technologies Used
Python
Flask
Google Gemini API
Gemini Embeddings (gemini-embedding-001)
ChromaDB
PyPDF
python-dotenv
HTML
CSS
JavaScript
Key Features
PDF document processing
Overlapping text chunking
Semantic embeddings
Local ChromaDB vector storage
Top-3 relevant document retrieval
Context injection into the LLM prompt
Grounded answers based on retrieved content
Flask-based web interface
Protection against unsupported or invented answers
Example
Question

How much is the internet reimbursement?

RAG Answer

The internet reimbursement is ₹1,200 per month.

The answer is generated using relevant information retrieved from the policy handbook.

RAG vs Without RAG
Without RAG
Question → Gemini → Answer

The model receives only the question and does not have access to the policy handbook.

With RAG
Question → Embedding → ChromaDB → Relevant Chunks → Gemini → Grounded Answer

RAG provides the model with relevant document context, making it suitable for answering questions about private or domain-specific information.

A separate test_without_rag.py script was created for comparison. The live Without-RAG test could not be completed during final testing because the Gemini free-tier generation quota was temporarily exhausted (429 RESOURCE_EXHAUSTED).

Project Structure
RAG/
├── documents/
│   └── test.pdf
├── chromadb/
├── src/
│   ├── __init__.py
│   ├── document_loader.py
│   ├── vector_store.py
│   ├── retriever.py
│   └── rag_pipeline.py
├── templates/
│   └── index.html
├── chunker.py
├── app.py
├── test_without_rag.py
├── test_gemini.py
├── requirements.txt
├── .env
├── .gitignore
└── README.md
How to Run
1. Install Dependencies
pip install -r requirements.txt
2. Configure Gemini API

Create a .env file in the project root:

GEMINI_API_KEY=your_api_key_here
3. Run the Application
python app.py
4. Open the Application
http://127.0.0.1:5000
Security

The Gemini API key is stored in an environment variable and should never be committed to GitHub.

The following files and folders should be excluded using .gitignore:

venv/
.env
chromadb/
__pycache__/
*.pyc
Learning Outcome

This task provided practical experience with:

RAG architecture
Document processing
PDF text extraction
Text chunking
Embeddings
Vector databases
Semantic retrieval
Context injection
Prompt grounding
Gemini API integration
Flask-based AI applications
Internship

Role: Generative AI Intern
Organization: Valentius Kryptix
Task: Task 3 – RAG System
