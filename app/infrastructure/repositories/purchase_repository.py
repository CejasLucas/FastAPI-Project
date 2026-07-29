from uuid import UUID

from sqlalchemy import select, extract, func
from sqlalchemy.orm import joinedload

from app.infrastructure.mappers.purchase_mapper import to_domain, to_model
from app.infrastructure.repositories.base_repository import SqlAlchemyBaseRepository

from app.infrastructure.database.session import AsyncSession
from app.infrastructure.database.models.product_model import ProductModel
from app.infrastructure.database.models.purchase_model import PurchaseModel
from app.infrastructure.database.models.purchase_item_model import PurchaseItemModel

from app.domain.entities.purchase import Purchase
from app.domain.enums.purchase_status import PurchaseStatus
from app.domain.repositories.purchase_repository import PurchaseRepository


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


    async def get_detail_model(self, purchase_id: UUID) -> PurchaseModel | None:
        stmt = (
            select(PurchaseModel)
            .where(PurchaseModel.id == purchase_id)
            .options(
                joinedload(PurchaseModel.supplier),
                joinedload(PurchaseModel.items)
                .joinedload(PurchaseItemModel.product)
                .joinedload(ProductModel.brand),
                joinedload(PurchaseModel.items)
                .joinedload(PurchaseItemModel.product)
                .joinedload(ProductModel.category)
            )
        )

        result = await self.session.execute(stmt)

        return result.unique().scalar_one_or_none()


    async def get_confirmed_by_year(self, year: int) -> list[PurchaseModel]:
        stmt = (
            select(PurchaseModel)
            .where(
                extract("year", PurchaseModel.purchase_date) == year,
                PurchaseModel.status == PurchaseStatus.CONFIRMED
            )
            .options(
                joinedload(PurchaseModel.supplier),
                joinedload(PurchaseModel.items)
                .joinedload(PurchaseItemModel.product)
                .joinedload(ProductModel.category)
            )
        )

        result = await self.session.execute(stmt)

        return list(result.unique().scalars().all())


    async def count_confirmed_by_year(self, year: int) -> int:
        stmt = (
            select(func.count())
            .select_from(PurchaseModel)
            .where(
                extract("year", PurchaseModel.purchase_date) == year,
                PurchaseModel.status == PurchaseStatus.CONFIRMED
            )
        )

        result = await self.session.execute(stmt)

        return result.scalar_one()


    async def get_recent(self, limit: int) -> list[PurchaseModel]:
        stmt = (
            select(PurchaseModel)
            .where(
                PurchaseModel.status == PurchaseStatus.CONFIRMED
            )
            .options(
                joinedload(PurchaseModel.supplier),
                joinedload(PurchaseModel.items)
                .joinedload(PurchaseItemModel.product)
            )
            .order_by(
                PurchaseModel.purchase_date.desc()
            )
            .limit(limit)
        )

        result = await self.session.execute(stmt)

        return list(result.unique().scalars().all())


    async def count_by_year(self, year: int) -> int:
        stmt = (
            select(func.count())
            .select_from(PurchaseModel)
            .where(
                extract("year", PurchaseModel.purchase_date) == year
            )
        )

        result = await self.session.execute(stmt)

        return result.scalar_one()


    async def get_purchases_by_year(self, year: int) -> list[PurchaseModel]:
        stmt = (
            select(PurchaseModel)
            .where(
                extract("year", PurchaseModel.purchase_date) == year
            )
            .options(
                joinedload(PurchaseModel.supplier),
                joinedload(PurchaseModel.items)
                .joinedload(PurchaseItemModel.product)
                .joinedload(ProductModel.category)
            )
        )

        result = await self.session.execute(stmt)

        return list(result.unique().scalars().all())


    async def get_total_by_status_and_year(
        self,
        year: int,
        status: PurchaseStatus
    ) -> float:

        stmt = (
            select(
                func.coalesce(
                    func.sum(PurchaseModel.total_amount),
                    0
                )
            )
            .where(
                extract("year", PurchaseModel.purchase_date) == year,
                PurchaseModel.status == status
            )
        )

        result = await self.session.execute(stmt)

        return float(result.scalar_one())