# Zad Islamic AI 🤖🕌

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/Python-3.12+-blue.svg)](https://www.python.org/)
[![.NET](https://img.shields.io/badge/.NET-8.0+-purple.svg)](https://dotnet.microsoft.com/)
[![Flutter](https://img.shields.io/badge/Flutter-3.10+-blue.svg)](https://flutter.dev/)
[![Docker](https://img.shields.io/badge/Docker-Ready-blue.svg)](https://www.docker.com/)

An intelligent Islamic AI assistant powered by Retrieval-Augmented Generation (RAG) technology, providing accurate, context-aware answers to questions about Islamic teachings, history, and practices. Built with a modern microservices architecture supporting mobile and web platforms.

## 🌟 Features

- **Intelligent Q&A**: Advanced RAG pipeline for precise Islamic knowledge retrieval
- **Multi-Platform Support**: Native mobile app (Flutter) and web API
- **Contextual Responses**: Embeddings-based semantic search using E5 models
- **Scalable Architecture**: Microservices with .NET API, Python AI engine, and vector database
- **Data-Driven**: Processed Islamic texts with cached embeddings for fast responses
- **Containerized Deployment**: Docker support for easy deployment and scaling

## 🏗️ Architecture

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Mobile App    │    │   API Server    │    │  AI RAG Engine  │
│   (Flutter)     │◄──►│   (.NET Core)   │◄──►│   (Python)      │
│                 │    │                 │    │                 │
└─────────────────┘    └─────────────────┘    └─────────────────┘
         │                       │                       │
         ▼                       ▼                       ▼
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   User Queries  │    │   REST API      │    │   Embeddings    │
│                 │    │   Endpoints     │    │   (E5 Models)   │
└─────────────────┘    └─────────────────┘    └─────────────────┘
                                                   │
                                                   ▼
                                         ┌─────────────────┐
                                         │  Vector DB      │
                                         │  (Qdrant)       │
                                         │                 │
                                         └─────────────────┘
                                                   │
                                                   ▼
                                         ┌─────────────────┐
                                         │  Islamic Texts  │
                                         │  (Processed)    │
                                         └─────────────────┘
```

### Components

- **Mobile App**: Flutter-based cross-platform application for iOS, Android, and Web
- **API Server**: .NET Core REST API handling user requests and authentication
- **AI RAG Engine**: Python FastAPI service with RAG pipeline (preprocessing, embeddings, retrieval, reranking, generation)
- **Vector Database**: Qdrant for efficient similarity search on Islamic text embeddings
- **Data Pipeline**: Processing raw Islamic texts into searchable chunks with cached embeddings

## 🛠️ Tech Stack

- **Frontend**: Flutter (Dart)
- **Backend API**: ASP.NET Core (.NET 8+)
- **AI Engine**: Python 3.12+, FastAPI, Hugging Face Transformers
- **Embeddings**: E5 Large/Small models
- **Vector DB**: Qdrant
- **Database**: SQL Server with Entity Framework Core
- **Deployment**: Docker, Docker Compose
- **AI/ML**: PyTorch, OpenAI API integration

## 🚀 Quick Start

### Prerequisites

- Docker & Docker Compose
- .NET 8.0 SDK
- Python 3.12+
- Flutter SDK (for mobile development)

### 1. Clone the Repository

```bash
git clone https://github.com/your-org/zad-islamic-ai.git
cd zad-islamic-ai
```

### 2. Environment Setup

```bash
# Copy environment files
cp apps/api-sever/appsettings.Development.json.example apps/api-sever/appsettings.Development.json
cp services/ai-rag-engine/.env.example services/ai-rag-engine/.env
```

### 3. Launch with Docker

```bash
docker-compose -f infrastructure/docker/docker-compose.yml up -d
```

This starts:
- Qdrant vector database
- AI RAG engine (Python)
- API server (.NET)
- Database migrations

### 4. Run Mobile App

```bash
cd apps/mobile_app
flutter pub get
flutter run
```

## 📖 Usage

### API Endpoints

The API server provides RESTful endpoints for Islamic Q&A:

```bash
# Ask a question
curl -X POST http://localhost:5000/api/questions/ask \
  -H "Content-Type: application/json" \
  -d '{"question": "What is the significance of Ramadan?"}'
```

### Mobile App

1. Open the app on your device
2. Sign in or create an account
3. Ask questions about Islamic topics
4. View detailed answers with source references

## 🔧 Development

### AI RAG Engine Setup

```bash
cd services/ai-rag-engine
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

### API Server Setup

```bash
cd apps/api-sever
dotnet restore
dotnet run --project ZAD.API/ZAD.API.csproj
```

### Data Processing

```bash
cd services/ai-rag-engine/scripts
python process_islamic_texts.py
```

## 📊 Data Pipeline

1. **Raw Data**: Islamic texts from various sources
2. **Preprocessing**: Text cleaning, normalization, dialect handling
3. **Chunking**: Split into semantically meaningful segments
4. **Embeddings**: Generate vector representations using E5 models
5. **Indexing**: Store in Qdrant vector database
6. **Retrieval**: Semantic search for relevant context
7. **Generation**: Use retrieved context for accurate answers

## 🧪 Testing

```bash
# AI Engine tests
cd services/ai-rag-engine
pytest

# API tests
cd apps/api-sever
dotnet test

# Mobile app tests
cd apps/mobile_app
flutter test
```

## 📚 Documentation

- [API Documentation](./docs/api-documentation/)
- [Architecture Diagrams](./docs/architecture-diagrams/)
- [AI Design](./docs/ai-design.md)
- [Deployment Guide](./docs/deployment-guide.md)

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guide](./CONTRIBUTING.md) for details.

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](./LICENSE) file for details.

## 🙏 Acknowledgments

- Islamic scholars and organizations for providing source texts
- Open-source community for AI/ML tools and frameworks
- Contributors and maintainers

## 📞 Support

For questions or support:
- Open an issue on GitHub
- Contact the maintainers
- Check the documentation

---

*Built with ❤️ for the Muslim community*