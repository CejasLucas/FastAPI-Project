# DOMAIN
from app.domain.entities.stock_movement import StockMovement
from app.domain.repositories.stock_movement_repository import StockMovementRepository

# DATABASE
from app.infrastructure.database.session import AsyncSession
from app.infrastructure.database.models.stock_movement_model import StockMovementModel

# INFRASTRUCTURE
from app.infrastructure.mappers.stock_movement_mapper import to_domain, to_model
from app.infrastructure.repositories.base_repository import SqlAlchemyBaseRepository


class SqlAlchemyStockMovementRepository(
    SqlAlchemyBaseRepository[StockMovement, StockMovementModel],
    StockMovementRepository
):
    def __init__(self, session: AsyncSession):
        super().__init__(
            session=session,
            model=StockMovementModel,
            to_domain=to_domain,
            to_model=to_model
        )