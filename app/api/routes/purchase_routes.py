from uuid import UUID
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import APIRouter, Depends

from app.api.services.purchase_service import PurchaseService
from app.api.dtos.purchase_dto import (
    PurchaseDetailDTO,
    PurchaseListItemDTO,
    PurchaseCreateDTO,
    PurchaseUpdateDTO,
)

from app.infrastructure.database.session import get_session
from app.infrastructure.repositories.purchase_repository import SqlAlchemyPurchaseRepository

router = APIRouter(prefix="/purchases", tags=["Purchases"])


@router.get("/", response_model=list[PurchaseListItemDTO])
async def get_purchases(db: AsyncSession = Depends(get_session)):
    service = PurchaseService(SqlAlchemyPurchaseRepository(db))
    return await service.get_all()


@router.get("/{purchase_id}", response_model=PurchaseDetailDTO)
async def get_purchase(purchase_id: UUID, db: AsyncSession = Depends(get_session)):
    service = PurchaseService(SqlAlchemyPurchaseRepository(db))
    return await service.get_detail(purchase_id)


@router.post("/", response_model=PurchaseDetailDTO, status_code=201)
async def create_purchase(body: PurchaseCreateDTO, db: AsyncSession = Depends(get_session)):
    service = PurchaseService(SqlAlchemyPurchaseRepository(db))
    return await service.create(body)


@router.put("/{purchase_id}", response_model=PurchaseDetailDTO)
async def update_purchase(purchase_id: UUID, body: PurchaseUpdateDTO, db: AsyncSession = Depends(get_session)):
    service = PurchaseService(SqlAlchemyPurchaseRepository(db))
    return await service.update(purchase_id, body)


@router.delete("/{purchase_id}", status_code=204)
async def delete_purchase(purchase_id: UUID, db: AsyncSession = Depends(get_session)):
    service = PurchaseService(SqlAlchemyPurchaseRepository(db))
    await service.delete(purchase_id)