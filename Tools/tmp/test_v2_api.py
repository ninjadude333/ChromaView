import requests
import json

def test_v2_api():
    """Test direct interaction with the v2 API"""
    host = "aipg.dudelabz.com"
    port = 8000
    base_url = f"http://{host}:{port}/api/v2"
    
    print(f"Testing v2 API at {base_url}")
    
    # Test heartbeat
    try:
        response = requests.get(f"{base_url}/heartbeat")
        print(f"Heartbeat: {response.status_code} - {response.text}")
    except Exception as e:
        print(f"Heartbeat error: {str(e)}")
    
    # Try to list collections
    try:
        # Try different endpoints for collections
        endpoints = [
            "/collections",
            "/list_collections",
            "/get_collections"
        ]
        
        for endpoint in endpoints:
            try:
                url = f"{base_url}{endpoint}"
                print(f"\nTrying to list collections at: {url}")
                response = requests.get(url)
                print(f"Status: {response.status_code}")
                print(f"Response: {response.text[:200]}...")
            except Exception as e:
                print(f"Error: {str(e)}")
    except Exception as e:
        print(f"Collections error: {str(e)}")

if __name__ == "__main__":
    test_v2_api()