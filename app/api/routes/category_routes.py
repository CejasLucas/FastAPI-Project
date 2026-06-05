from uuid import UUID
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import APIRouter, Depends, HTTPException

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