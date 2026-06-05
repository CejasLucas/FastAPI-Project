from uuid import UUID
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import APIRouter, Depends, HTTPException

from app.infrastructure.database.session import get_session
from app.infrastructure.repositories.product_repository import SqlAlchemyProductRepository

router = APIRouter(prefix="/products", tags=["Products"])


@router.get("/")
async def get_products(
    db: AsyncSession = Depends(get_session)
):
    repo = SqlAlchemyProductRepository(db)

    return await repo.get_all()


@router.get("/{product_id}")
async def get_product(
    product_id: UUID,
    db: AsyncSession = Depends(get_session)
):
    repo = SqlAlchemyProductRepository(db)

    product = await repo.get_by_id(product_id)

    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")

    return product