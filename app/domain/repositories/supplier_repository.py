from app.domain.entities.supplier import Supplier
from app.domain.repositories.base_repository import BaseRepository

# CRUD
class SupplierRepository(BaseRepository[Supplier]):
    ...