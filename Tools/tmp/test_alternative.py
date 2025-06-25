import chromadb

def test_alternative():
    """Test with alternative client creation approach"""
    host = "aipg.dudelabz.com"
    port = 8000
    collection_name = "vendor_emails"
    
    print(f"Using chromadb version: {chromadb.__version__}")
    print(f"Testing connection to ChromaDB at {host}:{port}")
    
    try:
        # Create client using the chromadb.Client approach
        client = chromadb.Client(
            chromadb.config.Settings(
                chroma_api_impl="rest",
                chroma_server_host=host,
                chroma_server_http_port=port
            )
        )
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
    test_alternative()