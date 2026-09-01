from uuid import UUID
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import APIRouter, Depends

from app.api.dtos.brand_dto import BrandDTO, BrandCreateDTO, BrandUpdateDTO
from app.api.services.brand_service import BrandService

from app.infrastructure.database.session import get_session
from app.infrastructure.repositories.brand_repository import SqlAlchemyBrandRepository

router = APIRouter(prefix="/brands", tags=["Brands"])


@router.get("/", response_model=list[BrandDTO])
async def get_brands(db: AsyncSession = Depends(get_session)):
    service = BrandService(SqlAlchemyBrandRepository(db))
    return await service.get_all()


@router.get("/{brand_id}", response_model=BrandDTO)
async def get_brand(brand_id: UUID, db: AsyncSession = Depends(get_session)):
    service = BrandService(SqlAlchemyBrandRepository(db))
    return await service.get_by_id(brand_id)


@router.post("/", response_model=BrandDTO, status_code=201)
async def create_brand(body: BrandCreateDTO, db: AsyncSession = Depends(get_session)):
    service = BrandService(SqlAlchemyBrandRepository(db))
    return await service.create(body)


@router.put("/{brand_id}", response_model=BrandDTO)
async def update_brand(brand_id: UUID, body: BrandUpdateDTO, db: AsyncSession = Depends(get_session)):
    service = BrandService(SqlAlchemyBrandRepository(db))
    return await service.update(brand_id, body)


@router.delete("/{brand_id}", status_code=204)
async def delete_brand(brand_id: UUID, db: AsyncSession = Depends(get_session)):
    service = BrandService(SqlAlchemyBrandRepository(db))
    await service.delete(brand_id)