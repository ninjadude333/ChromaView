import chromadb
from chromadb import HttpClient

def test_with_explicit_empty_tenant():
    """Test connection with explicit empty tenant"""
    host = "aipg.dudelabz.com"
    port = 8000
    
    print(f"Testing connection to ChromaDB at {host}:{port}")
    
    try:
        # Connect with explicit empty tenant
        client = HttpClient(
            host=host, 
            port=port,
            tenant=""  # Explicitly set empty tenant
        )
        print(f"Connected successfully with explicit empty tenant")
        
        # List collections
        try:
            collections = client.list_collections()
            print(f"Collections: {[c.name for c in collections]}")
        except Exception as e:
            print(f"List collections error: {str(e)}")
            
    except Exception as e:
        print(f"Connection error: {str(e)}")

if __name__ == "__main__":
    test_with_explicit_empty_tenant()