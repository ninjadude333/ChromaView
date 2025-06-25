import chromadb
from chromadb import HttpClient

def final_test():
    """Final test with current setup"""
    host = "aipg.dudelabz.com"
    port = 8000
    
    print(f"Using chromadb version: {chromadb.__version__}")
    print(f"Final test - connecting to {host}:{port}")
    
    try:
        client = HttpClient(host=host, port=port)
        
        # Try the vendor_emails collection directly
        collection = client.get_or_create_collection(name="vendor_emails")
        count = collection.count()
        print(f"SUCCESS! vendor_emails collection has {count} documents")
        
        # Try to get a few documents
        if count > 0:
            results = collection.get(limit=3)
            print(f"Sample documents: {len(results['ids'])} found")
        
        return True
        
    except Exception as e:
        print(f"Failed: {str(e)}")
        return False

if __name__ == "__main__":
    if final_test():
        print("\nConnection works! You can now build the Docker containers:")
        print("docker-compose up --build")
    else:
        print("\nConnection still fails. The ChromaDB server might need configuration changes.")
        print("Check if your ChromaDB server has tenant requirements enabled.")