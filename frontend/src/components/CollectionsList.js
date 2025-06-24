import React from 'react';

const CollectionsList = ({ collections, selectedCollection, onSelectCollection }) => {
  return (
    <div className="card">
      <h2>Collections ({collections.length})</h2>
      
      {collections.length === 0 ? (
        <p style={{ color: '#666', fontStyle: 'italic' }}>No collections found</p>
      ) : (
        <div style={{ display: 'grid', gap: '10px' }}>
          {collections.map((collection) => (
            <div
              key={collection.name}
              onClick={() => onSelectCollection(collection)}
              style={{
                padding: '15px',
                border: selectedCollection?.name === collection.name ? '2px solid #007bff' : '1px solid #ddd',
                borderRadius: '6px',
                cursor: 'pointer',
                backgroundColor: selectedCollection?.name === collection.name ? '#f8f9fa' : 'white',
                transition: 'all 0.2s'
              }}
            >
              <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
                <h3 style={{ margin: 0, color: '#333' }}>{collection.name}</h3>
                <span style={{ 
                  backgroundColor: '#007bff', 
                  color: 'white', 
                  padding: '4px 8px', 
                  borderRadius: '12px', 
                  fontSize: '12px' 
                }}>
                  {collection.count} docs
                </span>
              </div>
              
              {collection.metadata && Object.keys(collection.metadata).length > 0 && (
                <div style={{ marginTop: '10px', fontSize: '14px', color: '#666' }}>
                  <strong>Metadata:</strong>
                  <div style={{ marginTop: '5px' }}>
                    {Object.entries(collection.metadata).map(([key, value]) => (
                      <div key={key} style={{ marginLeft: '10px' }}>
                        <code>{key}: {JSON.stringify(value)}</code>
                      </div>
                    ))}
                  </div>
                </div>
              )}
            </div>
          ))}
        </div>
      )}
    </div>
  );
};

export default CollectionsList;