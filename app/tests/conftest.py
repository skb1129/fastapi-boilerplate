from typing import Dict, Generator

import pytest

from fastapi.testclient import TestClient

from app.database.session import create_session, global_init
from app.main import app


@pytest.fixture(scope="session")
def db() -> Generator:
    global_init()
    yield create_session()


@pytest.fixture(scope="module")
def client() -> Generator:
    with TestClient(app) as c:
        yield c


@pytest.fixture(scope="module")
def random_product() -> Dict[str, str]:
    return {
        "id": 1,
        "name": "Test Product",
        "price": 80,
    }
