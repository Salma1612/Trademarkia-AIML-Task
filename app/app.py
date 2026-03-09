# main.py

from fastapi import FastAPI
from pydantic import BaseModel
from src.embeddings import query_model
from src.cache import SemanticCache

app = FastAPI(title="Semantic Search API")

cache = SemanticCache()

class QueryRequest(BaseModel):
    query: str

# POST /query
@app.post("/query")
def query_endpoint(req: QueryRequest):
    q = req.query
    cached, hit = cache.get(q)
    if hit:
        cached["cache_hit"] = True
        return cached

    # Cache miss: compute result
    result = query_model(q)
    response = {
        "query": q,
        "cache_hit": False,
        "matched_query": result["matched_query"],
        "similarity_score": result["similarity_score"],
        "result": result["result"],
        "dominant_cluster": result["dominant_cluster"]
    }
    cache.set(q, response)
    return response

# GET /cache/stats
@app.get("/cache/stats")
def cache_stats():
    return cache.stats()

# DELETE /cache
@app.delete("/cache")
def clear_cache():
    cache.clear()
    return {"message": "Cache cleared successfully"}
