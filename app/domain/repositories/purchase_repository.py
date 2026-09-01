from abc import ABC
from uuid import UUID
from datetime import datetime

from app.domain.entities.purchase import Purchase
from app.domain.enums.purchase_status import PurchaseStatus
from app.domain.repositories.base_repository import BaseRepository


# CRUD
class PurchaseRepository(BaseRepository[Purchase], ABC):

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

    async def get_all_with_details(self) -> list:
        ...

    async def get_model_with_items(self, purchase_id: UUID):
        ...

    async def create_full(
        self,
        supplier_id: UUID,
        purchase_date: datetime,
        status: PurchaseStatus,
        items: list[dict],
    ):
        ...

    async def update_full(
        self,
        purchase_id: UUID,
        supplier_id: UUID,
        purchase_date: datetime,
        status: PurchaseStatus,
        items: list[dict],
    ):
        ...

    async def delete_by_id(self, purchase_id: UUID) -> bool:
        ...