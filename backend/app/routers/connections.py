from fastapi import APIRouter, HTTPException
from app.models.schemas import ConnectionConfig
from app.services.chroma_service import chroma_service

router = APIRouter()

@router.post("/connect")
async def connect_to_chroma(config: ConnectionConfig):
    try:
        success = chroma_service.connect(config)
        return {"status": "connected", "config": config}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/status")
async def get_connection_status():
    if chroma_service.client is None:
        return {"status": "disconnected"}
    
    try:
        chroma_service.client.heartbeat()
        return {
            "status": "connected",
            "config": chroma_service.connection_config
        }
    except:
        return {"status": "disconnected"}