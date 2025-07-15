#!/usr/bin/env python3
import os
import argparse
import chromadb
from dotenv import load_dotenv

def main():
    load_dotenv()
    
    parser = argparse.ArgumentParser()
    parser.add_argument('--list_collections', action='store_true')
    parser.add_argument('--read_collection', type=str)
    parser.add_argument('--detailed', action='store_true')
    args = parser.parse_args()
    
    # Connect to ChromaDB
    if os.getenv('USE_REMOTE', 'false').lower() == 'true':
        client = chromadb.HttpClient(
            host=os.getenv('REMOTE_HOST'),
            port=int(os.getenv('REMOTE_PORT'))
        )
    else:
        client = chromadb.PersistentClient(path=os.getenv('PERSIST_DIR'))
    
    # List collections
    if args.list_collections:
        collections = client.list_collections()
        print(f"Collections ({len(collections)}):")
        for col in collections:
            print(f"  - {col.name}")
    
    # Read collection
    if args.read_collection:
        try:
            collection = client.get_collection(args.read_collection)
            count = collection.count()
            
            print(f"Collection: {args.read_collection}")
            print(f"Documents: {count}")
            
            if args.detailed:
                all_data = collection.get()
                for i, doc in enumerate(all_data['documents']):
                    print(f"\nDocument {i+1}:")
                    print(f"  Content: {doc[:200]}..." if len(doc) > 200 else f"  Content: {doc}")
                    if all_data['metadatas'][i]:
                        print(f"  Metadata: {all_data['metadatas'][i]}")
            else:
                peek = collection.peek(limit=1)
                if peek['documents']:
                    print(f"Sample document: {peek['documents'][0][:100]}...")
                    if peek['metadatas'][0]:
                        print(f"Sample metadata: {peek['metadatas'][0]}")
        except Exception as e:
            print(f"Error reading collection: {e}")

if __name__ == "__main__":
    main()