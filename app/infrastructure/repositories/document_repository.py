# DOMAIN
from app.domain.entities.document import Document
from app.domain.repositories.document_repository import DocumentRepository

# DATABASE
from app.infrastructure.database.session import AsyncSession
from app.infrastructure.database.models.document_model import DocumentModel

# INFRASTRUCTURE
from app.infrastructure.repositories.base_repository import SqlAlchemyBaseRepository
from app.infrastructure.mappers.document_mapper import to_domain, to_model


class SqlAlchemyDocumentRepository(
    SqlAlchemyBaseRepository[Document, DocumentModel],
    DocumentRepository
):

    def __init__(self, session: AsyncSession):
        super().__init__(
            session=session,
            model=DocumentModel,
            to_domain=to_domain,
            to_model=to_model
        )