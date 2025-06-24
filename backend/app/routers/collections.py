from fastapi import APIRouter, HTTPException
from app.services.chroma_service import chroma_service

router = APIRouter()

@router.get("/")
async def get_collections():
    try:
        collections = chroma_service.get_collections()
        return {"collections": collections}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/{collection_name}/info")
async def get_collection_info(collection_name: str):
    try:
        collections = chroma_service.get_collections()
        collection = next((c for c in collections if c.name == collection_name), None)
        if not collection:
            raise HTTPException(status_code=404, detail="Collection not found")
        return collection
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))