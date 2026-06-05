# DOMAIN
from app.domain.entities.category import Category
from app.domain.repositories.category_repository import CategoryRepository

# DATABASE
from app.infrastructure.database.session import AsyncSession
from app.infrastructure.database.models.category_model import CategoryModel

# INFRASTRUCTURE
from app.infrastructure.repositories.base_repository import SqlAlchemyBaseRepository
from app.infrastructure.mappers.category_mapper import to_domain, to_model


class SqlAlchemyCategoryRepository(
    SqlAlchemyBaseRepository[Category, CategoryModel],
    CategoryRepository
):

    def __init__(self, session: AsyncSession):
        super().__init__(
            session=session,
            model=CategoryModel,
            to_domain=to_domain,
            to_model=to_model
        )