from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.infrastructure.database.session import get_session
from app.infrastructure.repositories.purchase_repository import SqlAlchemyPurchaseRepository
from app.infrastructure.repositories.product_repository import SqlAlchemyProductRepository
from app.infrastructure.repositories.supplier_repository import SqlAlchemySupplierRepository

from app.api.dtos.dashboard_dto import DashboardSummaryDTO
from app.domain.services.dashboard_service import DashboardService


router = APIRouter(prefix="/dashboard", tags=["Dashboard"])

@router.get("/", response_model=DashboardSummaryDTO)
async def get_dashboard_summary(
        db: AsyncSession = Depends(get_session)
):
    service = DashboardService(
        supplier_repo=SqlAlchemySupplierRepository(db),
        product_repo=SqlAlchemyProductRepository(db),
        purchase_repo=SqlAlchemyPurchaseRepository(db)
    )
    return await service.get_summary()
