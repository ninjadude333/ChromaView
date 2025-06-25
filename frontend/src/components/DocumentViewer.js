import React, { useState, useEffect } from 'react';
import { apiService } from '../services/apiService';

const DocumentViewer = ({ collection }) => {
  const [documents, setDocuments] = useState([]);
  const [loading, setLoading] = useState(false);
  const [searchQuery, setSearchQuery] = useState('');
  const [searchMode, setSearchMode] = useState(false);
  const [currentPage, setCurrentPage] = useState(0);
  const [selectedDoc, setSelectedDoc] = useState(null);

  const pageSize = 20;

  useEffect(() => {
    loadDocuments();
  }, [collection, currentPage]);

  const loadDocuments = async () => {
    setLoading(true);
    try {
      const data = await apiService.getDocuments(
        collection.name, 
        pageSize, 
        currentPage * pageSize
      );
      setDocuments(data.documents);
    } catch (error) {
      console.error('Failed to load documents:', error);
    } finally {
      setLoading(false);
    }
  };

  const handleSearch = async (e) => {
    e.preventDefault();
    if (!searchQuery.trim()) return;
    
    setLoading(true);
    setSearchMode(true);
    try {
      const data = await apiService.searchDocuments(collection.name, searchQuery, 20);
      setDocuments(data.documents);
    } catch (error) {
      console.error('Search failed:', error);
    } finally {
      setLoading(false);
    }
  };

  const clearSearch = () => {
    setSearchQuery('');
    setSearchMode(false);
    setCurrentPage(0);
    loadDocuments();
  };

  const truncateText = (text, maxLength = 200) => {
    if (!text || text.length <= maxLength) return text;
    return text.substring(0, maxLength) + '...';
  };

  return (
    <div className="card">
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '20px' }}>
        <h2>Documents - {collection.name}</h2>
        <div style={{ fontSize: '14px', color: '#666' }}>
          {collection.count} total documents
        </div>
      </div>

      {/* Search Bar */}
      <form onSubmit={handleSearch} style={{ marginBottom: '20px' }}>
        <div style={{ display: 'flex', gap: '10px' }}>
          <input
            type="text"
            placeholder="Search documents..."
            value={searchQuery}
            onChange={(e) => setSearchQuery(e.target.value)}
            style={{ 
              flex: 1, 
              padding: '10px', 
              border: '1px solid #ddd', 
              borderRadius: '4px' 
            }}
          />
          <button type="submit" className="btn btn-primary" disabled={loading}>
            Search
          </button>
          {searchMode && (
            <button type="button" className="btn btn-secondary" onClick={clearSearch}>
              Clear
            </button>
          )}
        </div>
      </form>

      {/* Documents List */}
      {loading ? (
        <div style={{ textAlign: 'center', padding: '40px' }}>Loading...</div>
      ) : (
        <>
          <div style={{ display: 'grid', gap: '15px' }}>
            {documents.map((doc, index) => (
              <div
                key={doc.id}
                style={{
                  border: '1px solid #eee',
                  borderRadius: '6px',
                  padding: '15px',
                  backgroundColor: '#fafafa'
                }}
              >
                <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start', marginBottom: '10px' }}>
                  <div style={{ fontSize: '12px', color: '#666', fontFamily: 'monospace' }}>
                    ID: {doc.id}
                  </div>
                  {doc.distance !== undefined && doc.distance !== null && (
                    <div style={{ fontSize: '12px', color: '#007bff' }}>
                      Distance: {doc.distance.toFixed(4)}
                    </div>
                  )}
                </div>

                {doc.document && (
                  <div style={{ marginBottom: '10px' }}>
                    <div style={{ fontSize: '14px', lineHeight: '1.5' }}>
                      {truncateText(doc.document)}
                    </div>
                    {doc.document.length > 200 && (
                      <button
                        onClick={() => setSelectedDoc(doc)}
                        style={{ 
                          marginTop: '5px', 
                          background: 'none', 
                          border: 'none', 
                          color: '#007bff', 
                          cursor: 'pointer',
                          fontSize: '12px'
                        }}
                      >
                        View Full Document
                      </button>
                    )}
                  </div>
                )}

                {doc.metadata && Object.keys(doc.metadata).length > 0 && (
                  <div style={{ fontSize: '12px', color: '#666' }}>
                    <strong>Metadata:</strong>
                    <div style={{ marginTop: '5px', fontFamily: 'monospace' }}>
                      {Object.entries(doc.metadata).map(([key, value]) => (
                        <div key={key}>
                          {key}: {JSON.stringify(value)}
                        </div>
                      ))}
                    </div>
                  </div>
                )}
              </div>
            ))}
          </div>

          {/* Pagination */}
          {!searchMode && (
            <div style={{ display: 'flex', justifyContent: 'center', gap: '10px', marginTop: '20px' }}>
              <button
                className="btn btn-secondary"
                onClick={() => setCurrentPage(Math.max(0, currentPage - 1))}
                disabled={currentPage === 0}
              >
                Previous
              </button>
              <span style={{ padding: '10px', alignSelf: 'center' }}>
                Page {currentPage + 1}
              </span>
              <button
                className="btn btn-secondary"
                onClick={() => setCurrentPage(currentPage + 1)}
                disabled={documents.length < pageSize}
              >
                Next
              </button>
            </div>
          )}
        </>
      )}

      {/* Document Modal */}
      {selectedDoc && (
        <div style={{
          position: 'fixed',
          top: 0,
          left: 0,
          right: 0,
          bottom: 0,
          backgroundColor: 'rgba(0,0,0,0.5)',
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'center',
          zIndex: 1000
        }}>
          <div style={{
            backgroundColor: 'white',
            padding: '20px',
            borderRadius: '8px',
            maxWidth: '80%',
            maxHeight: '80%',
            overflow: 'auto'
          }}>
            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '15px' }}>
              <h3>Document Details</h3>
              <button
                onClick={() => setSelectedDoc(null)}
                style={{ background: 'none', border: 'none', fontSize: '20px', cursor: 'pointer' }}
              >
                ×
              </button>
            </div>
            <div style={{ fontSize: '12px', color: '#666', marginBottom: '15px', fontFamily: 'monospace' }}>
              ID: {selectedDoc.id}
            </div>
            <div style={{ lineHeight: '1.6', marginBottom: '15px' }}>
              {selectedDoc.document}
            </div>
            {selectedDoc.metadata && (
              <div style={{ fontSize: '12px', color: '#666', fontFamily: 'monospace' }}>
                <strong>Metadata:</strong>
                <pre style={{ marginTop: '5px', backgroundColor: '#f5f5f5', padding: '10px', borderRadius: '4px' }}>
                  {JSON.stringify(selectedDoc.metadata, null, 2)}
                </pre>
              </div>
            )}
          </div>
        </div>
      )}
    </div>
  );
};

export default DocumentViewer;