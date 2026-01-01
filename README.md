# Sentiment Scope 📊

> A production-ready microservice for real-time sentiment analysis.

![FastAPI](https://img.shields.io/badge/FastAPI-0.100%2B-009688)
![Docker](https://img.shields.io/badge/Docker-Ready-blue)
![License](https://img.shields.io/badge/license-MIT-green)

Sentiment Scope is a high-performance REST API built with FastAPI that provides instant sentiment analysis for text data. It uses Natural Language Processing (NLP) to determine polarity and subjectivity, making it perfect for integrating into larger applications or data pipelines.

## 🚀 Features

*   **FastAPI Powered**: Modern, fast (high-performance), web framework for building APIs with Python 3.9+.
*   **Dockerized**: Ready for deployment with a production-grade `Dockerfile`.
*   **Detailed Metrics**: Returns both polarity (positive/negative) and subjectivity (fact/opinion) scores.
*   **Health Checks**: Built-in `/health` endpoint for monitoring.

## 🛠️ Installation

### Local Development

1.  **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/sentiment_scope.git
    cd sentiment_scope
    ```

2.  **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    python -m textblob.download_corpora
    ```

3.  **Run the Server**:
    ```bash
    python main.py
    # or
    uvicorn main:app --reload
    ```

### Docker Deployment

1.  **Build the Image**:
    ```bash
    docker build -t sentiment-scope .
    ```

2.  **Run the Container**:
    ```bash
    docker run -p 8000:8000 sentiment-scope
    ```

## 📖 API Documentation

Once the server is running, visit `http://localhost:8000/docs` for the interactive Swagger UI.

### Endpoints

*   `POST /analyze`: Analyze text sentiment.
    *   Body: `{"text": "I love this product!"}`
*   `GET /health`: Check API status.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
