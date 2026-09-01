from abc import ABC
from app.domain.entities.brand import Brand
from app.domain.repositories.base_repository import BaseRepository

# CRUD
class BrandRepository(BaseRepository[Brand], ABC):
    ...