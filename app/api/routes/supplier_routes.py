from uuid import UUID
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import APIRouter, Depends, HTTPException

from app.domain.entities.supplier import Supplier
from app.api.dtos.supplier_dto import SupplierCreateDTO, SupplierUpdateDTO

from app.infrastructure.database.session import get_session
from app.infrastructure.repositories.supplier_repository import SqlAlchemySupplierRepository


router = APIRouter(prefix="/suppliers", tags=["Suppliers"])

# ── Endpoints ──────────────────────────────────────────────────────────────────
@router.get("/")
async def get_suppliers(
    db: AsyncSession = Depends(get_session)
):
    repo = SqlAlchemySupplierRepository(db)
    return await repo.get_all()


@router.get("/{supplier_id}")
async def get_supplier(
    supplier_id: UUID,
    db: AsyncSession = Depends(get_session)
):
    repo = SqlAlchemySupplierRepository(db)
    supplier = await repo.get_by_id(supplier_id)

    if supplier is None:
        raise HTTPException(status_code=404, detail="Supplier not found")

    return supplier


@router.post("/", status_code=201)
async def create_supplier(
    body: SupplierCreateDTO,
    db: AsyncSession = Depends(get_session)
):
    repo = SqlAlchemySupplierRepository(db)

    supplier = Supplier(
        id=None,
        **body.model_dump()
    )

    return await repo.create(supplier)


@router.put("/{supplier_id}")
async def update_supplier(
    supplier_id: UUID,
    body: SupplierUpdateDTO,
    db: AsyncSession = Depends(get_session)
):
    repo = SqlAlchemySupplierRepository(db)

    existing = await repo.get_by_id(supplier_id)
    if existing is None:
        raise HTTPException(status_code=404, detail="Supplier not found")

    updated_data = existing.__dict__ | {
        k: v for k, v in body.model_dump().items() if v is not None
    }

    updated_supplier = Supplier(**updated_data)

    return await repo.update(updated_supplier)


@router.delete("/{supplier_id}", status_code=204)
async def delete_supplier(
    supplier_id: UUID,
    db: AsyncSession = Depends(get_session)
):
    repo = SqlAlchemySupplierRepository(db)

    existing = await repo.get_by_id(supplier_id)
    if existing is None:
        raise HTTPException(status_code=404, detail="Supplier not found")

    await repo.delete(supplier_id)