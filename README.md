20 Newsgroups Semantic Search Engine

A production-ready semantic search engine on the 20 Newsgroups dataset (~20k articles) with two-phase fuzzy clustering, a cluster-aware semantic cache, and an interactive FastAPI web UI. Supports natural language queries and fast semantic retrieval using embeddings and vector similarity.

Semantic Search FastAPI Project

This project implements a semantic search API using FastAPI, Sentence Transformers, and scikit-learn. It allows querying a dataset using natural language and returns results based on semantic similarity.

Project Structure
semantic_project/
├─ main.py                   # FastAPI app
├─ engine.py                 # Query processing and search logic
├─ precompute_embeddings.py  # Precompute embeddings for the dataset
├─ requirements.txt          # Python dependencies
├─ README.md
├─ .gitignore
└─ src/
   ├─ __init__.py
   ├─ embeddings.py          # Model and precomputed embeddings
   └─ cache.py               # Semantic cache implementation
Installation

Clone the repository:

git clone <your-repo-url>
cd semantic_project

Create and activate a virtual environment:

python -m venv venv
# Windows
.\venv\Scripts\activate
# Mac/Linux
source venv/bin/activate

Install dependencies:

pip install -r requirements.txt
Dataset

This project uses the 20 Newsgroups dataset from UCI Repository
.

Note: The dataset is automatically downloaded when running precompute_embeddings.py.

Precompute Embeddings

Before running the API, precompute embeddings for the dataset:

python precompute_embeddings.py

This may take a few minutes depending on your machine.

Running the API

Start the FastAPI server:

python -m uvicorn main:app --reload

The server will run at http://127.0.0.1:8000.

API documentation is available at http://127.0.0.1:8000/docs.

API Endpoints
1. POST /query

Request Body (JSON):

{
  "query": "machine learning applications"
}

Response Example:

{
  "query": "machine learning applications",
  "cache_hit": true,
  "matched_query": "applications of machine learning",
  "similarity_score": 0.91,
  "result": "Relevant document content...",
  "dominant_cluster": 3
}

On a cache miss, the result is computed and stored in the semantic cache.

2. GET /cache/stats

Response Example:

{
  "total_entries": 42,
  "hit_count": 17,
  "miss_count": 25,
  "hit_rate": 0.405
}
3. DELETE /cache

Flush the cache entirely and reset all stats.

Notes

Do not push venv/ or compiled Python files (.pyc) to GitHub.

Use requirements.txt to recreate the environment on any machine.

Make sure src/ folder contains all 3 modules (__init__.py, embeddings.py, cache.py) for the project to run.

Contact / Help

For issues with deployment or API errors, please contact the project owner or refer to the documentation of FastAPI and Sentence Transformers.
