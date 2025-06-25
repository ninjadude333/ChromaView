# ChromaView Connection Guide

## Connecting to aipg.dudelabz.com ChromaDB Instance

To connect to the ChromaDB instance at aipg.dudelabz.com:

1. Use the following connection settings:
   - Host: `aipg.dudelabz.com`
   - Port: `8000`
   - Remote Connection: Checked
   - Tenant: Leave empty (unless you know a specific tenant is required)
   - Database: Leave empty (unless you know a specific database is required)

2. After connecting, you should be able to see and access the `vendor_emails` collection.

## Troubleshooting

If you encounter connection issues:

1. Verify that the ChromaDB instance is running and accessible
2. Check network connectivity between your browser and the ChromaDB server
3. If you get tenant or database errors, try different values or leave them empty
4. Check the browser console and backend logs for detailed error messages

## Connection Details from Your Working Configuration

Based on your working configuration:
```yaml
vector_store:
  persist_directory: data/chroma
  collection_name: vendor_emails
  use_remote: true
  remote_host: "aipg.dudelabz.com"
  remote_port: 8000
```

The ChromaDB instance at aipg.dudelabz.com:8000 should be accessible without specifying tenant or database parameters.