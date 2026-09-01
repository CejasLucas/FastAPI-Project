from uuid import UUID
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import APIRouter, Depends

from app.domain.enums.pruduct_unit import Unit
from app.infrastructure.database.session import get_session
from app.infrastructure.repositories.product_repository import SqlAlchemyProductRepository

from app.api.dtos.product_dto import (
    ProductDTO,
    ProductCreateDTO,
    ProductUpdateDTO,
    ProductListItemDTO,
)
from app.api.services.product_service import ProductService


router = APIRouter(prefix="/products", tags=["Products"])


@router.get("/", response_model=list[ProductDTO])
async def get_products(db: AsyncSession = Depends(get_session)):
    service = ProductService(SqlAlchemyProductRepository(db))
    return await service.get_all()


@router.get("/items", response_model=list[ProductListItemDTO])
async def get_product_items(db: AsyncSession = Depends(get_session)):
    service = ProductService(SqlAlchemyProductRepository(db))
    return await service.get_all_for_selection()


@router.get("/units")
async def get_units():
    return [
        {"value": unit.value, "label": unit.value.capitalize()}
        for unit in Unit
    ]


@router.get("/{product_id}", response_model=ProductDTO)
async def get_product(product_id: UUID, db: AsyncSession = Depends(get_session)):
    service = ProductService(SqlAlchemyProductRepository(db))
    return await service.get_by_id(product_id)


@router.post("/", response_model=ProductDTO, status_code=201)
async def create_product(body: ProductCreateDTO, db: AsyncSession = Depends(get_session)):
    service = ProductService(SqlAlchemyProductRepository(db))
    return await service.create(body)


@router.put("/{product_id}", response_model=ProductDTO)
async def update_product(product_id: UUID, body: ProductUpdateDTO, db: AsyncSession = Depends(get_session)):
    service = ProductService(SqlAlchemyProductRepository(db))
    return await service.update(product_id, body)


@router.delete("/{product_id}", status_code=204)
async def delete_product(product_id: UUID, db: AsyncSession = Depends(get_session)):
    service = ProductService(SqlAlchemyProductRepository(db))
    await service.delete(product_id)