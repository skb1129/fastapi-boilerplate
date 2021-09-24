from typing import Dict
from fastapi.testclient import TestClient
from app.core import settings
from sqlmodel import Session


def test_create_product(client: TestClient, random_product: Dict[str, str]) -> None:
    response = client.post(f"{settings.API_V1_STR}/products", json=random_product)
    product = response.json()
    assert response.status_code == 200
    assert product.get("name") == random_product.get("name")
    assert product.get("price") == random_product.get("price")
