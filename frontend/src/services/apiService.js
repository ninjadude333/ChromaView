import axios from 'axios';

const API_BASE_URL = process.env.REACT_APP_API_URL || 'http://localhost:8000';

const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

export const apiService = {
  // Connection endpoints
  connect: async (config) => {
    const response = await api.post('/api/connections/connect', config);
    return response.data;
  },

  getConnectionStatus: async () => {
    const response = await api.get('/api/connections/status');
    return response.data;
  },

  // Collections endpoints
  getCollections: async () => {
    const response = await api.get('/api/collections/');
    return response.data;
  },

  getCollectionInfo: async (collectionName) => {
    const response = await api.get(`/api/collections/${collectionName}/info`);
    return response.data;
  },

  // Documents endpoints
  getDocuments: async (collectionName, limit = 50, offset = 0) => {
    const response = await api.get(`/api/documents/${collectionName}`, {
      params: { limit, offset }
    });
    return response.data;
  },

  searchDocuments: async (collectionName, query, limit = 10) => {
    const response = await api.post(`/api/documents/${collectionName}/search`, {
      query,
      collection_name: collectionName,
      limit
    });
    return response.data;
  },
};