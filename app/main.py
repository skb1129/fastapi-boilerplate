import uvicorn

from fastapi import FastAPI

from app.api.v1 import api_router
from app.core import config

app = FastAPI(title=config.PROJECT_NAME)

app.include_router(api_router, prefix=config.API_V1_STR)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
