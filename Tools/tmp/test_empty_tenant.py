import chromadb
from chromadb import HttpClient, Settings

def test_chroma_connection():
    """Test connection to ChromaDB with explicit empty tenant"""
    host = "aipg.dudelabz.com"
    port = 8000
    
    print(f"Testing connection to ChromaDB at {host}:{port}")
    
    try:
        # Create settings with explicit empty tenant
        settings = Settings(
            chroma_api_impl="rest",
            chroma_server_host=host,
            chroma_server_http_port=port,
            tenant="",  # Explicitly set empty tenant
            anonymized_telemetry=False
        )
        
        # Connect with settings
        client = chromadb.Client(settings)
        print(f"Connected successfully with empty tenant")
        
        # List collections
        try:
            collections = client.list_collections()
            print(f"Collections: {[c.name for c in collections]}")
            
            # Try to get vendor_emails collection
            if any(c.name == "vendor_emails" for c in collections):
                collection = client.get_collection("vendor_emails")
                count = collection.count()
                print(f"vendor_emails collection count: {count}")
        except Exception as e:
            print(f"List collections error: {str(e)}")
            
    except Exception as e:
        print(f"Connection error: {str(e)}")

if __name__ == "__main__":
    test_chroma_connection()