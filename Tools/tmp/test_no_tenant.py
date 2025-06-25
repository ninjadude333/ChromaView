import chromadb
from chromadb import HttpClient

def test_without_tenant():
    """Test connection without specifying a tenant"""
    host = "aipg.dudelabz.com"
    port = 8000
    
    print(f"Testing connection to ChromaDB at {host}:{port}")
    
    try:
        # Connect without specifying tenant
        client_kwargs = {
            "host": host,
            "port": port
        }
        
        print(f"Creating HttpClient with: {client_kwargs}")
        client = HttpClient(**client_kwargs)
        
        # Try to list collections
        try:
            collections = client.list_collections()
            print(f"Collections: {[c.name for c in collections]}")
        except Exception as e:
            print(f"List collections error: {str(e)}")
            
    except Exception as e:
        print(f"Connection error: {str(e)}")

if __name__ == "__main__":
    test_without_tenant()