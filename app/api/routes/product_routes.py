from uuid import UUID
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import APIRouter, Depends, HTTPException

from domain.enums.pruduct_unit import Unit
from app.domain.entities.product import  Product
from app.api.dtos.product_dto import ProductCreateDTO, ProductUpdateDTO

from app.infrastructure.database.session import get_session
from app.infrastructure.repositories.product_repository import SqlAlchemyProductRepository

router = APIRouter(prefix="/products", tags=["Products"])


@router.get("/")
async def get_products(
    db: AsyncSession = Depends(get_session)
):
    repo = SqlAlchemyProductRepository(db)

    return await repo.get_all()

@router.get("/units")
async def get_units():
    return [
        {
            "value": unit.value,
            "label": unit.value.capitalize()
        }
        for unit in Unit
    ]

@router.post("/", status_code=201)
async def create_product(
    body: ProductCreateDTO,
    db: AsyncSession = Depends(get_session)
):
    repo = SqlAlchemyProductRepository(db)

    product = Product(
        id=None,
        **body.model_dump()
    )

    return await repo.create(product)


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


@router.put("/{product_id}")
async def update_product(
    product_id: UUID,
    body: ProductUpdateDTO,
    db: AsyncSession = Depends(get_session)
):
    repo = SqlAlchemyProductRepository(db)

    existing = await repo.get_by_id(product_id)
    if existing is None:
        raise HTTPException(status_code=404, detail="Product not found")

    updated_data = existing.__dict__ | {
        k: v for k, v in body.model_dump().items() if v is not None
    }

    updated_product = Product(**updated_data)

    return await repo.update(updated_product)


@router.delete("/{product_id}", status_code=204)
async def delete_product(
    product_id: UUID,
    db: AsyncSession = Depends(get_session)
):
    repo = SqlAlchemyProductRepository(db)

    existing = await repo.get_by_id(product_id)
    if existing is None:
        raise HTTPException(status_code=404, detail="Product not found")

    await repo.delete(product_id)

