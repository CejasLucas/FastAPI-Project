from uuid import UUID
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import APIRouter, Depends, HTTPException

from app.infrastructure.database.session import get_session
from app.infrastructure.repositories.purchase_item_repository import SqlAlchemyPurchaseItemRepository

router = APIRouter(prefix="/purchase-items", tags=["Purchase Items"])


@router.get("/")
async def get_purchase_items(
    db: AsyncSession = Depends(get_session)
):
    repo = SqlAlchemyPurchaseItemRepository(db)

    return await repo.get_all()


@router.get("/{purchase_item_id}")
async def get_purchase_item(
    purchase_item_id: UUID,
    db: AsyncSession = Depends(get_session)
):
    repo = SqlAlchemyPurchaseItemRepository(db)

    purchase_item = await repo.get_by_id(purchase_item_id)

    if purchase_item is None:
        raise HTTPException(status_code=404, detail="Purchase item not found")

    return purchase_item