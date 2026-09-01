from uuid import UUID
from abc import ABC, abstractmethod
from typing import Generic, TypeVar

T = TypeVar("T")

class BaseRepository(ABC, Generic[T]):

    @abstractmethod
    async def create(self, entity: T) -> T:
        ...

    @abstractmethod
    async def get_by_id(self, id: UUID) -> T | None:
        ...

    @abstractmethod
    async def update(self, entity: T) -> T:
        ...

    @abstractmethod
    async def delete(self, id: UUID) -> None:
        ...

    @abstractmethod
    async def get_all(self) -> list[T]:
        ...

    @abstractmethod
    async def count_all(self) -> int:
        ...