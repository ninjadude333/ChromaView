import subprocess
import sys

def test_with_newer_chromadb():
    """Test with a newer version of chromadb that handles tenants better"""
    print("Installing newer chromadb version...")
    
    # Install a newer version that should handle tenants better
    subprocess.run([sys.executable, "-m", "pip", "install", "chromadb==0.4.24", "--force-reinstall"], check=True)
    
    # Test the connection
    import chromadb
    from chromadb import HttpClient
    
    host = "aipg.dudelabz.com"
    port = 8000
    
    print(f"Using chromadb version: {chromadb.__version__}")
    print(f"Testing connection to ChromaDB at {host}:{port}")
    
    try:
        # Create client without specifying tenant
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
            print("SUCCESS! Connection working with chromadb 0.4.24")
        else:
            print("vendor_emails collection not found, but connection is working")
            
    except Exception as e:
        print(f"Connection error: {str(e)}")

if __name__ == "__main__":
    test_with_newer_chromadb()