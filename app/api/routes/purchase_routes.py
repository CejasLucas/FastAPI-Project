from uuid import UUID
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import APIRouter, Depends, HTTPException

from api.dtos.purchase_dto import PurchaseDetailDTO
from app.infrastructure.database.session import get_session
from app.infrastructure.repositories.purchase_repository import SqlAlchemyPurchaseRepository

router = APIRouter(prefix="/purchases", tags=["Purchases"])


@router.get("/")
async def get_purchases(
    db: AsyncSession = Depends(get_session)
):
    repo = SqlAlchemyPurchaseRepository(db)

    return await repo.get_all()


@router.get("/details/{purchase_id}")
async def get_details_purchase(
    purchase_id: UUID,
    db: AsyncSession = Depends(get_session)
) -> PurchaseDetailDTO:
    repo = SqlAlchemyPurchaseRepository(db)

    purchase = await repo.get_detail(purchase_id)

    if purchase is None:
        raise HTTPException(
            status_code=404,
            detail="Purchase not found"
        )

    return PurchaseDetailDTO(
        id=purchase.id,
        supplier_id=purchase.supplier_id,
        purchase_date=purchase.purchase_date,
        status=purchase.status,
        total_amount=float(purchase.total_amount),
        items=[
            {
                "product_id": item.product.id,
                "product_name": item.product.name,
                "quantity": item.quantity,
                "unit_price": float(item.unit_price),
                "subtotal": float(item.quantity * item.unit_price),
            }
            for item in purchase.items
        ]
    )


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