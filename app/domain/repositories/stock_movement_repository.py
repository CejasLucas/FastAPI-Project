from app.domain.entities.stock_movement import StockMovement
from app.domain.repositories.base_repository import BaseRepository

# CRUD
class StockMovementRepository(BaseRepository[StockMovement]):
    ...