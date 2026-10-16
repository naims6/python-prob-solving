from pathlib import Path

import numpy as np
import os
from sentence_transformers import SentenceTransformer
from dotenv import load_dotenv
from google import genai

filePath = Path("data/knowledge.txt")
document = filePath.read_text(encoding="utf8")


chunks = [paragraph.strip() for paragraph in document.split("\n\n") if paragraph.strip()]
model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")


chunkEmbeddings = model.encode(chunks, normalize_embeddings=True)

# print("Chunk Embedding", chunkEmbeddings)
# print("Chunk Embedding shape", chunkEmbeddings.shape)


# ask a question
query = "are you know about bangladesh"
queryEmbedding = model.encode(query, normalize_embeddings=True)

# print("Query Embedding", queryEmbedding)

scores = chunkEmbeddings @ queryEmbedding

# print("Scores",scores)

topK = min(3, len(chunks))
bestIndices = np.argsort(scores)[::-1][:topK]

# print("topK :", topK)
# print("NP.argsort :", np.argsort(scores))
# print("bestIndices :", bestIndices)

# print("\nMost relevant chunks: ")

# for index in bestIndices:
#     print(f"\nScore: {scores[index]:.4f}")
#     print(chunks[index])

# build the context from retrived chunks
context = "\n\n".join(chunks[index] for index in bestIndices)

# print(context)

# load dot env
load_dotenv()

apiKey = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=apiKey)


# prompt for ai

prompt = f""" 
You are a helpful assistant.

Answer the question using only the provided context.
If the context does not contain the answer, say:
"I don't know based on the provided documents."

Context: 
{context}

Question:
{query}
"""

response = client.models.generate_content(model="gemini-3.8-flash", contents=prompt)

print("Question:", query)
print("Answer:")
print(response.text)
