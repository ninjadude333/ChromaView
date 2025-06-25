<div align="center">
  <h1>🔍 ChromaView</h1>
  <p><strong>The Missing ChromaDB Visualizer</strong></p>
  <p>Finally, a beautiful web interface to explore, debug, and understand your vector database</p>
  
  <p>
    <a href="#quick-start">🚀 Quick Start</a> •
    <a href="#features">✨ Features</a> •
    <a href="#demo">🎥 Demo</a> •
    <a href="#contributing">🤝 Contributing</a>
  </p>
  
  <img src="https://img.shields.io/badge/ChromaDB-Compatible-blue?style=for-the-badge" alt="ChromaDB Compatible">
  <img src="https://img.shields.io/badge/Docker-Ready-2496ED?style=for-the-badge&logo=docker&logoColor=white" alt="Docker Ready">
  <img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge" alt="MIT License">
</div>

---

## 🎯 Why ChromaView?

**Ever struggled with:**
- 🤔 "What's actually in my ChromaDB?"
- 🐛 "Why isn't my similarity search working?"
- 📊 "How can I validate my embeddings?"
- 🔍 "I need to quickly browse my vector data!"

**ChromaView solves this.** It's the tool you wish existed when you started working with ChromaDB.

## ✨ Features

### 🎨 **Beautiful Interface**
- Clean, intuitive design that gets out of your way
- Responsive layout that works on any screen
- Dark/light mode support *(coming soon)*

### 🔌 **Universal Connection**
- **Local ChromaDB**: Connect to your development instances
- **Remote ChromaDB**: Production servers via HTTP
- **One-click connection** with smart defaults

### 📊 **Smart Collection Explorer**
- View all collections with rich metadata
- Document counts and embedding dimensions
- Collection health indicators

### 📄 **Powerful Document Viewer**
- Browse documents with smooth pagination
- Full-text search across your collections
- Metadata inspection with JSON formatting
- **No more blind queries!**

### 🔍 **Advanced Search**
- Semantic similarity search
- Metadata filtering
- Distance scoring visualization
- Query result ranking

### ⚡ **Developer Experience**
- **Instant refresh** - see changes immediately
- **Docker-first** - runs anywhere
- **API-ready** - integrate with your workflow

## 🚀 Quick Start

**Get ChromaView running in under 2 minutes:**

```bash
# 1. Clone and enter directory
git clone https://github.com/your-username/ChromaView.git
cd ChromaView

# 2. Start everything with Docker
docker-compose up --build

# 3. Open your browser
# 🌐 http://localhost:3000 (or your Docker host IP:3000)
```

**That's it!** ChromaView is ready to connect to any ChromaDB instance.

### 🎯 Connect to Your ChromaDB

1. **Remote ChromaDB**: Enter your host/port (e.g., `your-server.com:8000`)
2. **Local ChromaDB**: Use `localhost:8000` for local instances
3. **Docker ChromaDB**: Use your Docker host IP and port
4. **Leave tenant/database empty** for most setups
5. **Click Connect** and start exploring!

### 🔧 Supported ChromaDB Versions

- ✅ **ChromaDB 1.0.x** (Recommended)
- ✅ **ChromaDB 0.4.x** (Supported)
- ⚠️ **ChromaDB 0.3.x** (Limited support)

### 🐳 Production Deployment

```bash
# For production use
docker-compose up -d

# Access via your server IP
# http://your-server-ip:3000
```

### 🔧 Configuration

**Environment Variables:**

```bash
# Frontend API URL (adjust for your setup)
REACT_APP_API_URL=http://your-backend-host:8000

# Backend settings
PYTHONPATH=/app
RELOAD=true
```

## 🎥 Demo

> **Coming Soon**: Screenshots and video walkthrough

**What you'll see:**
- 🔌 Instant connection to ChromaDB
- 📊 Beautiful collection overview
- 📄 Document browsing with search
- 🔍 Similarity search in action

## 🏗️ Architecture

