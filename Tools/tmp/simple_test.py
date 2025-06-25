import chromadb
from chromadb import HttpClient

def test_chroma_connection():
    """Test connection to ChromaDB using the chromadb client library"""
    host = "aipg.dudelabz.com"
    port = 8000
    
    print(f"Testing connection to ChromaDB at {host}:{port}")
    
    try:
        # Basic connection without tenant/database
        client = HttpClient(host=host, port=port)
        print(f"Connected successfully")
        
        # Test heartbeat
        try:
            heartbeat = client.heartbeat()
            print(f"Heartbeat: {heartbeat}")
        except Exception as e:
            print(f"Heartbeat error: {str(e)}")
        
        # List collections
        try:
            collections = client.list_collections()
            print(f"Collections: {[c.name for c in collections]}")
        except Exception as e:
            print(f"List collections error: {str(e)}")
            
        # Try to get vendor_emails collection
        try:
            collection = client.get_collection("vendor_emails")
            count = collection.count()
            print(f"vendor_emails collection count: {count}")
        except Exception as e:
            print(f"Error accessing vendor_emails: {str(e)}")
            
    except Exception as e:
        print(f"Connection error: {str(e)}")

if __name__ == "__main__":
    test_chroma_connection()