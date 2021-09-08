from fastapi import APIRouter

from app.api.v1 import products, products_async

api_router = APIRouter()
api_router.include_router(products.router, prefix="/products", tags=["products"])
api_router.include_router(
    products_async.router, prefix="/products_async", tags=["async", "products"]
)
