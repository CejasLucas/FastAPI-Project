from app.domain.entities.category import Category
from app.domain.repositories.base_repository import BaseRepository

# CRUD
class CategoryRepository(BaseRepository[Category]):
    ...