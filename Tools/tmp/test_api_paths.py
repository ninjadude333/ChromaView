import chromadb
from chromadb import HttpClient

def test_with_version_0_4_15():
    """Test using the exact code from the working application with version 0.4.15"""
    print(f"Using chromadb version: {chromadb.__version__}")
    
    # Your working code configuration
    chroma_host = "aipg.dudelabz.com"
    chroma_port = 8000
    collection_name = "vendor_emails"
    
    print(f"Testing connection to ChromaDB at {chroma_host}:{chroma_port}")
    
    try:
        # Try with different API paths
        api_paths = ["", "/api", "/api/v1", "/api/v2"]
        
        for api_path in api_paths:
            try:
                print(f"\nTrying with api_path: '{api_path}'")
                client = HttpClient(
                    host=chroma_host, 
                    port=chroma_port,
                    path=api_path
                )
                
                # Try to list collections
                collections = client.list_collections()
                print(f"SUCCESS! Connected with api_path '{api_path}'")
                print(f"Collections: {[c.name for c in collections]}")
                
                # Try to access vendor_emails collection
                try:
                    collection = client.get_or_create_collection(name=collection_name)
                    count = collection.count()
                    print(f"vendor_emails collection count: {count}")
                except Exception as e:
                    print(f"Could not access vendor_emails: {str(e)}")
                    
                # This api_path worked, so break the loop
                break
                
            except Exception as e:
                print(f"Failed with api_path '{api_path}': {str(e)}")
        
    except Exception as e:
        print(f"Connection error: {str(e)}")

if __name__ == "__main__":
    test_with_version_0_4_15()