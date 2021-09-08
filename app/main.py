import uvicorn

from fastapi import FastAPI

from app.api.v1 import api_router
from app.core import settings
from app.database.session import global_init


def create_app() -> FastAPI:
    app = FastAPI(title=settings.PROJECT_NAME)
    global_init()
    app.include_router(api_router, prefix=settings.API_V1_STR)
    return app


app = create_app()

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
