from abc import ABC
from app.domain.entities.product import Product
from app.domain.repositories.base_repository import BaseRepository

# CRUD
class ProductRepository(BaseRepository[Product], ABC):

    async def get_low_stock(self, limit: int) -> list[Product]:
        ...