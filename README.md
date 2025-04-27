# 📦 docker-fastapi

A minimal FastAPI project packaged with Docker, ready for quick development and
deployment.

## ✨ Features

- ⚡ High-performance asynchronous API using FastAPI and Uvicorn
- 🐳 Dockerized environment for easy setup and consistency
- 🔥 Hot reload support for development
- 🛠️ Example SQLite database (`address_book.db`) included for simple CRUD
  operations

## 🧰 Tech Stack

- Python 3.7+
- FastAPI
- Uvicorn
- SQLite
- Docker & Docker Compose

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/jimmy89Li/docker-fastapi.git
cd docker-fastapi
```

### 2. Create a virtual environment and activate it

Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the server:

```bash
uvicorn app.main:app --reload
```

The API will be available at http://127.0.0.1:8000

API documentation available at http://127.0.0.1:8000/docs

### 3. Running with Docker

Make sure Docker and Docker Compose are installed.

Start the app:

```bash
docker compose up --build
```

Access it at http://localhost:8000

### 4. Database

- The project includes a sample SQLite database: `address_book.db`
- It is mounted inside the Docker container automatically
- Suitable for simple demo/testing purposes

### 🏗️ Project Structure

```bash
.
├── app/
│   ├── main.py        # Main FastAPI app
├── address_book.db    # SQLite demo database
├── Dockerfile         # Container image definition
├── compose.yaml       # Docker Compose setup
├── requirements.txt   # Python dependencies
├── .dockerignore      # Docker ignore file
└── .gitignore         # Git ignore file
```

## License

This project is licensed under the MIT License.
