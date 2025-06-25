from fastapi import APIRouter, HTTPException
from app.models.schemas import ConnectionConfig
from app.services.chroma_service import chroma_service

router = APIRouter()

@router.post("/connect")
async def connect_to_chroma(config: ConnectionConfig):
    try:
        print(f"Attempting to connect to {config.host}:{config.port}, remote={config.is_remote}")
        success = chroma_service.connect(config)
        return {"status": "connected", "config": config}
    except Exception as e:
        print(f"Connection failed: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/disconnect")
async def disconnect_from_chroma():
    try:
        chroma_service.disconnect()
        return {"status": "disconnected"}
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