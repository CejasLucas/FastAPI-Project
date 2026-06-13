from uuid import UUID
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import APIRouter, Depends, HTTPException

from app.domain.entities.category import Category
from app.api.dtos.category_dto import CategoryCreateDTO, CategoryUpdateDTO

from app.infrastructure.database.session import get_session
from app.infrastructure.repositories.category_repository import SqlAlchemyCategoryRepository

router = APIRouter(prefix="/categories", tags=["Categories"])

@router.get("/")
async def get_categories(
    db: AsyncSession = Depends(get_session)
):
    repo = SqlAlchemyCategoryRepository(db)

    return await repo.get_all()


@router.get("/{category_id}")
async def get_category(
        category_id: UUID,
        db: AsyncSession = Depends(get_session)
):
    repo = SqlAlchemyCategoryRepository(db)

    category = await repo.get_by_id(category_id)

    if category is None:
        raise HTTPException(status_code=404, detail="Category not found")

    return category


@router.post("/", status_code=201)
async def create_category(
    body: CategoryCreateDTO,
    db: AsyncSession = Depends(get_session)
):
    repo = SqlAlchemyCategoryRepository(db)

    category = Category(
        id=None,
        **body.model_dump()
    )

    return await repo.create(category)


@router.put("/{category_id}")
async def update_category(
    category_id: UUID,
    body: CategoryUpdateDTO,
    db: AsyncSession = Depends(get_session)
):
    repo = SqlAlchemyCategoryRepository(db)

    existing = await repo.get_by_id(category_id)
    if existing is None:
        raise HTTPException(status_code=404, detail="Category not found")

    updated_data = existing.__dict__ | {
        k: v for k, v in body.model_dump().items() if v is not None
    }

    updated_category = Category(**updated_data)

    return await repo.update(updated_category)


@router.delete("/{category_id}", status_code=204)
async def delete_category(
    category_id: UUID,
    db: AsyncSession = Depends(get_session)
):
    repo = SqlAlchemyCategoryRepository(db)

    existing = await repo.get_by_id(category_id)
    if existing is None:
        raise HTTPException(status_code=404, detail="Category not found")

    await repo.delete(category_id)