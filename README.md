# DataSync AI – Document Intelligence System

**DataSync AI** is a Retrieval-Augmented Generation (RAG) based document intelligence system that allows users to ask natural-language questions about an employee policy handbook.

The system processes the document, creates semantic embeddings, stores them in a local **ChromaDB** vector database, retrieves relevant document sections, and provides context-grounded responses using **Google Gemini**.

This project was developed as part of my **Generative AI Internship at Valentius Kryptix**.

---

## Project Overview

Large Language Models can generate useful responses, but they may not have access to private or domain-specific information.

DataSync AI addresses this problem by connecting an LLM with an external document through a **Retrieval-Augmented Generation (RAG)** pipeline.

Instead of relying only on the model's general knowledge, the system retrieves relevant information from the policy handbook and provides it to the LLM as context before generating a response.

---

## RAG Architecture

The complete workflow of DataSync AI is:

```text
PDF Document
     ↓
Text Extraction
     ↓
Text Chunking
     ↓
Gemini Embeddings
     ↓
ChromaDB Vector Storage
     ↓
Semantic Retrieval
     ↓
Relevant Context
     ↓
Gemini LLM
     ↓
Grounded Answer
```

---

## Key Features

* PDF document ingestion and text extraction
* Overlapping text chunking
* Semantic embedding generation
* Local vector storage using ChromaDB
* Semantic similarity-based retrieval
* Top-3 relevant document chunk retrieval
* Context injection into the LLM prompt
* Grounded responses based on retrieved information
* Flask-based web interface
* Protection against unsupported or invented answers
* Environment-based API key configuration

---

## Technology Stack

| Technology        | Purpose                                  |
| ----------------- | ---------------------------------------- |
| Python            | Core application development             |
| Flask             | Web application and API                  |
| Google Gemini API | LLM-based response generation            |
| Gemini Embeddings | Semantic representation of document text |
| ChromaDB          | Local vector database                    |
| PyPDF             | PDF text extraction                      |
| python-dotenv     | Environment variable management          |
| HTML              | Web interface structure                  |
| CSS               | User interface styling                   |
| JavaScript        | Frontend interaction                     |

---

## Example

### User Question

> How much is the internet reimbursement?

### DataSync AI Response

> The internet reimbursement is ₹1,200 per month.

The response is generated using relevant information retrieved from the policy handbook and provided to the Gemini model as context.

This helps the system answer questions based on the information contained in the document rather than relying only on the model's general knowledge.

---

## RAG vs. Without RAG

### Without RAG

```text
User Question
      ↓
Gemini
      ↓
Answer
```

Without RAG, the model receives the user's question without retrieving information from the policy handbook.

### With RAG

```text
User Question
      ↓
Query Embedding
      ↓
ChromaDB
      ↓
Relevant Chunks
      ↓
Context
      ↓
Gemini
      ↓
Grounded Answer
```

With RAG, relevant information is retrieved from the document and provided to the LLM as context.

This allows the application to work with **private, custom, and domain-specific information**.

A separate `test_without_rag.py` script is included in the repository for comparison.

> **Testing Note:** During final testing, the live Without-RAG generation request could not be completed because the Gemini API free-tier generation quota was temporarily exhausted (`429 RESOURCE_EXHAUSTED`). The RAG pipeline itself was successfully tested and produced grounded document-based responses.

---

## Project Structure

```text
DataSync-AI/
│
├── documents/
│   └── test.pdf
│
├── src/
│   ├── __init__.py
│   ├── document_loader.py
│   ├── vector_store.py
│   ├── retriever.py
│   └── rag_pipeline.py
│
├── templates/
│   └── index.html
│
├── app.py
├── test_without_rag.py
├── requirements.txt
├── .gitignore
└── README.md
```

### Excluded from Git

The following local files and directories are intentionally excluded from the repository:

```text
venv/
.env
chromadb/
__pycache__/
*.pyc
```

The `chromadb/` directory contains the locally generated vector database and can be recreated through the document processing pipeline.

---

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/Lokeshkumar763/DataSync-AI.git
cd DataSync-AI
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

### 3. Activate the Virtual Environment

#### Windows PowerShell

```powershell
venv\Scripts\Activate.ps1
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure the Gemini API Key

Create a `.env` file in the project root:

```env
GEMINI_API_KEY=your_api_key_here
```

**Never commit your API key to GitHub.**

### 6. Run the Application

```bash
python app.py
```

### 7. Open the Application

Open the following address in your browser:

```text
http://127.0.0.1:5000
```

---

## Security

The Gemini API key is stored using an environment variable and should never be hardcoded or committed to the repository.

The `.gitignore` file excludes:

```text
.env
venv/
chromadb/
__pycache__/
*.pyc
```

---

## Learning Outcomes

Through this project, I gained practical experience in:

* Retrieval-Augmented Generation (RAG)
* Document processing and PDF text extraction
* Text chunking and overlapping chunks
* Semantic embeddings
* Vector databases
* Semantic search and retrieval
* Context injection
* Prompt grounding
* Google Gemini API integration
* Flask-based AI applications
* Building LLM-powered applications

---

## Internship Context

| Details | Information |
|---|---|
| Role | Generative AI Intern |
| Organization | Valentius Kryptix |
| Project | DataSync AI |
| Focus Area | Retrieval-Augmented Generation (RAG) |

---

## Author

**Lokeshkumar S**

B.Sc. Artificial Intelligence and Data Science Graduate

---

## Repository

[DataSync AI – GitHub Repository](https://github.com/Lokeshkumar763/DataSync-AI)
