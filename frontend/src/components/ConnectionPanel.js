import React, { useState } from 'react';

const ConnectionPanel = ({ status, onConnect, onRefresh }) => {
  const [config, setConfig] = useState({
    host: 'localhost',
    port: 8001,
    is_remote: false
  });
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  const handleConnect = async (e) => {
    e.preventDefault();
    setLoading(true);
    setError('');
    
    try {
      await onConnect(config);
    } catch (err) {
      setError(err.response?.data?.detail || 'Connection failed');
    } finally {
      setLoading(false);
    }
  };

  const getStatusColor = () => {
    switch (status) {
      case 'connected': return '#28a745';
      case 'disconnected': return '#dc3545';
      default: return '#ffc107';
    }
  };

  return (
    <div className="card">
      <h2>Connection Status</h2>
      <div style={{ display: 'flex', alignItems: 'center', gap: '10px', marginBottom: '20px' }}>
        <div 
          style={{
            width: '12px',
            height: '12px',
            borderRadius: '50%',
            backgroundColor: getStatusColor()
          }}
        />
        <span style={{ textTransform: 'capitalize', fontWeight: 'bold' }}>
          {status}
        </span>
        {status === 'connected' && (
          <button 
            className="btn btn-secondary" 
            onClick={onRefresh}
            style={{ marginLeft: 'auto' }}
          >
            Refresh
          </button>
        )}
      </div>

      {status !== 'connected' && (
        <form onSubmit={handleConnect}>
          <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '15px', marginBottom: '15px' }}>
            <div>
              <label>Host:</label>
              <input
                type="text"
                value={config.host}
                onChange={(e) => setConfig({...config, host: e.target.value})}
                style={{ width: '100%', padding: '8px', marginTop: '5px' }}
              />
            </div>
            <div>
              <label>Port:</label>
              <input
                type="number"
                value={config.port}
                onChange={(e) => setConfig({...config, port: parseInt(e.target.value)})}
                style={{ width: '100%', padding: '8px', marginTop: '5px' }}
              />
            </div>
          </div>
          
          <div style={{ marginBottom: '15px' }}>
            <label>
              <input
                type="checkbox"
                checked={config.is_remote}
                onChange={(e) => setConfig({...config, is_remote: e.target.checked})}
                style={{ marginRight: '8px' }}
              />
              Remote Connection
            </label>
          </div>

          {error && (
            <div style={{ color: '#dc3545', marginBottom: '15px' }}>
              {error}
            </div>
          )}

          <button 
            type="submit" 
            className="btn btn-primary"
            disabled={loading}
          >
            {loading ? 'Connecting...' : 'Connect'}
          </button>
        </form>
      )}
    </div>
  );
};

export default ConnectionPanel;