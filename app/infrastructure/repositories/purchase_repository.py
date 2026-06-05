# DOMAIN
from app.domain.entities.purchase import Purchase
from app.domain.repositories.purchase_repository import PurchaseRepository

# DATABASE
from app.infrastructure.database.session import AsyncSession
from app.infrastructure.database.models.purchase_model import PurchaseModel

# INFRASTRUCTURE
from app.infrastructure.mappers.purchase_mapper import to_domain, to_model
from app.infrastructure.repositories.base_repository import SqlAlchemyBaseRepository


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