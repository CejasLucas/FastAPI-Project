from uuid import UUID
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import APIRouter, Depends, HTTPException

from app.domain.entities.brand import Brand
from app.api.dtos.brand_dto import BrandCreateDTO, BrandUpdateDTO

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

@router.post("/", status_code=201)
async def create_brand(
    body: BrandCreateDTO,
    db: AsyncSession = Depends(get_session)
):
    repo = SqlAlchemyBrandRepository(db)

    brand = Brand(
        id=None,
        **body.model_dump()
    )

    return await repo.create(brand)


@router.put("/{brand_id}")
async def update_brand(
    brand_id: UUID,
    body: BrandUpdateDTO,
    db: AsyncSession = Depends(get_session)
):
    repo = SqlAlchemyBrandRepository(db)

    existing = await repo.get_by_id(brand_id)
    if existing is None:
        raise HTTPException(status_code=404, detail="Brand not found")

    updated_data = existing.__dict__ | {
        k: v for k, v in body.model_dump().items() if v is not None
    }

    updated_brand = Brand(**updated_data)

    return await repo.update(updated_brand)


@router.delete("/{brand_id}", status_code=204)
async def delete_brand(
    brand_id: UUID,
    db: AsyncSession = Depends(get_session)
):
    repo = SqlAlchemyBrandRepository(db)

    existing = await repo.get_by_id(brand_id)
    if existing is None:
        raise HTTPException(status_code=404, detail="Brand not found")

    await repo.delete(brand_id)