# DOMAIN
from app.domain.entities.supplier import Supplier
from app.domain.repositories.supplier_repository import SupplierRepository

# DATABASE
from app.infrastructure.database.session import AsyncSession
from app.infrastructure.database.models.supplier_model import SupplierModel

# INFRASTRUCTURE
from app.infrastructure.mappers.supplier_mapper import to_domain, to_model
from app.infrastructure.repositories.base_repository import SqlAlchemyBaseRepository


class SqlAlchemySupplierRepository(
    SqlAlchemyBaseRepository[Supplier, SupplierModel],
    SupplierRepository
):

    def __init__(self, session: AsyncSession):
        super().__init__(
            session=session,
            model=SupplierModel,
            to_domain=to_domain,
            to_model=to_model
        )
