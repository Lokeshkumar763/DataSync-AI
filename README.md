# DataSync AI – Document Intelligence System!

DataSync AI is a document intelligence system built using **Retrieval-Augmented Generation (RAG)** to answer questions from an employee policy handbook. The system retrieves relevant information from the document using semantic search and provides grounded responses using Google's Gemini API.

## TOPIC : Retrieval-Augmented Generation (RAG)

This project was developed as part of the **Generative AI Internship at Valentius Kryptix**.

## OBJECTIVE

Build a RAG system that can process a real document, split it into meaningful chunks, generate embeddings, store them in a vector database, retrieve relevant information, and use the retrieved context to generate grounded answers.

## WORKFLOW

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

## TECHNICAL STACK:

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

## KEY FEATURES:

PDF document processing
Overlapping text chunking
Semantic embeddings
Local ChromaDB vector storage
Top-3 relevant document retrieval
Context injection into the LLM prompt
Grounded answers based on retrieved content
Flask-based web interface
Protection against unsupported or invented answers

## EXAMPLE QUESTIONS:

How much is the internet reimbursement?

RAG Answer;

The internet reimbursement is ₹1,200 per month.

The answer is generated using relevant information retrieved from the policy handbook rather than relying only on the model's general knowledge.

## RAG vs WITHOUT RAG:

• Without RAG;

Question
   ↓
Gemini
   ↓
Answer

Without RAG, the model receives only the user's question and does not have access to the policy handbook.

• With RAG;

Question
   ↓
Query Embedding
   ↓
ChromaDB
   ↓
Relevant Chunks
   ↓
Gemini
   ↓
Grounded Answer

With RAG, relevant document content is retrieved and provided to the model as context. This allows the system to answer questions using private or domain-specific information contained in the document.

A separate test_without_rag.py script is included in the repository for comparison.

During final testing, the live Without-RAG generation request could not be completed because the Gemini API free-tier generation quota was temporarily exhausted (429 RESOURCE_EXHAUSTED). The RAG pipeline itself was successfully tested with grounded document-based answers.

## PROJECT STRUCTURE:

DataSync-AI/
├── documents/
│   └── test.pdf
├── src/
│   ├── __init__.py
│   ├── document_loader.py
│   ├── vector_store.py
│   ├── retriever.py
│   └── rag_pipeline.py
├── templates/
│   └── index.html
├── app.py
├── test_without_rag.py
├── requirements.txt
├── .gitignore
└── README.md
Excluded from Git

The following local files and folders are intentionally excluded from the public repository:

venv/
.env
chromadb/
__pycache__/
*.pyc

chromadb/ contains the locally generated vector database and can be recreated from the document processing pipeline.

How to Run
1. Clone the Repository
git clone https://github.com/Lokeshkumar763/DataSync-AI.git
cd DataSync-AI
2. Create and Activate a Virtual Environment
python -m venv venv

## WINDOWS POWERSHELL:

venv\Scripts\Activate.ps1
3. Install Dependencies
pip install -r requirements.txt
4. Configure Gemini API

Create a .env file in the project root:

GEMINI_API_KEY=your_api_key_here

Never commit the API key to GitHub.

5. Run the Application
python app.py
6. Open the Application
http://127.0.0.1:5000
Security

The Gemini API key is stored in an environment variable and should never be committed to GitHub.

The following are excluded using .gitignore:

venv/
.env
chromadb/
__pycache__/
*.pyc
Learning Outcome

## GAINED EXPERIENCE:

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

## ABOUT
Role: Generative AI Intern
Organization: Valentius Kryptix
Topic: RAG System
