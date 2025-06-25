import chromadb
from typing import List, Dict, Any, Optional
from app.models.schemas import ConnectionConfig, CollectionInfo, DocumentResponse

class ChromaService:
    def __init__(self):
        self.client = None
        self.connection_config = None
    
    def connect(self, config: ConnectionConfig):
        try:
            print(f"Connecting to ChromaDB at {config.host}:{config.port}, remote={config.is_remote}")
            
            if config.is_remote:
                # Use EXACTLY the same approach as your working code
                import chromadb
                
                print(f"Creating HttpClient with host={config.host}, port={config.port}")
                # Exact same parameters as your working code
                self.client = chromadb.HttpClient(
                    host=config.host,
                    port=config.port
                )
                
                # Test connection by accessing vendor_emails collection (exactly like your working code)
                print("Testing connection by accessing vendor_emails collection...")
                collection = self.client.get_or_create_collection(name="vendor_emails")
                print(f"Connection successful - vendor_emails collection accessible")
            else:
                print("Creating local Client")
                self.client = chromadb.Client()
            
            self.connection_config = config
            return True
            
        except Exception as e:
            error_msg = str(e)
            print(f"Connection failed: {error_msg}")
            raise Exception(f"Failed to connect to ChromaDB: {error_msg}")
    
    def disconnect(self):
        self.client = None
        self.connection_config = None
        return True
    
    def get_collections(self) -> List[CollectionInfo]:
        if not self.client:
            raise Exception("Not connected to ChromaDB")
        
        # Use the same approach as your working code
        try:
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
        except Exception as e:
            print(f"list_collections failed: {str(e)}")
            # Fallback to known collections
            known_collections = ["vendor_emails"]
            result = []
            
            for collection_name in known_collections:
                try:
                    collection = self.client.get_or_create_collection(name=collection_name)
                    count = collection.count()
                    result.append(CollectionInfo(
                        name=collection.name,
                        count=count,
                        metadata=collection.metadata
                    ))
                except Exception as e:
                    print(f"Could not access collection {collection_name}: {str(e)}")
            
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