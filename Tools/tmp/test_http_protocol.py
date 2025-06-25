import chromadb
from chromadb import HttpClient

def test_with_http_protocol():
    """Test connection with HTTP protocol explicitly specified"""
    host = "aipg.dudelabz.com"
    port = 8000
    collection_name = "vendor_emails"
    
    print(f"Using chromadb version: {chromadb.__version__}")
    print(f"Testing connection to ChromaDB at http://{host}:{port}")
    
    try:
        # Try with HTTP protocol explicitly specified
        client = HttpClient(
            host=host, 
            port=port,
            protocol="http"
        )
        
        # Try to list collections
        collections = client.list_collections()
        print(f"SUCCESS! Connected with HTTP protocol")
        print(f"Collections: {[c.name for c in collections]}")
        
        # Try to access vendor_emails collection
        collection = client.get_or_create_collection(name=collection_name)
        count = collection.count()
        print(f"vendor_emails collection count: {count}")
        
    except Exception as e:
        print(f"Connection error: {str(e)}")

if __name__ == "__main__":
    test_with_http_protocol()