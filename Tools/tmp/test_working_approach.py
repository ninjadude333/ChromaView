import chromadb
from chromadb import HttpClient

def test_working_approach():
    """Test connection using the approach from the working code"""
    host = "aipg.dudelabz.com"
    port = 8000
    collection_name = "vendor_emails"
    
    print(f"Testing connection to ChromaDB at {host}:{port}")
    
    try:
        # Connect using HttpClient directly (like in the working code)
        client = HttpClient(host=host, port=port)
        print(f"Connected successfully")
        
        # Try to get the collection
        try:
            collection = client.get_or_create_collection(name=collection_name)
            count = collection.count()
            print(f"{collection_name} collection count: {count}")
            
            # List all collections
            collections = client.list_collections()
            print(f"All collections: {[c.name for c in collections]}")
            
        except Exception as e:
            print(f"Collection error: {str(e)}")
            
    except Exception as e:
        print(f"Connection error: {str(e)}")

if __name__ == "__main__":
    test_working_approach()