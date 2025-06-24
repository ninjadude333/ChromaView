from fastapi import APIRouter, HTTPException, Query
from app.models.schemas import SearchRequest
from app.services.chroma_service import chroma_service

router = APIRouter()

@router.get("/{collection_name}")
async def get_documents(
    collection_name: str,
    limit: int = Query(50, ge=1, le=100),
    offset: int = Query(0, ge=0)
):
    try:
        documents = chroma_service.get_documents(collection_name, limit, offset)
        return {"documents": documents, "limit": limit, "offset": offset}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/{collection_name}/search")
async def search_documents(collection_name: str, search_request: SearchRequest):
    try:
        documents = chroma_service.search_documents(
            collection_name, 
            search_request.query, 
            search_request.limit
        )
        return {"documents": documents, "query": search_request.query}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))