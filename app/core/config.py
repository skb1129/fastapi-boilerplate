import os
import secrets

API_V1_STR: str = os.getenv("API_V1_STR", "/api/v1")
PROJECT_NAME: str = os.getenv("PROJECT_NAME", "FastAPI")
SECRET_KEY: str = os.getenv("SECRET_KEY", secrets.token_urlsafe(32))
SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "postgresql://localhost:5432/fastapi_db")
