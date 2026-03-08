# precompute_embeddings.py
import os
import numpy as np
from sklearn.datasets import fetch_20newsgroups
from sentence_transformers import SentenceTransformer

# Load dataset
data = fetch_20newsgroups(subset='all', remove=('headers','footers','quotes'))
documents = data.data

# Load model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Save embeddings
if not os.path.exists("cache"):
    os.makedirs("cache")

doc_embeddings = model.encode(documents, convert_to_numpy=True)
np.save("cache/doc_embeddings.npy", doc_embeddings)
print("Embeddings precomputed and saved.")