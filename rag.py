from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
# Load PDF
loader = PyPDFLoader("data/Machine_Learning_RAG_Document.pdf")
documents = loader.load()

print(f"Pages loaded: {len(documents)}")

# Chunking
splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=100
)

chunks = splitter.split_documents(documents)

print(f"Chunks created: {len(chunks)}")

# Embeddings
embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# Vector Database
vectordb = Chroma.from_documents(
    documents=chunks,
    embedding=embedding_model,
    persist_directory="./chroma_db"
)

print("Vector DB Created Successfully!")

# Query
query = "What is Supervised Learning?"

results = vectordb.similarity_search(query, k=3)

print("\nQuestion:")
print(query)

print("\nRetrieved Chunks:\n")

for i, doc in enumerate(results, start=1):
    print(f"\nChunk {i}:")
    print(doc.page_content[:500])
    from langchain_google_genai import ChatGoogleGenerativeAI

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key="AQ.Ab8RN6JubZ25m2McACKPFbLKBVAk1iSbeF_id5pQgXQ2K13juQ"
)

context = "\n".join([doc.page_content for doc in results])

prompt = f"""
Answer the question using only the provided context.

Context:
{context}

Question:
{query}

Answer:
"""

response = llm.invoke(prompt)

print("\nFinal Answer:")
print(response.content)