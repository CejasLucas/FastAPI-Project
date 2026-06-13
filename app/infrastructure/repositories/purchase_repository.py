# DOMAIN
from uuid import UUID

from sqlalchemy import select
from sqlalchemy.orm import joinedload

from app.domain.entities.purchase import Purchase
from app.domain.repositories.purchase_repository import PurchaseRepository

# DATABASE
from app.infrastructure.database.session import AsyncSession
from app.infrastructure.database.models.purchase_model import PurchaseModel

# INFRASTRUCTURE
from app.infrastructure.mappers.purchase_mapper import to_domain, to_model
from app.infrastructure.repositories.base_repository import SqlAlchemyBaseRepository
from app.infrastructure.database.models.purchase_item_model import PurchaseItemModel


class SqlAlchemyPurchaseRepository(
    SqlAlchemyBaseRepository[Purchase, PurchaseModel],
    PurchaseRepository
):
    def __init__(self, session: AsyncSession):
        super().__init__(
            session=session,
            model=PurchaseModel,
            to_domain=to_domain,
            to_model=to_model
        )

    async def get_detail(self, purchase_id: UUID):
        stmt = (
            select(PurchaseModel)
            .where(PurchaseModel.id == purchase_id)
            .options(
                joinedload(PurchaseModel.items)
                .joinedload(PurchaseItemModel.product)
            )
        )

        result = await self.session.execute(stmt)

        purchase = result.unique().scalar_one_or_none()

        return purchase