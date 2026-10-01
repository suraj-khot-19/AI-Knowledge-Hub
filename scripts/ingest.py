'''
PDF → Pages → Chunks → Embeddings → FAISS Index
'''


from app.service.vector_store import create_vector_store
from langchain_text_splitters import RecursiveCharacterTextSplitter

from app.service.loader import load_pdf

docs = load_pdf("data/documents/guide.pdf")

splitter = RecursiveCharacterTextSplitter(
 chunk_size=800,
 chunk_overlap=120
)

chunks = splitter.split_documents(docs)
print(f"Loaded {len(docs)} pages")
print(f"Created {len(chunks)} chunks")
create_vector_store(chunks)
print("FAISS index created.")

'''
guide.pdf
   ↓
loader.py
   ↓
29 pages
   ↓
ingest.py
   ↓
64 chunks
   ↓
vector_store.py
   ↓
Embeddings (384 dimensions)
   ↓
FAISS Index
   ↓
Ready for Retrieval

It creates two file:
index.faiss = Where are the relevant vectors? 🔍(Stores the actual vector data and FAISS search index.)
index.pkl = What document/chunk does that vector belong to? 📄(Stores the mapping/metadata associated with those vectors, including the LangChain document information)

Together:
index.faiss + index.pkl = Your LangChain FAISS vector store.
'''