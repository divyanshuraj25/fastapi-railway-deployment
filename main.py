import os
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="AI Backend Service")

API_KEY = os.getenv("API_KEY", "default-key")
MODEL_NAME = os.getenv("MODEL_NAME", "gpt-4o-mini")
SIMILARITY_THRESHOLD = float(os.getenv("SIMILARITY_THRESHOLD", "0.75"))

class QueryRequest(BaseModel):
    query: str

@app.get("/")
def root():
    return {"status": "ok", "message": "Service is live"}

@app.get("/health")
def health():
    return {
        "status": "healthy",
        "model": MODEL_NAME,
        "threshold": SIMILARITY_THRESHOLD
    }

@app.post("/predict")
def predict(request: QueryRequest):
    return {
        "query": request.query,
        "model_used": MODEL_NAME,
        "score": SIMILARITY_THRESHOLD,
        "response": f"Processed: '{request.query}' successfully."
    }