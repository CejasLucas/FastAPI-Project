from uuid import UUID
from fastapi import HTTPException

from app.domain.entities.brand import Brand
from app.api.dtos.brand_dto import BrandDTO, BrandCreateDTO, BrandUpdateDTO
from app.infrastructure.repositories.brand_repository import SqlAlchemyBrandRepository


class BrandService:
    def __init__(self, repo: SqlAlchemyBrandRepository):
        self.repo = repo


    async def get_all(self) -> list[BrandDTO]:

        brands = await self.repo.get_all()

        return [BrandDTO.model_validate(b) for b in brands]



    async def get_by_id(self, brand_id: UUID) -> BrandDTO:

        brand = await self.repo.get_by_id(brand_id)

        if brand is None:
            raise HTTPException(status_code=404, detail="Brand not found")

        return BrandDTO.model_validate(brand)



    async def create(self, dto: BrandCreateDTO) -> BrandDTO:

        brand = Brand(id=None, **dto.model_dump())

        created = await self.repo.create(brand)

        return BrandDTO.model_validate(created)



    async def update(self, brand_id: UUID, dto: BrandUpdateDTO) -> BrandDTO:

        existing = await self.repo.get_by_id(brand_id)

        if existing is None:
            raise HTTPException(status_code=404, detail="Brand not found")

        updated_data = {**vars(existing), **dto.model_dump(exclude_unset=True)}

        updated_brand = Brand(**updated_data)

        result = await self.repo.update(updated_brand)

        return BrandDTO.model_validate(result)



    async def delete(self, brand_id: UUID) -> None:

        existing = await self.repo.get_by_id(brand_id)

        if existing is None:
            raise HTTPException(status_code=404, detail="Brand not found")

        await self.repo.delete(brand_id)
