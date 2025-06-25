from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import collections, documents, connections

app = FastAPI(
    title="ChromaView API",
    description="API for ChromaDB visualization and exploration",
    version="0.1.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://172.16.205.103:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(connections.router, prefix="/api/connections", tags=["connections"])
app.include_router(collections.router, prefix="/api/collections", tags=["collections"])
app.include_router(documents.router, prefix="/api/documents", tags=["documents"])

@app.get("/")
async def root():
    return {"message": "ChromaView API is running"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}