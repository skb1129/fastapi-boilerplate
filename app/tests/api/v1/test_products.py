from typing import Dict

from fastapi.testclient import TestClient

from app.core import settings


def test_create_product(client: TestClient, random_product: Dict[str, str]) -> None:
    response = client.post(f"{settings.API_V1_STR}/products", json=random_product)
    product = response.json()
    assert response.status_code == 200
    assert product.get("name") == random_product.get("name")
    assert product.get("price") == random_product.get("price")


def test_read_products(client: TestClient) -> None:
    response = client.get(f"{settings.API_V1_STR}/products")
    products = response.json()
    assert response.status_code == 200
    assert len(products) > 0


def test_update_product(client: TestClient, random_product: Dict[str, str]) -> None:
    random_product["price"] = 100
    response = client.put(f"{settings.API_V1_STR}/products", json=random_product)
    product = response.json()
    assert response.status_code == 200
    assert product.get("price") == random_product.get("price")


def test_delete_product(client: TestClient, random_product: Dict[str, str]) -> None:
    response = client.delete(f"{settings.API_V1_STR}/products?id={random_product.get('id')}")
    message = response.json()
    assert response.status_code == 200
    assert "message" in message
