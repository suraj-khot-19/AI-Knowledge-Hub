'''
This code reads/loads the PDF and extracts its content

PDF
 ↓
1. Load PDF
 ↓
2. Split text into chunks
 ↓
3. Convert text/query into vectors
'''
from langchain_text_splitters import RecursiveCharacterTextSplitter
from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader
from langchain_huggingface import HuggingFaceEmbeddings


def load_pdf(file_path: str):
 loader = PyPDFLoader(file_path)
 return loader.load()


if __name__ == "__main__":
 docs = load_pdf("data/documents/guide.pdf")
 print("Pages:", len(docs))
 print(docs[0].page_content[:500])
 print(docs[0].metadata)


splitter = RecursiveCharacterTextSplitter(
 chunk_size=800,
 chunk_overlap=120,
 separators=["\n\n", "\n", ". ", " ", ""]
)
chunks = splitter.split_documents(docs)
print("Pages:", len(docs))
print("Chunks:", len(chunks))
print(chunks[0].page_content)


embeddings = HuggingFaceEmbeddings(
 model_name="sentence-transformers/all-MiniLM-L6-v2"
)
vector = embeddings.embed_query(
 "How does the system handle authentication?"
)
print("Vector dimensions:", len(vector))
