from app.domain.entities.purchase_item import PurchaseItem
from app.domain.repositories.base_repository import BaseRepository

# CRUD
class PurchaseItemRepository(BaseRepository[PurchaseItem]):
    ...