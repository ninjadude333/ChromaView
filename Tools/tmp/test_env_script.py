
import chromadb
from chromadb import HttpClient
import requests

def test_connection():
    host = "aipg.dudelabz.com"
    port = 8000
    
    print(f"Using chromadb version: {chromadb.__version__}")
    print(f"Testing connection to ChromaDB at {host}:{port}")
    
    # First check if server is reachable
    try:
        response = requests.get(f"http://{host}:{port}/api/v2/heartbeat")
        print(f"Server heartbeat: {response.status_code} - {response.text}")
    except Exception as e:
        print(f"Server not reachable: {str(e)}")
        return
    
    # Try to connect with chromadb client
    try:
        client = HttpClient(host=host, port=port)
        print("Client created successfully")
        
        # Try heartbeat
        heartbeat = client.heartbeat()
        print(f"Client heartbeat: {heartbeat}")
        
        # Try to list collections
        collections = client.list_collections()
        print(f"Collections: {[c.name for c in collections]}")
        
        # Try to get or create vendor_emails collection
        collection = client.get_or_create_collection(name="vendor_emails")
        count = collection.count()
        print(f"vendor_emails collection count: {count}")
        
    except Exception as e:
        print(f"Connection error: {str(e)}")

if __name__ == "__main__":
    test_connection()
