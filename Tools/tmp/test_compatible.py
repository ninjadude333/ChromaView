import subprocess
import sys

def test_with_compatible_numpy():
    """Test with compatible numpy version"""
    print("Installing compatible numpy version...")
    
    # Install compatible numpy version
    subprocess.run([sys.executable, "-m", "pip", "install", "numpy<2.0.0", "--force-reinstall"], check=True)
    
    # Test the connection
    import chromadb
    from chromadb import HttpClient
    
    host = "aipg.dudelabz.com"
    port = 8000
    
    print(f"Using chromadb version: {chromadb.__version__}")
    print(f"Testing connection to ChromaDB at {host}:{port}")
    
    try:
        # Create client
        client = HttpClient(host=host, port=port)
        print("Client created successfully")
        
        # Try heartbeat
        heartbeat = client.heartbeat()
        print(f"Client heartbeat: {heartbeat}")
        
        # Try to list collections
        collections = client.list_collections()
        print(f"Collections: {[c.name for c in collections]}")
        
        # Try to get vendor_emails collection
        if any(c.name == "vendor_emails" for c in collections):
            collection = client.get_collection("vendor_emails")
            count = collection.count()
            print(f"vendor_emails collection count: {count}")
            print("SUCCESS! Connection working!")
        else:
            print("vendor_emails collection not found, but connection is working")
            
    except Exception as e:
        print(f"Connection error: {str(e)}")

if __name__ == "__main__":
    test_with_compatible_numpy()