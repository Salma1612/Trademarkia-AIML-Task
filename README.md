20 Newsgroups — Semantic Search Engine

Trademarkia AI/ML Engineer Task | Built by Shaik Salma

A production-ready semantic search engine on the 20 Newsgroups dataset (~20k articles). Includes two-phase fuzzy clustering, a custom cluster-aware semantic cache, and an interactive FastAPI web UI. Supports natural language queries and fast semantic retrieval using embeddings and vector similarity.

⚡ Quick Start (Recommended)

Clone the repository

git clone <your-repo-url>
cd semantic_project

Create & activate a virtual environment

python -m venv venv
# Windows
.\venv\Scripts\activate
# Mac/Linux
source venv/bin/activate

Install dependencies

pip install -r requirements.txt

Dataset
This project uses the 20 Newsgroups dataset from UCI Repository:
20 Newsgroups Dataset

⚡ Note: The dataset is automatically downloaded when running precompute_embeddings.py.

Precompute Embeddings
Before running the API, precompute embeddings for the dataset:

python precompute_embeddings.py

⚡ This may take a few minutes depending on your machine.

Run the API

python -m uvicorn main:app --reload

The server will run at: http://127.0.0.1:8000

API docs (Swagger UI): http://127.0.0.1:8000/docs

🧪 API Endpoints
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

📂 Project Structure
semantic_project/
├─ main.py                  # FastAPI app
├─ engine.py                # Query processing & search logic
├─ precompute_embeddings.py # Precompute embeddings for the dataset
├─ requirements.txt         # Python dependencies
├─ README.md
├─ .gitignore
└─ src/
   ├─ __init__.py
   ├─ embeddings.py         # Model & precomputed embeddings
   └─ cache.py              # Semantic cache implementation
🧠 Architecture & Design Decisions
Decision	Choice	Rationale
Embedding model	all-MiniLM-L6-v2	384-dim, purpose-built for retrieval, ~3× faster than large models
Vector store	ChromaDB	File-backed, zero infra, cosine HNSW index
Clustering	Two-phase FCM	Sample 5k → fit centers → predict on all 14k
Cluster count	k=13 (silhouette)	Avoids assuming 20 labels = true semantic structure
Cache lookup	Cluster-bucketed cosine	O(N/k) vs O(N) — ~13× speedup as cache grows
Cache threshold	0.80	Rephrasings match, dissimilar queries separate cleanly
Cache persistence	Pure JSON	No Redis, no SQLite — built from scratch
State management	app.state singleton	Single model + cache instance, no race conditions
🧪 Sample Queries to Test the Semantic Cache

Try these query pairs in the UI to see cache behavior:

Pair 1 — Apple / Mac Hardware

what is the word apple means → hits the corpus (~300ms)

Macintosh display problems → ⚡ CACHE HIT (same semantic cluster, <1ms)

Pair 2 — Space / NASA

NASA space shuttle launch Mars mission → new cache entry

space shuttle rocket NASA orbit → ⚡ CACHE HIT

Pair 3 — Threshold boundary (should MISS)

commercial satellite launch SpaceX → CACHE MISS (different intent, demonstrates 0.80 threshold heuristic)

