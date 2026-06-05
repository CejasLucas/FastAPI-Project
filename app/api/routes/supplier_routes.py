from uuid import UUID
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import APIRouter, Depends, HTTPException

from app.infrastructure.database.session import get_session
from app.infrastructure.repositories.supplier_repository import SqlAlchemySupplierRepository


router = APIRouter(prefix="/suppliers", tags=["Suppliers"])


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