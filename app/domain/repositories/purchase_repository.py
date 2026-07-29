from uuid import UUID
from app.domain.entities.purchase import Purchase
from app.domain.repositories.base_repository import BaseRepository
from domain.enums.purchase_status import PurchaseStatus


# CRUD
class PurchaseRepository(BaseRepository[Purchase]):

    async def get_recent(self, limit: int) -> list[Purchase]:
        ...

    async def get_detail_model(self, purchase_id: UUID):
        ...

    async def get_purchases_by_year(self, year: int) -> list[Purchase]:
        ...

    async def count_by_year(self, year: int) -> int:
        ...

    async def get_total_by_status_and_year(self, year, status: PurchaseStatus):
        ...

    async def count_confirmed_by_year(self, year: int) -> int:
        ...

    async def get_confirmed_by_year(self, year: int):
        ...