import subprocess
import sys

def test_with_older_chromadb():
    """Test with older chromadb versions that might not have tenant requirements"""
    
    # Try different versions
    versions_to_try = ["0.3.29", "0.4.0", "0.4.5", "0.4.10"]
    
    for version in versions_to_try:
        try:
            print(f"\n=== Testing with chromadb {version} ===")
            
            # Install the version
            subprocess.run([sys.executable, "-m", "pip", "install", f"chromadb=={version}", "--force-reinstall"], 
                         check=True, capture_output=True)
            
            # Test connection
            import chromadb
            from chromadb import HttpClient
            
            host = "aipg.dudelabz.com"
            port = 8000
            collection_name = "vendor_emails"
            
            print(f"Using chromadb version: {chromadb.__version__}")
            
            # Test the connection
            client = HttpClient(host=host, port=port)
            collection = client.get_or_create_collection(name=collection_name)
            count = collection.count()
            print(f"SUCCESS! Collection '{collection_name}' count: {count}")
            print(f"Working version: {version}")
            return version
            
        except Exception as e:
            print(f"Failed with version {version}: {str(e)}")
            continue
    
    print("\nAll versions failed. Your working app might be using a very specific configuration.")
    return None

if __name__ == "__main__":
    working_version = test_with_older_chromadb()
    if working_version:
        print(f"\nUpdate your requirements.txt to use: chromadb=={working_version}")
    else:
        print("\nNo compatible version found. Check your working app's exact chromadb version.")