import requests

def test_server_reachable():
    """Test if the server is reachable using direct HTTP requests"""
    host = "aipg.dudelabz.com"
    port = 8000
    
    # Try different endpoints
    endpoints = [
        "",
        "/api/v1",
        "/api/v1/collections",
        "/api/v1/heartbeat",
        "/api/v2",
        "/api/v2/collections",
        "/api/v2/heartbeat"
    ]
    
    print(f"Testing if server at {host}:{port} is reachable")
    
    for endpoint in endpoints:
        url = f"http://{host}:{port}{endpoint}"
        try:
            print(f"\nTrying endpoint: {url}")
            response = requests.get(url, timeout=5)
            print(f"Status code: {response.status_code}")
            print(f"Response: {response.text[:200]}...")  # Show first 200 chars
        except Exception as e:
            print(f"Error: {str(e)}")
    
    print("\nIf any endpoint returned a valid response, the server is reachable.")

if __name__ == "__main__":
    test_server_reachable()