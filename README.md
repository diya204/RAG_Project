# Retrieval-Augmented Generation (RAG) with LangChain, ChromaDB & Gemini

## 📌 Project Overview

This project demonstrates a simple Retrieval-Augmented Generation (RAG) pipeline using LangChain, ChromaDB, Hugging Face Embeddings, and Google Gemini.

The application loads a PDF document, splits it into chunks, stores embeddings in a vector database, retrieves relevant information based on a user query, and generates an answer using Gemini AI.

---

## 🚀 Features

- PDF Document Loading
- Text Chunking
- Embedding Generation
- Vector Database Storage
- Semantic Search
- AI-Powered Question Answering
- Google Gemini Integration

---

## 🛠️ Technologies Used

- Python
- LangChain
- ChromaDB
- Hugging Face Sentence Transformers
- Google Gemini AI
- PyPDF

---

## 📂 Project Structure

```text
├── rag.py
├── requirements.txt
├── chroma_db/
└── data/
    └── Machine_Learning_RAG_Document.pdf
```

---

## ⚙️ Installation

### 1. Clone Repository

```bash
git clone https://github.com/your-username/RAG-with-LangChain.git
cd RAG-with-LangChain
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure Gemini API Key

Set your Google Gemini API Key:

```bash
export GOOGLE_API_KEY="your_api_key"
```

Windows:

```cmd
set GOOGLE_API_KEY=your_api_key
```

---

## ▶️ Run the Project

```bash
python rag.py
```

---

## 🔄 Workflow

1. Load PDF using PyPDFLoader
2. Split document into chunks
3. Generate embeddings using all-MiniLM-L6-v2
4. Store embeddings in ChromaDB
5. Perform similarity search
6. Retrieve relevant chunks
7. Send context to Gemini AI
8. Generate final answer

---

## 📊 Example Query

```text
What is Supervised Learning?
```

### Example Output

```text
Final Answer:
Supervised Learning is a machine learning approach where a model learns from labeled data to make predictions on unseen data.
```

---

## 🎯 Learning Outcomes

- Retrieval-Augmented Generation (RAG)
- Vector Databases
- Semantic Search
- Embeddings
- Prompt Engineering
- Large Language Models (LLMs)
- LangChain Framework

---

## ⭐ Future Improvements

- Streamlit Frontend
- Chat Interface
- Multiple PDF Support
- Hybrid Search
- Conversation Memory
- Advanced Retrieval Techniques
