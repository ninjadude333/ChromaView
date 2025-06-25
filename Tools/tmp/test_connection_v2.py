import requests
import json
import chromadb
from chromadb import HttpClient

def test_chroma_connection_v2():
    """Test connection to ChromaDB using v2 API and chromadb client"""
    host = "aipg.dudelabz.com"
    port = 8000
    
    print(f"Testing connection to ChromaDB at {host}:{port}")
    
    # Try using the chromadb client directly
    try:
        # Basic connection without tenant/database
        print("\nTesting basic connection...")
        client = HttpClient(host=host, port=port)
        heartbeat = client.heartbeat()
        print(f"Heartbeat: {heartbeat}")
        
        # Try to list collections
        try:
            collections = client.list_collections()
            print(f"Collections: {[c.name for c in collections]}")
        except Exception as e:
            print(f"Error listing collections: {str(e)}")
        
        # Try with tenant
        print("\nTesting with tenant...")
        try:
            client_with_tenant = HttpClient(host=host, port=port, tenant="default_tenant")
            collections = client_with_tenant.list_collections()
            print(f"Collections with tenant: {[c.name for c in collections]}")
        except Exception as e:
            print(f"Error with tenant: {str(e)}")
        
        # Try with tenant and database
        print("\nTesting with tenant and database...")
        try:
            client_with_both = HttpClient(
                host=host, 
                port=port, 
                tenant="default_tenant", 
                database="default_database"
            )
            collections = client_with_both.list_collections()
            print(f"Collections with tenant and database: {[c.name for c in collections]}")
        except Exception as e:
            print(f"Error with tenant and database: {str(e)}")
            
        # Try with vendor_emails collection
        print("\nTrying to access vendor_emails collection...")
        try:
            collection = client.get_collection("vendor_emails")
            count = collection.count()
            print(f"vendor_emails collection count: {count}")
        except Exception as e:
            print(f"Error accessing vendor_emails: {str(e)}")
            
    except Exception as e:
        print(f"Error connecting to ChromaDB: {str(e)}")
        
    print("\nConnection recommendation based on your config:")
    print("Host: aipg.dudelabz.com")
    print("Port: 8000")
    print("Remote Connection: True")
    print("Collection: vendor_emails")
    print("Tenant: Leave empty unless required")
    print("Database: Leave empty unless required")

if __name__ == "__main__":
    test_chroma_connection_v2()