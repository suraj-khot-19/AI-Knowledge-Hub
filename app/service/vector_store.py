''''
Chunks → Embeddings → FAISS → Save
'''

from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings

INDEX_PATH = "data/index/faiss"

def create_vector_store(chunks):
    embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
    )
    db = FAISS.from_documents(chunks, embeddings)
    db.save_local(INDEX_PATH)
    return db


def load_vector_store():
    embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
    )
    return FAISS.load_local(
    INDEX_PATH,
    embeddings,
    allow_dangerous_deserialization=True
    )
