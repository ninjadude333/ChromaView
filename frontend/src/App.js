import React, { useState, useEffect } from 'react';
import ConnectionPanel from './components/ConnectionPanel';
import CollectionsList from './components/CollectionsList';
import DocumentViewer from './components/DocumentViewer';
import { apiService } from './services/apiService';

function App() {
  const [connectionStatus, setConnectionStatus] = useState('disconnected');
  const [collections, setCollections] = useState([]);
  const [selectedCollection, setSelectedCollection] = useState(null);

  useEffect(() => {
    checkConnectionStatus();
  }, []);

  const checkConnectionStatus = async () => {
    try {
      const status = await apiService.getConnectionStatus();
      setConnectionStatus(status.status);
      if (status.status === 'connected') {
        loadCollections();
      }
    } catch (error) {
      setConnectionStatus('disconnected');
    }
  };

  const loadCollections = async () => {
    try {
      const data = await apiService.getCollections();
      setCollections(data.collections);
    } catch (error) {
      console.error('Failed to load collections:', error);
    }
  };

  const handleConnect = async (config) => {
    try {
      await apiService.connect(config);
      setConnectionStatus('connected');
      loadCollections();
    } catch (error) {
      console.error('Connection failed:', error);
      throw error;
    }
  };

  const handleRefresh = () => {
    if (connectionStatus === 'connected') {
      loadCollections();
    }
  };

  return (
    <div className="container">
      <header style={{ marginBottom: '30px' }}>
        <h1>ChromaView 🔍</h1>
        <p>ChromaDB Visualizer and Explorer</p>
      </header>

      <ConnectionPanel 
        status={connectionStatus}
        onConnect={handleConnect}
        onRefresh={handleRefresh}
      />

      {connectionStatus === 'connected' && (
        <>
          <CollectionsList 
            collections={collections}
            selectedCollection={selectedCollection}
            onSelectCollection={setSelectedCollection}
          />

          {selectedCollection && (
            <DocumentViewer 
              collection={selectedCollection}
            />
          )}
        </>
      )}
    </div>
  );
}

export default App;