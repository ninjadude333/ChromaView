import chromadb
from chromadb import HttpClient, Settings

def test_bypass_tenant():
    """Test different approaches to bypass tenant requirement"""
    host = "aipg.dudelabz.com"
    port = 8000
    
    print(f"Using chromadb version: {chromadb.__version__}")
    print(f"Testing connection to ChromaDB at {host}:{port}")
    
    # Try approach 1: Using Settings with empty tenant
    try:
        print("\nApproach 1: Using Settings with empty tenant")
        settings = Settings(
            chroma_server_host=host,
            chroma_server_http_port=port,
            chroma_api_impl="rest",
            tenant="",
            database=""
        )
        client = chromadb.Client(settings)
        collections = client.list_collections()
        print(f"SUCCESS! Collections: {[c.name for c in collections]}")
        return client
    except Exception as e:
        print(f"Failed: {str(e)}")
    
    # Try approach 2: Direct HTTP requests to bypass client
    try:
        print("\nApproach 2: Using requests directly")
        import requests
        
        # Try to get collections directly
        response = requests.get(f"http://{host}:{port}/api/v1/collections")
        if response.status_code == 200:
            print(f"SUCCESS! Direct API call worked: {response.json()}")
        else:
            print(f"Direct API failed: {response.status_code} - {response.text}")
    except Exception as e:
        print(f"Failed: {str(e)}")
    
    # Try approach 3: Using different tenant names
    tenant_names = ["", "default", "public", "main"]
    for tenant in tenant_names:
        try:
            print(f"\nApproach 3: Trying tenant '{tenant}'")
            client = HttpClient(host=host, port=port, tenant=tenant)
            collections = client.list_collections()
            print(f"SUCCESS with tenant '{tenant}'! Collections: {[c.name for c in collections]}")
            return client
        except Exception as e:
            print(f"Failed with tenant '{tenant}': {str(e)}")
    
    print("\nAll approaches failed. The ChromaDB instance might require specific tenant configuration.")
    return None

if __name__ == "__main__":
    test_bypass_tenant()