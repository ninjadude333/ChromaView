import requests
import json

def test_chroma_connection():
    """Test connection to ChromaDB and determine required fields"""
    base_url = "http://aipg.dudelabz.com:8000"
    
    # Try basic connection
    try:
        # Test heartbeat endpoint
        response = requests.get(f"{base_url}/api/v1/heartbeat")
        print(f"Heartbeat response: {response.status_code}")
        if response.status_code == 200:
            print("ChromaDB is reachable")
        
        # Try to get version info
        response = requests.get(f"{base_url}/api/v1")
        if response.status_code == 200:
            print(f"API info: {response.json()}")
        
        # Try to list collections without tenant/database
        response = requests.get(f"{base_url}/api/v1/collections")
        if response.status_code == 200:
            print("Collections accessible without tenant/database")
            print(f"Collections: {response.json()}")
        else:
            print(f"Collections error: {response.status_code} - {response.text}")
            
        # Try with default_tenant
        headers = {"X-Chroma-Tenant": "default_tenant"}
        response = requests.get(f"{base_url}/api/v1/collections", headers=headers)
        if response.status_code == 200:
            print("Collections accessible with default_tenant")
            print(f"Collections: {response.json()}")
        else:
            print(f"default_tenant error: {response.status_code} - {response.text}")
            
        # Try with both default_tenant and default_database
        headers = {
            "X-Chroma-Tenant": "default_tenant",
            "X-Chroma-Database": "default_database"
        }
        response = requests.get(f"{base_url}/api/v1/collections", headers=headers)
        if response.status_code == 200:
            print("Collections accessible with default_tenant and default_database")
            print(f"Collections: {response.json()}")
        else:
            print(f"default_tenant+database error: {response.status_code} - {response.text}")
            
    except Exception as e:
        print(f"Error connecting to ChromaDB: {str(e)}")
        
    print("\nConnection recommendation:")
    print("Host: aipg.dudelabz.com")
    print("Port: 8000")
    print("Remote Connection: True")
    print("Tenant: Try with and without 'default_tenant'")
    print("Database: Try with and without 'default_database'")

if __name__ == "__main__":
    test_chroma_connection()