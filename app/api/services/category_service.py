from uuid import UUID
from fastapi import HTTPException

from app.domain.entities.category import Category
from app.api.dtos.category_dto import CategoryDTO, CategoryCreateDTO, CategoryUpdateDTO
from app.infrastructure.repositories.category_repository import SqlAlchemyCategoryRepository


class CategoryService:
    def __init__(self, repo: SqlAlchemyCategoryRepository):
        self.repo = repo


    async def get_all(self) -> list[CategoryDTO]:

        categories = await self.repo.get_all()

        return [CategoryDTO.model_validate(c) for c in categories]



    async def get_by_id(self, category_id: UUID) -> CategoryDTO:

        category = await self.repo.get_by_id(category_id)

        if category is None:
            raise HTTPException(status_code=404, detail="Category not found")

        return CategoryDTO.model_validate(category)



    async def create(self, dto: CategoryCreateDTO) -> CategoryDTO:

        category = Category(id=None, **dto.model_dump())

        created = await self.repo.create(category)

        return CategoryDTO.model_validate(created)



    async def update(self, category_id: UUID, dto: CategoryUpdateDTO) -> CategoryDTO:

        existing = await self.repo.get_by_id(category_id)

        if existing is None:
            raise HTTPException(status_code=404, detail="Category not found")

        updated_data = {**vars(existing), **dto.model_dump(exclude_unset=True)}

        updated_category = Category(**updated_data)

        result = await self.repo.update(updated_category)

        return CategoryDTO.model_validate(result)



    async def delete(self, category_id: UUID) -> None:

        existing = await self.repo.get_by_id(category_id)

        if existing is None:
            raise HTTPException(status_code=404, detail="Category not found")

        await self.repo.delete(category_id)
