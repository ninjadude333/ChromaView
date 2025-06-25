import chromadb
from typing import List, Dict, Any, Optional
from app.models.schemas import ConnectionConfig, CollectionInfo, DocumentResponse

class ChromaService:
    def __init__(self):
        self.client = None
        self.connection_config = None
    
    def connect(self, config: ConnectionConfig):
        try:
            if config.is_remote:
                self.client = chromadb.HttpClient(
                    host=config.host,
                    port=config.port
                )
            else:
                self.client = chromadb.Client()
            
            self.connection_config = config
            # Test connection by creating/accessing a test collection
            try:
                # This will create the tenant if it doesn't exist
                test_collection = self.client.get_or_create_collection(name="connection_test")
            except Exception:
                # Fallback to heartbeat if collection access fails
                self.client.heartbeat()
            return True
        except Exception as e:
            raise Exception(f"Failed to connect to ChromaDB: {str(e)}")
    
    def disconnect(self):
        self.client = None
        self.connection_config = None
        return True
    
    def get_collections(self) -> List[CollectionInfo]:
        if not self.client:
            raise Exception("Not connected to ChromaDB")
        
        collections = self.client.list_collections()
        result = []
        
        for collection in collections:
            count = collection.count()
            result.append(CollectionInfo(
                name=collection.name,
                count=count,
                metadata=collection.metadata
            ))
        
        return result
    
    def get_documents(self, collection_name: str, limit: int = 50, offset: int = 0) -> List[DocumentResponse]:
        if not self.client:
            raise Exception("Not connected to ChromaDB")
        
        collection = self.client.get_collection(collection_name)
        
        # Get documents with pagination
        results = collection.get(
            limit=limit,
            offset=offset,
            include=["documents", "metadatas"]
        )
        
        documents = []
        for i, doc_id in enumerate(results["ids"]):
            documents.append(DocumentResponse(
                id=doc_id,
                document=results["documents"][i] if results["documents"] else None,
                metadata=results["metadatas"][i] if results["metadatas"] else None
            ))
        
        return documents
    
    def search_documents(self, collection_name: str, query: str, limit: int = 10) -> List[DocumentResponse]:
        if not self.client:
            raise Exception("Not connected to ChromaDB")
        
        collection = self.client.get_collection(collection_name)
        
        results = collection.query(
            query_texts=[query],
            n_results=limit,
            include=["documents", "metadatas", "distances"]
        )
        
        documents = []
        for i, doc_id in enumerate(results["ids"][0]):
            documents.append(DocumentResponse(
                id=doc_id,
                document=results["documents"][0][i] if results["documents"] else None,
                metadata=results["metadatas"][0][i] if results["metadatas"] else None,
                distance=results["distances"][0][i] if results["distances"] else None
            ))
        
        return documents

# Global service instance
chroma_service = ChromaService()