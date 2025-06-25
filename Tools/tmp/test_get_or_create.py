import chromadb
from chromadb import HttpClient

def test_get_or_create():
    """Test using get_or_create_collection like in your working code"""
    host = "aipg.dudelabz.com"
    port = 8000
    collection_name = "vendor_emails"
    
    print(f"Using chromadb version: {chromadb.__version__}")
    print(f"Testing connection to ChromaDB at {host}:{port}")
    
    try:
        # Use the exact same approach as your working code
        client = HttpClient(host=host, port=port)
        print("Client created successfully")
        
        # Use get_or_create_collection instead of list_collections
        collection = client.get_or_create_collection(name=collection_name)
        print(f"Collection '{collection_name}' accessed successfully")
        
        # Try to get count
        count = collection.count()
        print(f"Collection count: {count}")
        
        print("SUCCESS! Connection working with get_or_create_collection!")
        return True
        
    except Exception as e:
        print(f"Connection error: {str(e)}")
        return False

if __name__ == "__main__":
    test_get_or_create()