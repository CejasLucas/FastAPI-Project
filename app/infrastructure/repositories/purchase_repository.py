from uuid import UUID
from datetime import datetime

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


    async def get_all_with_details(self) -> list[PurchaseModel]:
        stmt = (
            select(PurchaseModel)
            .options(
                joinedload(PurchaseModel.supplier),
                joinedload(PurchaseModel.items),
            )
            .order_by(PurchaseModel.purchase_date.desc())
        )

        result = await self.session.execute(stmt)

        return list(result.unique().scalars().all())


    async def get_model_with_items(self, purchase_id: UUID) -> PurchaseModel | None:
        stmt = (
            select(PurchaseModel)
            .where(PurchaseModel.id == purchase_id)
            .options(joinedload(PurchaseModel.items))
        )

        result = await self.session.execute(stmt)

        return result.unique().scalar_one_or_none()


    async def create_full(
        self,
        supplier_id: UUID,
        purchase_date: datetime,
        status: PurchaseStatus,
        items: list[dict],
    ) -> PurchaseModel:

        total_amount = sum(
            item["quantity"] * item["unit_price"] for item in items
        )

        purchase = PurchaseModel(
            supplier_id=supplier_id,
            purchase_date=purchase_date,
            status=status,
            total_amount=total_amount,
            items=[
                PurchaseItemModel(
                    product_id=item["product_id"],
                    quantity=item["quantity"],
                    unit_price=item["unit_price"],
                )
                for item in items
            ],
        )

        self.session.add(purchase)

        await self.session.flush()

        return purchase


    async def update_full(
        self,
        purchase_id: UUID,
        supplier_id: UUID,
        purchase_date: datetime,
        status: PurchaseStatus,
        items: list[dict],
    ) -> PurchaseModel | None:

        purchase = await self.get_model_with_items(purchase_id)

        if purchase is None:
            return None

        total_amount = sum(
            item["quantity"] * item["unit_price"] for item in items
        )

        purchase.supplier_id = supplier_id
        purchase.purchase_date = purchase_date
        purchase.status = status
        purchase.total_amount = total_amount

        purchase.items.clear()
        purchase.items.extend(
            PurchaseItemModel(
                product_id=item["product_id"],
                quantity=item["quantity"],
                unit_price=item["unit_price"],
            )
            for item in items
        )

        await self.session.flush()

        return purchase


    async def delete_by_id(self, purchase_id: UUID) -> bool:
        purchase = await self.session.get(PurchaseModel, purchase_id)

        if purchase is None:
            return False

        await self.session.delete(purchase)
        await self.session.flush()

        return True


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