import chromadb
from chromadb import HttpClient, Settings

def test_with_ssl_disabled():
    """Test connection with SSL verification disabled"""
    host = "aipg.dudelabz.com"
    port = 8000
    collection_name = "vendor_emails"
    
    print(f"Using chromadb version: {chromadb.__version__}")
    print(f"Testing connection to ChromaDB at {host}:{port} with SSL verification disabled")
    
    try:
        # Try with SSL verification disabled
        settings = Settings(
            chroma_client_auth_provider="token",
            chroma_client_auth_credentials=None,
            anonymized_telemetry=False,
            chroma_server_ssl_enabled=False
        )
        
        client = HttpClient(
            host=host, 
            port=port,
            ssl=False,
            settings=settings
        )
        
        # Try to list collections
        collections = client.list_collections()
        print(f"SUCCESS! Connected with SSL verification disabled")
        print(f"Collections: {[c.name for c in collections]}")
        
        # Try to access vendor_emails collection
        collection = client.get_or_create_collection(name=collection_name)
        count = collection.count()
        print(f"vendor_emails collection count: {count}")
        
    except Exception as e:
        print(f"Connection error: {str(e)}")
        
        # Try with different parameters
        try:
            print("\nTrying with different parameters...")
            client = HttpClient(
                host=host, 
                port=port,
                ssl=False
            )
            
            collections = client.list_collections()
            print(f"SUCCESS! Connected with simple SSL=False")
            print(f"Collections: {[c.name for c in collections]}")
        except Exception as e:
            print(f"Still failed: {str(e)}")

if __name__ == "__main__":
    test_with_ssl_disabled()