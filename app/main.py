import uvicorn
from fastapi import FastAPI
from app.logging.logs import init_logging
from loguru import logger

from app.api.v1 import api_router
from app.core import settings
from app.database.session import create_db_and_tables


def create_app() -> FastAPI:
    app = FastAPI(title=settings.PROJECT_NAME)
    app.include_router(api_router, prefix=settings.API_V1_STR)
    return app


app = create_app()


@app.on_event("startup")
def startup():
    init_logging()
    logger.info("Startup")
    create_db_and_tables()


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
