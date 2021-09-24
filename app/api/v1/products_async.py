from typing import List, Any
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from app import schemas, crud
from app.api.deps import get_db_async

router = APIRouter()


@router.get("", response_model=List[schemas.ProductResponse])
async def read_products(
    db: AsyncSession = Depends(get_db_async), skip: int = 0, limit: int = 100
) -> Any:
    """
    Retrieve all products.
    """
    products = await crud.async_product.get_multi(db, skip=skip, limit=limit)
    return products


@router.post("", response_model=schemas.ProductResponse)
async def create_product(
    *, db: AsyncSession = Depends(get_db_async), product_in: schemas.ProductCreate
) -> Any:
    """
    Create new products.
    """
    product = await crud.async_product.create(db, obj_in=product_in)
    return product


@router.put("", response_model=schemas.ProductResponse)
async def update_product(
    *, db: AsyncSession = Depends(get_db_async), product_in: schemas.ProductUpdate
) -> Any:
    """
    Update existing products.
    """
    product = await crud.async_product.get(db, model_id=product_in.id)
    if not product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="The product with this ID does not exist in the system.",
        )
    product = await crud.async_product.update(db, db_obj=product, obj_in=product_in)
    return product


@router.delete("", response_model=schemas.Message)
async def delete_product(*, db: AsyncSession = Depends(get_db_async), id: int) -> Any:
    """
    Delete existing product.
    """
    product = await crud.async_product.get(db, model_id=id)
    if not product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="The product with this ID does not exist in the system.",
        )
    await crud.async_product.remove(db, model_id=product.id)
    return {"message": f"Product with ID = {id} deleted."}
