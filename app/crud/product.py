from typing import Optional, List

from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.crud.asyncbase import AsyncCRUDBase
from app.models.product import Product
from app.schemas import ProductCreate, ProductUpdate


class CRUDProduct(CRUDBase[Product, ProductCreate, ProductUpdate]):
    # Declare model specific CRUD operation methods.
    pass


class AsyncCRUDProduct(AsyncCRUDBase[Product, ProductCreate, ProductUpdate]):
    # Declare model specific CRUD operation methods.
    pass


product = CRUDProduct(Product)
async_product = AsyncCRUDProduct(Product)
