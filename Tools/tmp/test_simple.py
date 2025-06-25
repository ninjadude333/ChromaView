import chromadb
from chromadb import HttpClient

def test_simple():
    """Test with the simplest possible configuration"""
    host = "aipg.dudelabz.com"
    port = 8000
    collection_name = "vendor_emails"
    
    print(f"Using chromadb version: {chromadb.__version__}")
    print(f"Testing connection to ChromaDB at {host}:{port}")
    
    try:
        # Create a new client instance
        client = HttpClient(host=host, port=port)
        print("Client created successfully")
        
        # Try to list collections
        try:
            collections = client.list_collections()
            print(f"Collections: {[c.name for c in collections]}")
        except Exception as e:
            print(f"List collections error: {str(e)}")
        
        # Try to get or create collection
        try:
            collection = client.get_or_create_collection(name=collection_name)
            print(f"Collection '{collection_name}' accessed successfully")
            
            # Try to get count
            count = collection.count()
            print(f"Collection count: {count}")
        except Exception as e:
            print(f"Collection error: {str(e)}")
            
    except Exception as e:
        print(f"Connection error: {str(e)}")

if __name__ == "__main__":
    test_simple()