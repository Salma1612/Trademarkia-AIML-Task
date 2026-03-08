# src/embeddings.py
import os
import numpy as np
from sklearn.datasets import fetch_20newsgroups
from sentence_transformers import SentenceTransformer

# Load dataset
data = fetch_20newsgroups(subset='all', remove=('headers','footers','quotes'))
documents = data.data

# Load model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Load precomputed embeddings instantly
embedding_file = os.path.join("cache", "doc_embeddings.npy")
doc_embeddings = np.load(embedding_file)
print("Embeddings loaded instantly. FastAPI will start immediately.")

def query_model(query: str):
    q_embed = model.encode([query], convert_to_numpy=True)[0]
    q_norm = q_embed / np.linalg.norm(q_embed)
    doc_norms = doc_embeddings / np.linalg.norm(doc_embeddings, axis=1, keepdims=True)
    cosine_scores = np.dot(doc_norms, q_norm)
    best_idx = int(np.argmax(cosine_scores))
    best_score = float(cosine_scores[best_idx])
    return {
        "matched_query": documents[best_idx],
        "similarity_score": best_score,
        "result": documents[best_idx],
        "dominant_cluster": best_idx
    }
