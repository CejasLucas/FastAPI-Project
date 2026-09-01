from uuid import UUID
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import APIRouter, Depends

from app.api.dtos.supplier_dto import SupplierDTO, SupplierCreateDTO, SupplierUpdateDTO
from app.api.services.supplier_service import SupplierService

from app.infrastructure.database.session import get_session
from app.infrastructure.repositories.supplier_repository import SqlAlchemySupplierRepository

router = APIRouter(prefix="/suppliers", tags=["Suppliers"])


@router.get("/", response_model=list[SupplierDTO])
async def get_suppliers(db: AsyncSession = Depends(get_session)):
    service = SupplierService(SqlAlchemySupplierRepository(db))
    return await service.get_all()


@router.get("/{supplier_id}", response_model=SupplierDTO)
async def get_supplier(supplier_id: UUID, db: AsyncSession = Depends(get_session)):
    service = SupplierService(SqlAlchemySupplierRepository(db))
    return await service.get_by_id(supplier_id)


@router.post("/", response_model=SupplierDTO, status_code=201)
async def create_supplier(body: SupplierCreateDTO, db: AsyncSession = Depends(get_session)):
    service = SupplierService(SqlAlchemySupplierRepository(db))
    return await service.create(body)


@router.put("/{supplier_id}", response_model=SupplierDTO)
async def update_supplier(supplier_id: UUID, body: SupplierUpdateDTO, db: AsyncSession = Depends(get_session)):
    service = SupplierService(SqlAlchemySupplierRepository(db))
    return await service.update(supplier_id, body)


@router.delete("/{supplier_id}", status_code=204)
async def delete_supplier(supplier_id: UUID, db: AsyncSession = Depends(get_session)):
    service = SupplierService(SqlAlchemySupplierRepository(db))
    await service.delete(supplier_id)