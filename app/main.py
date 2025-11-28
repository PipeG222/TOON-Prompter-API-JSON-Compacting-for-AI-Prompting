from fastapi import FastAPI
from app.routers.rest import router as rest_router

app = FastAPI(
    title="TOON Prompter API",
    description="JSON compaction + LLM optimization API",
    version="1.0.0"
)

app.include_router(rest_router, prefix="/convert")

@app.get("/")
def root():
    return {"status": "ok", "message": "TOON API running"}
