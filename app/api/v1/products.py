from typing import Any, List
from fastapi import APIRouter, Depends
from sqlmodel import Session
from app.models.product import ProductResponse, ProductCreate
from app.api.deps import get_session
from app import crud

router = APIRouter()


@router.post("", response_model=ProductResponse)
def create_product(*, db: Session = Depends(get_session), product_in: ProductCreate) -> Any:
    """
    Create new products.
    """
    product = crud.product.create(db, obj_in=product_in)
    return product


@router.get("", response_model=List[ProductResponse])
def read_products(db: Session = Depends(get_session), skip: int = 0, limit: int = 100) -> Any:
    """
    Retrieve all products.
    """
    products = crud.product.get_multi(db, skip=skip, limit=limit)
    return products
