20 Newsgroups Semantic Search Engine
A production-ready semantic search engine on the 20 Newsgroups dataset (~20k articles) with two-phase fuzzy clustering, a cluster-aware semantic cache, and an interactive FastAPI web UI. Supports natural language queries and fast semantic retrieval using embeddings and vector similarity.

If you want, I can also write a slightly longer version with badges and key features that looks perfect for GitHub’s README starter. This will make your repo look polished for submissions. Do you want me to do that?

readme text

Here’s a full, professional README text you can use for your repository. It’s clean, original, and submission-ready:

20 Newsgroups — Semantic Search Engine

A production-ready semantic search engine built on the 20 Newsgroups dataset (~20k articles). This project implements two-phase clustering, a custom semantic cache, and an interactive FastAPI web interface for fast and accurate semantic search.

Features

Semantic Search – Query the dataset using natural language, not just keywords.

Two-Phase Fuzzy Clustering – Organizes documents into semantic clusters for faster retrieval.

Cluster-Aware Semantic Cache – Reuses results from similar queries for instant responses.

FastAPI Web UI – Interactive interface to explore search results and cache behavior.

Vector Store – Uses ChromaDB for efficient embedding storage and cosine similarity search.

Installation & Quick Start

Clone the repository

git clone <your-repo-link>
cd <repo-folder>

Install dependencies

conda create -n semantic_env python=3.10
conda activate semantic_env
pip install -r requirements.txt

Run the pipeline (embedding + clustering + cache setup)

python scripts/run_pipeline.py

Start the API and UI

uvicorn src.api:app --host 0.0.0.0 --port 8000

Open the UI in a browser
http://localhost:8000

Architecture & Design

Embedding Model: all-MiniLM-L6-v2 (384-dim, fast and accurate embeddings)

Vector Store: File-based ChromaDB with cosine similarity index

Clustering: Two-phase fuzzy C-Means to improve retrieval speed and cache efficiency

Cache: JSON-based cluster-aware semantic cache with configurable similarity threshold

API & UI: FastAPI backend with lightweight interactive web interface

Project Structure
src/
  data_pipeline.py       # Load, clean, embed, store in ChromaDB
  clustering.py          # Two-phase fuzzy C-Means clustering
  semantic_cache.py      # Cluster-aware semantic cache implementation
  api.py                 # FastAPI service + interactive web UI
  static/index.html      # Web UI
scripts/
  run_pipeline.py        # Master pipeline runner
notebooks/
  heuristic_analysis.ipynb  # Cache threshold analysis
tests/
  test_cache.py          # Semantic cache unit tests
  test_api.py            # API integration tests
Sample Queries

Apple / Mac Hardware

“What is the word apple means?” → new cache entry

“Macintosh display problems” → ⚡ CACHE HIT

Space / NASA

“NASA space shuttle launch Mars mission” → new cache entry

“Space shuttle rocket NASA orbit” → ⚡ CACHE HIT

Different Intent (Boundary Case)

“Commercial satellite launch SpaceX” → CACHE MISS

Learning Outcomes

End-to-end semantic search engine implementation

Combining embeddings, vector databases, clustering, and caching for fast retrieval

Production-ready Python API development and interactive web UI design
