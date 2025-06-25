import pkg_resources
import sys

def check_chromadb_version():
    """Check the installed version of chromadb"""
    try:
        version = pkg_resources.get_distribution("chromadb").version
        print(f"Installed chromadb version: {version}")
        
        # Print Python version
        print(f"Python version: {sys.version}")
        
        # Try to import and print client version
        import chromadb
        print(f"chromadb.__version__: {chromadb.__version__}")
        
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    check_chromadb_version()