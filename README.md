# FastAPI Boilerplate Project

A modern, production-ready FastAPI boilerplate application featuring a **Feature/Module-based Architecture**, environment configuration, and Docker containerization support.

---

## Table of Contents
1. [Overview](#1-overview)
2. [Prerequisites](#2-prerequisites)
3. [Installation & Setup](#3-installation--setup)
   - [Local Environment Setup](#local-environment-setup)
   - [Environment Configuration](#environment-configuration)
4. [Project Structure](#4-project-structure)
5. [Running the Application](#5-running-the-application)
   - [Local Development Mode](#local-development-mode)
   - [Docker / Docker Compose Mode](#docker--docker-compose-mode)
6. [API Endpoints & Swagger Documentation](#6-api-endpoints--swagger-documentation)
7. [Adding a New Feature/Module](#7-adding-a-new-featuremodule)
8. [Advanced Topics](#8-advanced-topics)
   - [Database Connection](#database-connection)
   - [JWT Authentication](#jwt-authentication)

---

## 1. Overview

**FastAPI** is a modern, fast (high-performance), web framework for building APIs with Python 3.8+ based on standard Python type hints.

Key features of this boilerplate:
- 🚀 **High Performance**: Built on top of Starlette and Pydantic.
- 📄 **Interactive API Docs**: Auto-generated Swagger UI and ReDoc.
- 🔒 **Data Validation**: Built-in validation using Pydantic.
- 🧱 **Scalable Architecture**: Structured using a Feature/Module-based layout.
- 🐳 **Docker Ready**: Pre-configured `Dockerfile` and `docker-compose.yml` for containerization.

---

## 2. Prerequisites

Make sure you have the following installed on your system:
- **Python 3.11+**
- **pip** (Python package installer)
- **Docker** and **Docker Compose** (Optional, for containerized environments)

---

## 3. Installation & Setup

### Local Environment Setup

1. **Clone the repository** (or navigate to your project directory):
   ```bash
   cd <project_directory>
   ```

2. **Create a virtual environment**:
   It is highly recommended to use a virtual environment to isolate project dependencies.
   - **Windows (PowerShell)**:
     ```powershell
     python -m venv venv
     .\venv\Scripts\Activate.ps1
     ```
   - **macOS / Linux**:
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

### Environment Configuration

1. **Set up `.env`**:
   The project requires a `.env` file at the root directory for configuration. Make sure you have a `.env` file containing:
   ```env
   APP_NAME=FastAPI App
   DEBUG=true
   DB_HOST=localhost
   DB_USER=root
   DB_PASSWORD=123456
   DB_NAME=test_db
   JWT_SECRET=supersecret
   ```

2. **Security Warning**:
   Do **NOT** commit your `.env` file to version control systems like Git. The `.gitignore` file should always contain `.env` to prevent accidental commits.

---

## 4. Project Structure

The project follows a **Feature/Module-based Architecture**, grouping logic by domains/features instead of technical layers (like MVC). This makes scale-up cleaner and keeps code relevant to a specific domain together.

```css
FAST_API/
 ┣ src/
 ┃ ┣ config/           # Global configuration files (e.g., db connection, environment settings)
 ┃ ┃ ┗ mysql.py        # Database setup and connection engine
 ┃ ┣ middleware/       # Custom middleware (auth, logging, CORS, security validation)
 ┃ ┃ ┗ check_role.py   # Role-based access control middleware
 ┃ ┣ user/             # User Feature Module
 ┃ ┃ ┣ user_controller.py   # Processes requests and returns responses (no business logic)
 ┃ ┃ ┣ user_router.py       # Configures user-specific URL routes
 ┃ ┃ ┣ user_model.py        # Database schemas and models
 ┃ ┃ ┣ user_utils.py        # Utility helper functions specific to users
 ┃ ┃ ┗ user_dto.py          # Data Transfer Objects / Pydantic validation schemas
 ┃ ┣ utils/            # Shared / General Utilities Module
 ┃ ┃ ┣ utils_controller.py  # Shared controller methods
 ┃ ┃ ┗ utils_router.py      # Route configuration for general utilities
 ┣ .env                # Local environment variables
 ┣ Dockerfile          # Multi-stage build image instructions
 ┣ docker-compose.yml  # Docker Compose orchestration configuration
 ┣ main.py             # App entrypoint & Router registration
 ┗ requirements.txt    # List of requirements/dependencies
```

---

## 5. Running the Application

### Local Development Mode

To run the application locally with hot-reloading (changes will auto-reload the server):
```bash
fastapi dev main.py
```
Alternatively, you can run using `uvicorn`:
```bash
uvicorn main:app --reload --host 127.0.0.1 --port 8000
```

### Docker / Docker Compose Mode

To build and run the application inside a Docker container:
```bash
# Build and run in the background
docker compose up --build -d

# Check running container logs
docker compose logs -f
```
The server will start up inside Docker and listen on port `8000`.

---

## 6. API Endpoints & Swagger Documentation

Once the server is running, the following endpoints are available:

- **Root API**: [http://127.0.0.1:8000/](http://127.0.0.1:8000/) - Returns `{"message": "Hello World"}`
- **Get Users API**: [http://127.0.0.1:8000/users](http://127.0.0.1:8000/users) - Returns mock user details.
- **Interactive Swagger UI**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) (Allows you to view, test, and document all APIs in real-time).
- **Alternative ReDoc Docs**: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc).

---

## 7. Adding a New Feature/Module

To add a new feature (e.g., `product`):

1. **Create the folder structure**:
   Create a new directory `src/product/` with the following files:
   - `product_router.py`
   - `product_controller.py`
   - `product_model.py` (if db required)

2. **Define routes and handlers**:
   * `src/product/product_controller.py`:
     ```python
     def get_products():
         return [{"id": 1, "name": "Laptop"}, {"id": 2, "name": "Smartphone"}]
     ```
   * `src/product/product_router.py`:
     ```python
     from fastapi import APIRouter
     from src.product.product_controller import get_products

     router = APIRouter()
     router.get("/products")(get_products)
     ```

3. **Register the router in `main.py`**:
   ```python
   # main.py
   ...
   from src.product.product_router import router as product_router
   
   app.include_router(product_router)
   ```

---

## 8. Advanced Topics

### Database Connection

This template supports database connections like MySQL/PostgreSQL using SQLAlchemy or SQLModel.
First, install required dependencies:
```bash
pip install sqlalchemy pymysql
```

Set up your engine in `src/config/mysql.py`:
```python
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = f"mysql+pymysql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}/{os.getenv('DB_NAME')}"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
```

### JWT Authentication

For securing APIs, install Python-Jose and Passlib for hashing and token generation:
```bash
pip install python-jose passlib[bcrypt]
```
Use middleware or dependencies to check the `Authorization: Bearer <token>` header on protected endpoints.
