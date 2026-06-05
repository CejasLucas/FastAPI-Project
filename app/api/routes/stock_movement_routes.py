from uuid import UUID
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import APIRouter, Depends, HTTPException

from app.infrastructure.database.session import get_session
from app.infrastructure.repositories.stock_movement_repository import SqlAlchemyStockMovementRepository


router = APIRouter(prefix="/stock_movements", tags=["Stock Movements"])


@router.get("/")
async def get_suppliers(
    db: AsyncSession = Depends(get_session)
):
    repo = SqlAlchemyStockMovementRepository(db)

    return await repo.get_all()


@router.get("/{stock_movement_id}")
async def get_supplier(
    stock_movement_id: UUID,
    db: AsyncSession = Depends(get_session)
):
    repo = SqlAlchemyStockMovementRepository(db)

    stock_movement = await repo.get_by_id(stock_movement_id)

    if stock_movement is None:
        raise HTTPException(status_code=404, detail="Stock Movement not found")

    return stock_movement