**Simple, clean, and fast:**

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   React Frontend│    │  FastAPI Backend│    │  Your ChromaDB  │
│   (Port 3000)   │◄──►│   (Port 8000)   │◄──►│  (Any Host:Port) │
│                 │    │                 │    │                 │
│ • Modern UI     │    │ • Fast API      │    │ • Your Data     │
│ • Real-time     │    │ • ChromaDB      │    │ • Collections   │
│ • Responsive    │    │   Client v1.0   │    │ • Documents     │
└─────────────────┘    └─────────────────┘    └─────────────────┘
```

## 📁 Project Structure

```
ChromaView/
├── backend/                 # FastAPI backend
│   ├── app/
│   │   ├── main.py         # FastAPI application
│   │   ├── models/         # Data models
│   │   ├── routers/        # API routes
│   │   └── services/       # Business logic
│   ├── requirements.txt
│   └── Dockerfile.dev
├── frontend/               # React frontend
│   ├── src/
│   │   ├── components/     # React components
│   │   ├── services/       # API services
│   │   └── utils/          # Utilities
│   ├── package.json
│   └── Dockerfile.dev
├── docker-compose.yml      # Development environment
├── docker-compose.prod.yml # Production environment
└── README.md
```

## 🛠️ Development

**Want to contribute? We'd love your help!**

### 🔧 Local Development

```bash
# Backend (FastAPI + ChromaDB)
cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload --host 0.0.0.0

# Frontend (React)
cd frontend
npm install && npm start

# Or use Docker for development
docker-compose up --build
```

### 🧪 Testing Connection

```bash
# Test backend API
curl http://localhost:8000/api/connections/status

# Test ChromaDB connection
curl -X POST http://localhost:8000/api/connections/connect \
  -H "Content-Type: application/json" \
  -d '{"host":"your-chromadb-host","port":8000,"is_remote":true}'
```

### 🎯 What We're Building Next

- [ ] **Advanced Query Builder** - Visual query construction
- [ ] **Collection Analytics** - Embedding quality metrics
- [ ] **Data Export** - CSV, JSON export capabilities
- [ ] **Multi-DB Support** - Connect to multiple ChromaDB instances
- [ ] **Real-time Updates** - Live data synchronization
- [ ] **Embedding Visualization** - 2D/3D vector plots

**See something missing? [Open an issue](https://github.com/your-username/ChromaView/issues) or contribute!**

## 🤝 Contributing

**ChromaView is built by the community, for the community.**

### 🌟 Ways to Contribute

- **🐛 Found a bug?** [Report it](https://github.com/your-username/ChromaView/issues)
- **💡 Have an idea?** [Share it](https://github.com/your-username/ChromaView/discussions)
- **📝 Improve docs** - Documentation PRs are always welcome
- **🎨 Design skills?** Help us make ChromaView even more beautiful
- **⚡ Performance guru?** Optimize our queries and rendering

### 🚀 Quick Contribution Guide

```bash
# 1. Fork & clone
git clone https://github.com/your-username/ChromaView.git

# 2. Create feature branch
git checkout -b feature/amazing-feature

# 3. Make changes & test
docker-compose up --build

# 4. Submit PR
git push origin feature/amazing-feature
```

**First time contributing to open source? We're here to help! 🤗**

### 🐛 Known Issues & Solutions

- **Connection fails**: Check ChromaDB version compatibility
- **Tenant errors**: Leave tenant/database fields empty
- **Network issues**: Ensure ChromaDB is accessible from Docker container
- **Port conflicts**: Adjust ports in docker-compose.yml if needed

## 🌟 Community

**Join the ChromaView community:**

- 💬 **[GitHub Discussions](https://github.com/your-username/ChromaView/discussions)** - Ask questions, share ideas
- 🐛 **[Issues](https://github.com/your-username/ChromaView/issues)** - Bug reports and feature requests
- 🐦 **[Twitter](https://twitter.com/chromaview)** - Updates and announcements
- 📧 **[Email](mailto:hello@chromaview.dev)** - Direct contact

## 🏆 Recognition

**Built with love by developers who understand the pain of debugging vector databases.**

### 🙏 Special Thanks

- **ChromaDB Team** - For building an amazing vector database
- **Early Contributors** - You know who you are! 🚀
- **Community Feedback** - Every issue and suggestion makes ChromaView better

## 📄 License

**MIT License** - Use ChromaView however you want, commercially or personally.

---

<div align="center">
  <h3>⭐ Star us on GitHub if ChromaView helps you!</h3>
  <p><strong>Made with ❤️ for the ChromaDB community</strong></p>
  
  <p>
    <a href="https://github.com/your-username/ChromaView/stargazers">⭐ Star</a> •
    <a href="https://github.com/your-username/ChromaView/fork">🍴 Fork</a> •
    <a href="https://github.com/your-username/ChromaView/issues">🐛 Issues</a> •
    <a href="https://github.com/your-username/ChromaView/discussions">💬 Discuss</a>
  </p>
</div>