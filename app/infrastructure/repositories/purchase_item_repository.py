# DOMAIN
from app.domain.entities.purchase_item import PurchaseItem
from app.domain.repositories.purchase_item_repository import PurchaseItemRepository

# DATABASE
from app.infrastructure.database.session import AsyncSession
from app.infrastructure.database.models.purchase_item_model import PurchaseItemModel

# INFRASTRUCTURE
from app.infrastructure.mappers.purchase_item_mapper import to_domain, to_model
from app.infrastructure.repositories.base_repository import SqlAlchemyBaseRepository


class SqlAlchemyPurchaseItemRepository(
    SqlAlchemyBaseRepository[PurchaseItem, PurchaseItemModel],
    PurchaseItemRepository
):
    def __init__(self, session: AsyncSession):
        super().__init__(
            session=session,
            model=PurchaseItemModel,
            to_domain=to_domain,
            to_model=to_model
        )