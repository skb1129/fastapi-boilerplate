from typing import Optional
from sqlalchemy.sql.expression import table
from sqlmodel import SQLModel, Field


class ProductBase(SQLModel):
    name: Optional[str]
    price: Optional[float]


class Product(ProductBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)


class ProductCreate(SQLModel):
    name: str
    price: float


class ProductUpdate(ProductBase):
    id: int


class ProductResponse(SQLModel):
    id: str
    name: str
    price: float
