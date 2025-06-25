import chromadb
from chromadb import HttpClient

def test_with_tenant_names():
    """Test connection with different tenant names"""
    host = "aipg.dudelabz.com"
    port = 8000
    
    # List of tenant names to try
    tenant_names = [
        "default",
        "admin",
        "main",
        "primary",
        "chromadb",
        "chroma",
        "public"
    ]
    
    print(f"Testing connection to ChromaDB at {host}:{port}")
    
    for tenant in tenant_names:
        try:
            print(f"\nTrying with tenant: '{tenant}'")
            client = HttpClient(host=host, port=port, tenant=tenant)
            
            # Try to list collections
            collections = client.list_collections()
            print(f"SUCCESS! Connected with tenant '{tenant}'")
            print(f"Collections: {[c.name for c in collections]}")
            
            # Try to access vendor_emails collection
            try:
                collection = client.get_collection("vendor_emails")
                count = collection.count()
                print(f"vendor_emails collection count: {count}")
            except Exception as e:
                print(f"Could not access vendor_emails: {str(e)}")
                
            # This tenant worked, so break the loop
            break
            
        except Exception as e:
            print(f"Failed with tenant '{tenant}': {str(e)}")
    
    print("\nIf no tenant worked, try running your working application and check:")
    print("1. What tenant name it's using")
    print("2. What version of chromadb it's using")

if __name__ == "__main__":
    test_with_tenant_names()