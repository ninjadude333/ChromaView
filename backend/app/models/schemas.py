from pydantic import BaseModel
from typing import Optional, Dict, Any, List

class ConnectionConfig(BaseModel):
    host: str = "localhost"
    port: int = 8000
    is_remote: bool = False
    tenant: Optional[str] = None
    database: Optional[str] = None

class CollectionInfo(BaseModel):
    name: str
    count: int
    metadata: Optional[Dict[str, Any]] = None

class DocumentResponse(BaseModel):
    id: str
    document: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    distance: Optional[float] = None

class SearchRequest(BaseModel):
    query: str
    collection_name: str
    limit: int = 10
    where: Optional[Dict[str, Any]] = None