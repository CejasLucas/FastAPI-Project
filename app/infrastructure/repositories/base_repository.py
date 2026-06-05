from typing import Generic, TypeVar, Type, Callable
from uuid import UUID

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

T = TypeVar("T")  # Domain Entity
M = TypeVar("M")  # ORM Model


class SqlAlchemyBaseRepository(Generic[T, M]):

    def __init__(
        self,
        session: AsyncSession,
        model: Type[M],
        to_domain: Callable[[M], T],
        to_model: Callable[[T], M],
    ):
        self.session = session
        self.model = model
        self.to_domain = to_domain
        self.to_model = to_model


    async def create(self, entity: T) -> T:
        model = self.to_model(entity)

        self.session.add(model)

        await self.session.flush()

        return self.to_domain(model)


    async def get_by_id(self, entity_id: UUID) -> T | None:
        model = await self.session.get(self.model, entity_id)

        return self.to_domain(model) if model else None


    async def update(self, entity: T) -> T:
        model = await self.session.get(self.model, entity.id)

        if not model:
            raise ValueError("Entity not found")

        updated_model = self.to_model(entity)

        for key, value in vars(updated_model).items():
            if key.startswith("_"):
                continue

            setattr(model, key, value)

        await self.session.flush()

        return self.to_domain(model)


    async def delete(self, entity_id: UUID) -> None:
        model = await self.session.get(self.model, entity_id)

        if model:
            await self.session.delete(model)
            await self.session.flush()


    async def get_all(self) -> list[T]:
        result = await self.session.execute( select(self.model) )

        return [
            self.to_domain(model)
            for model in result.scalars().all()
        ]
