from typing import Dict
from fastapi.testclient import TestClient
from sqlmodel import Session
from app.core import settings
from app.models.product import Product


def test_create_product(client: TestClient, random_product: Dict[str, str]) -> None:
    response = client.post(f"{settings.API_V1_STR}/products", json=random_product)
    product = response.json()
    assert response.status_code == 200
    assert product.get("name") == random_product.get("name")
    assert product.get("price") == random_product.get("price")


def test_read_products(client: TestClient, session: Session, random_product: Dict[str, str]) -> None:
    productIN1 = Product(name=random_product.get("name"), price=random_product.get("price"))
    productIN2 = Product(name="Product2", price=random_product.get("price"))
    session.add(productIN1)
    session.add(productIN2)
    session.commit()
    session.refresh(productIN1)
    session.refresh(productIN2)
    response = client.get(f"{settings.API_V1_STR}/products")
    products = response.json()
    assert response.status_code == 200
    assert len(products) > 0
