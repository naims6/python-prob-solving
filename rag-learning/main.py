from pathlib import Path

import numpy as np
from sentence_transformers import SentenceTransformer

filePath = Path("data/knowledge.txt")
document = filePath.read_text(encoding="utf8")


chunks = [paragraph.strip() for paragraph in document.split("\n\n") if paragraph.strip()]


model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")


chunkEmbeddings = model.encode(chunks, normalize_embeddings=True)

print("Chunk Embedding", chunkEmbeddings)
print("Chunk Embedding shape", chunkEmbeddings.shape)


# ask a question
query = "What is rag?"
queryEmbedding = model.encode(query, normalize_embeddings=True)

print("Query Embedding", queryEmbedding)

scores = chunkEmbeddings @ queryEmbedding

print("Scores",scores)