import chromadb
from chromadb import HttpClient

def test_exact_working_code():
    """Test using the exact code from the working application"""
    chroma_host = "aipg.dudelabz.com"
    chroma_port = 8000
    collection_name = "vendor_emails"
    
    print(f"Testing connection to ChromaDB at {chroma_host}:{chroma_port}")
    
    try:
        # This is the exact code from your working application
        client = HttpClient(host=chroma_host, port=chroma_port)
        collection = client.get_or_create_collection(name=collection_name)
        
        # Check if connection worked
        count = collection.count()
        print(f"Connection successful! Collection '{collection_name}' has {count} documents")
        
        # List all collections
        collections = client.list_collections()
        print(f"All collections: {[c.name for c in collections]}")
        
    except Exception as e:
        print(f"Connection error: {str(e)}")
        
        # Try with different chromadb versions
        print("\nChecking chromadb version:")
        import pkg_resources
        version = pkg_resources.get_distribution("chromadb").version
        print(f"Installed chromadb version: {version}")
        print("Your working application might be using a different version.")

if __name__ == "__main__":
    test_exact_working_code()