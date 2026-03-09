Trademarkia Semantic Search with Cluster-Aware Semantic Cache
Project Overview

This project implements a semantic search system built using modern Natural Language Processing (NLP) and vector similarity search techniques.

The system retrieves relevant documents using Sentence Embeddings, FAISS Vector Indexing, Fuzzy Clustering, and a custom semantic caching layer.

The search system is exposed through a FastAPI service, allowing users to query the corpus using natural language queries.

During development, the API was temporarily exposed using ngrok public tunnels to allow external access and testing.

This project follows the architecture specified in the Trademarkia AI/ML Engineer Task and demonstrates how clustering, vector search, and semantic caching can work together in a scalable semantic retrieval system.

System Architecture

User Query
→ Query Embedding Generation
→ Cluster Prediction (Fuzzy C-Means)
→ Semantic Cache Lookup
→ FAISS Vector Search (on cache miss)
→ Retrieve Top Documents
→ Store Result in Semantic Cache
→ Return Response via FastAPI

Repository Structure
trademarkia-semantic-search/

app/
│
├── __init__.py
├── app.py  → Main FastAPI service implementation
│
└── utils/
    ├── __init__.py
    ├── engine.py → Query processing and semantic search logic
    ├── embeddings.py → Sentence Transformer embedding utilities
    ├── cache.py → Semantic cache implementation
    └── precompute_embeddings.py → Script to generate document embeddings

data/
│
├── raw/
│   └── .gitkeep
│
├── processed/
│   └── .gitkeep
│
└── artifacts/
    └── .gitkeep

notebooks/
│
└── pipeline.ipynb → End-to-end experimentation notebook

Other files

requirements.txt → Python dependencies  
.gitignore  
README.md
Complete System Pipeline

This section explains the end-to-end machine learning pipeline implemented in this project.

1. Dataset Collection

The dataset used in this project is the 20 Newsgroups Dataset, obtained from the UCI Machine Learning Repository.

The dataset contains approximately 20,000 news articles across 20 discussion categories.

Example categories include:

Politics

Religion

Sports

Computer Hardware

Space

Firearms

The dataset is distributed as a compressed archive of raw text documents, which must be parsed and structured before further processing.

2. Data Preprocessing

The raw dataset contains several types of noise and irrelevant metadata, including:

Email headers

Formatting artifacts

Punctuation

Stopwords

To improve the quality of the downstream semantic representations, a text preprocessing pipeline was implemented.

Preprocessing Steps

The following transformations were applied:

• Lowercasing
• Punctuation removal
• Stopword removal
• Metadata stripping
• Whitespace normalization

Generated Intermediate Files

The preprocessing pipeline produces several intermediate datasets:

raw_documents.csv → structured version of the original dataset
cleaned_documents.csv → cleaned textual content
filtered_documents.csv → final dataset after noise filtering

Documents that were too short, noisy, or semantically weak were removed to ensure high-quality embeddings.

3. Document Embedding Generation

To enable semantic similarity search, each document is converted into a dense vector embedding.

Embedding Model

Sentence Transformers

Model used:

all-MiniLM-L6-v2

Library:

sentence-transformers

Embedding dimension:

384-dimensional vector representation

This model converts each document into a semantic vector representation capturing contextual meaning rather than simple keyword presence.

4. Vector Database using FAISS

To efficiently search across thousands of embeddings, a vector similarity index is built using FAISS (Facebook AI Similarity Search).

Technology Used

FAISS Vector Database

Index Type

Flat L2 Index

FAISS enables fast nearest-neighbour search across high-dimensional embeddings.

When a query embedding is generated, FAISS retrieves the most semantically similar documents.

5. Fuzzy Clustering of Documents

Real-world documents often belong to multiple semantic topics simultaneously.

For example:

A document discussing gun legislation may relate to both politics and firearms.

Therefore, traditional hard clustering algorithms such as K-Means are not suitable.

Instead, this project uses Fuzzy C-Means Clustering.

Algorithm Used

Fuzzy C-Means

Library used:

scikit-fuzzy

Key Concept

Instead of assigning each document to a single cluster, Fuzzy C-Means assigns membership probabilities.

Example:

Document A →
Cluster 1 → 0.2
Cluster 3 → 0.7
Cluster 7 → 0.1

This allows documents to belong partially to multiple clusters, which better reflects real semantic relationships.

6. Semantic Cache Design

Traditional caches fail when queries are phrased differently but have the same meaning.

Example:

"How do graphics cards work?"
vs
"Explain GPU architecture"

A keyword-based cache would treat these as different queries.

To solve this, the project implements a semantic cache from first principles.

Core Idea

Queries are compared using embedding similarity instead of exact string matching.

Cache Workflow

When a query arrives:

The query is converted into a vector embedding

The system checks similarity against previous cached query embeddings

If similarity exceeds a predefined threshold, it becomes a cache hit

Otherwise the system performs a FAISS vector search

The result is then stored in the semantic cache.

Cache Metrics

The system tracks:

Total entries

Cache hits

Cache misses

Hit rate

7. FastAPI Service

The search system is exposed as a REST API using FastAPI.

Framework

FastAPI

ASGI Server

Uvicorn

Implemented Endpoints

POST /query

Example Response:

{
  "query": "...",
  "cache_hit": true,
  "matched_query": "...",
  "similarity_score": 0.91,
  "result": "...",
  "dominant_cluster": 3
}

GET /cache/stats

Returns semantic cache statistics.

Example:

{
  "total_entries": 42,
  "hit_count": 17,
  "miss_count": 25,
  "hit_rate": 0.405
}

DELETE /cache

Clears cache entries and statistics.

Running the Project

Install dependencies:

pip install -r requirements.txt

Start the API server:

uvicorn app.app:app --host 0.0.0.0 --port 8000

Open API documentation:

http://localhost:8000/docs

Author

Shaik Salma
23BCE20344
B.Tech Computer Science (AI & ML)
Pre-Final Year Student
VIT-AP University

