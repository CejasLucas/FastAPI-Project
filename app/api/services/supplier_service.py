from uuid import UUID
from fastapi import HTTPException

from app.domain.entities.supplier import Supplier
from app.api.dtos.supplier_dto import SupplierDTO, SupplierCreateDTO, SupplierUpdateDTO
from app.infrastructure.repositories.supplier_repository import SqlAlchemySupplierRepository


class SupplierService:
    def __init__(self, repo: SqlAlchemySupplierRepository):
        self.repo = repo


    async def get_all(self) -> list[SupplierDTO]:

        suppliers = await self.repo.get_all()

        return [SupplierDTO.model_validate(s) for s in suppliers]



    async def get_by_id(self, supplier_id: UUID) -> SupplierDTO:

        supplier = await self.repo.get_by_id(supplier_id)

        if supplier is None:
            raise HTTPException(status_code=404, detail="Supplier not found")

        return SupplierDTO.model_validate(supplier)



    async def create(self, dto: SupplierCreateDTO) -> SupplierDTO:

        supplier = Supplier(id=None, **dto.model_dump())

        created = await self.repo.create(supplier)

        return SupplierDTO.model_validate(created)



    async def update(self, supplier_id: UUID, dto: SupplierUpdateDTO) -> SupplierDTO:
        existing = await self.repo.get_by_id(supplier_id)

        if existing is None:
            raise HTTPException(status_code=404, detail="Supplier not found")

        updated_data = {**vars(existing), **dto.model_dump(exclude_unset=True)}

        updated_supplier = Supplier(**updated_data)

        result = await self.repo.update(updated_supplier)

        return SupplierDTO.model_validate(result)



    async def delete(self, supplier_id: UUID) -> None:

        existing = await self.repo.get_by_id(supplier_id)

        if existing is None:
            raise HTTPException(status_code=404, detail="Supplier not found")

        await self.repo.delete(supplier_id)