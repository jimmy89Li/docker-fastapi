# FastAPI Project

This is a FastAPI-based project.

## Features

- High-performance API built with Python and FastAPI.
- Asynchronous support for better scalability.
- Easy-to-use and well-documented endpoints.

## Requirements

- Python 3.7+
- FastAPI
- Uvicorn

## Installation

1. Clone the repository:

```bash
git clone https://github.com/jimmy89Li/docker-fastapi
cd docker-fastapi
```

2. Create a virtual environment and activate it:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

## Running the Application

Start the development server:

```bash
uvicorn main:app --reload
```

The API will be available at `http://127.0.0.1:8000`.

## License

This project is licensed under the MIT License.
