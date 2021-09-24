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


def test_update_product(client: TestClient, session: Session, random_product: Dict[str, str]) -> None:
    # Add product to the test db
    productIN = Product(name=random_product.get("name"), price=random_product.get("price"))
    session.add(productIN)
    session.commit()
    session.refresh(productIN)
    # update price and test
    random_product["price"] = 100
    response = client.put(f"{settings.API_V1_STR}/products", json=random_product)
    product = response.json()
    assert response.status_code == 200
    assert product.get("price") == random_product.get("price")
    # update with id only
    random_product.pop("name", None)
    random_product["price"] = 5000
    response = client.put(f"{settings.API_V1_STR}/products", json=random_product)
    product = response.json()
    assert response.status_code == 200
    assert product.get("price") == random_product.get("price")


def test_delete_product(client: TestClient, session: Session, random_product: Dict[str, str]) -> None:
    productIN = Product(name=random_product.get("name"), price=random_product.get("price"))
    session.add(productIN)
    session.commit()
    session.refresh(productIN)

    response = client.delete(f"{settings.API_V1_STR}/products?id={random_product.get('id')}")
    message = response.json()
    assert response.status_code == 200
    assert "message" in message
