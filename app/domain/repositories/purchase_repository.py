from app.domain.entities.purchase import Purchase
from app.domain.repositories.base_repository import BaseRepository

# CRUD
class PurchaseRepository(BaseRepository[Purchase]):
    ...