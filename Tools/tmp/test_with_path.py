import chromadb
from chromadb import HttpClient

def test_with_api_path():
    """Test connection with specific API path"""
    host = "aipg.dudelabz.com"
    port = 8000
    collection_name = "vendor_emails"
    
    print(f"Using chromadb version: {chromadb.__version__}")
    print(f"Testing connection to ChromaDB at {host}:{port}")
    
    # Try with different API paths
    api_paths = ["/api/v1", "/api", "", "/v1", "/v2"]
    
    for api_path in api_paths:
        try:
            print(f"\nTrying with api_path: '{api_path}'")
            client = HttpClient(
                host=host, 
                port=port,
                path=api_path
            )
            
            # Try to list collections
            try:
                collections = client.list_collections()
                print(f"SUCCESS! Connected with api_path '{api_path}'")
                print(f"Collections: {[c.name for c in collections]}")
                
                # Try to access vendor_emails collection
                try:
                    collection = client.get_or_create_collection(name=collection_name)
                    count = collection.count()
                    print(f"vendor_emails collection count: {count}")
                    print(f"\nWORKING CONFIGURATION:")
                    print(f"host: {host}")
                    print(f"port: {port}")
                    print(f"path: {api_path}")
                    return
                except Exception as e:
                    print(f"Could not access vendor_emails: {str(e)}")
            except Exception as e:
                print(f"List collections error: {str(e)}")
                
        except Exception as e:
            print(f"Failed with api_path '{api_path}': {str(e)}")
    
    print("\nNone of the API paths worked.")

if __name__ == "__main__":
    test_with_api_path()