#!/usr/bin/env python
# backend/test_backend_connection.py

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.services.chroma_service import chroma_service
from app.models.schemas import ConnectionConfig

def test_backend_connection():
    """Test if the backend can connect to ChromaDB"""
    config = ConnectionConfig(
        host="aipg.dudelabz.com",
        port=8000,
        is_remote=True,
        tenant="",
        database=""
    )
    
    try:
        print("Attempting to connect to ChromaDB...")
        chroma_service.connect(config)
        print("Connection successful!")
        
        print("\nListing collections:")
        collections = chroma_service.get_collections()
        for collection in collections:
            print(f"- {collection.name} ({collection.count} documents)")
        
        print("\nConnection test completed successfully!")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    test_backend_connection()