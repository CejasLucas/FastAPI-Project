from uuid import UUID
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import APIRouter, Depends, HTTPException

from app.infrastructure.database.session import get_session
from app.infrastructure.repositories.brand_repository import SqlAlchemyBrandRepository
router = APIRouter(prefix="/brands", tags=["Brands"])



@router.get("/")
async def get_brands(
    db: AsyncSession = Depends(get_session)
):
    repo = SqlAlchemyBrandRepository(db)

    return await repo.get_all()


@router.get("/{brand_id}")
async def get_brand(
        brand_id: UUID,
        db: AsyncSession = Depends(get_session)
):
    repo = SqlAlchemyBrandRepository(db)

    brand = await repo.get_by_id(brand_id)

    if brand is None:
        raise HTTPException(status_code=404, detail="Brand not found")

    return brand