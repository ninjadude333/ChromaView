import subprocess
import sys

def setup_compatible_environment():
    """Set up a compatible environment for testing"""
    print("Setting up a compatible environment for testing...")
    
    # Create a new virtual environment
    subprocess.run([sys.executable, "-m", "venv", "test_env"], check=True)
    
    # Determine the pip and python commands for the new environment
    if sys.platform == "win32":
        pip_cmd = ".\\test_env\\Scripts\\pip"
        python_cmd = ".\\test_env\\Scripts\\python"
    else:
        pip_cmd = "./test_env/bin/pip"
        python_cmd = "./test_env/bin/python"
    
    # Install compatible versions
    print("Installing compatible versions of packages...")
    subprocess.run([pip_cmd, "install", "numpy<2.0.0"], check=True)
    subprocess.run([pip_cmd, "install", "chromadb==0.4.15"], check=True)
    subprocess.run([pip_cmd, "install", "requests"], check=True)
    
    # Create a test script
    test_script = """
import chromadb
from chromadb import HttpClient
import requests

def test_connection():
    host = "aipg.dudelabz.com"
    port = 8000
    
    print(f"Using chromadb version: {chromadb.__version__}")
    print(f"Testing connection to ChromaDB at {host}:{port}")
    
    # First check if server is reachable
    try:
        response = requests.get(f"http://{host}:{port}/api/v2/heartbeat")
        print(f"Server heartbeat: {response.status_code} - {response.text}")
    except Exception as e:
        print(f"Server not reachable: {str(e)}")
        return
    
    # Try to connect with chromadb client
    try:
        client = HttpClient(host=host, port=port)
        print("Client created successfully")
        
        # Try heartbeat
        heartbeat = client.heartbeat()
        print(f"Client heartbeat: {heartbeat}")
        
        # Try to list collections
        collections = client.list_collections()
        print(f"Collections: {[c.name for c in collections]}")
        
        # Try to get or create vendor_emails collection
        collection = client.get_or_create_collection(name="vendor_emails")
        count = collection.count()
        print(f"vendor_emails collection count: {count}")
        
    except Exception as e:
        print(f"Connection error: {str(e)}")

if __name__ == "__main__":
    test_connection()
"""
    
    with open("test_env_script.py", "w") as f:
        f.write(test_script)
    
    # Run the test script
    print("\nRunning test script with compatible environment...")
    subprocess.run([python_cmd, "test_env_script.py"])

if __name__ == "__main__":
    setup_compatible_environment()