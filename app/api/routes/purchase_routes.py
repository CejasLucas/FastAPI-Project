from uuid import UUID
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import APIRouter, Depends, HTTPException

from app.infrastructure.database.session import get_session
from app.infrastructure.repositories.purchase_repository import SqlAlchemyPurchaseRepository

router = APIRouter(prefix="/purchases", tags=["Purchases"])


@router.get("/")
async def get_purchases(
    db: AsyncSession = Depends(get_session)
):
    repo = SqlAlchemyPurchaseRepository(db)

    return await repo.get_all()


@router.get("/{purchase_id}")
async def get_purchase(
    purchase_id: UUID,
    db: AsyncSession = Depends(get_session)
):
    repo = SqlAlchemyPurchaseRepository(db)

    purchase = await repo.get_by_id(purchase_id)

    if purchase is None:
        raise HTTPException(status_code=404, detail="Purchase not found")

    return purchase