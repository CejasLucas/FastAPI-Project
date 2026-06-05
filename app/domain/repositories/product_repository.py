from app.domain.entities.product import Product
from app.domain.repositories.base_repository import BaseRepository

# CRUD
class ProductRepository(BaseRepository[Product]):
    ...
