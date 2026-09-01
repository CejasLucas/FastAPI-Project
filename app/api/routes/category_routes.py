from uuid import UUID
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import APIRouter, Depends

from app.api.dtos.category_dto import CategoryDTO, CategoryCreateDTO, CategoryUpdateDTO
from app.api.services.category_service import CategoryService

from app.infrastructure.database.session import get_session
from app.infrastructure.repositories.category_repository import SqlAlchemyCategoryRepository

router = APIRouter(prefix="/categories", tags=["Categories"])


@router.get("/", response_model=list[CategoryDTO])
async def get_categories(db: AsyncSession = Depends(get_session)):
    service = CategoryService(SqlAlchemyCategoryRepository(db))
    return await service.get_all()


@router.get("/{category_id}", response_model=CategoryDTO)
async def get_category(category_id: UUID, db: AsyncSession = Depends(get_session)):
    service = CategoryService(SqlAlchemyCategoryRepository(db))
    return await service.get_by_id(category_id)


@router.post("/", response_model=CategoryDTO, status_code=201)
async def create_category(body: CategoryCreateDTO, db: AsyncSession = Depends(get_session)):
    service = CategoryService(SqlAlchemyCategoryRepository(db))
    return await service.create(body)


@router.put("/{category_id}", response_model=CategoryDTO)
async def update_category(category_id: UUID, body: CategoryUpdateDTO, db: AsyncSession = Depends(get_session)):
    service = CategoryService(SqlAlchemyCategoryRepository(db))
    return await service.update(category_id, body)


@router.delete("/{category_id}", status_code=204)
async def delete_category(category_id: UUID, db: AsyncSession = Depends(get_session)):
    service = CategoryService(SqlAlchemyCategoryRepository(db))
    await service.delete(category_id)