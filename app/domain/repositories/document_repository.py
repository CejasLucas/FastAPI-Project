from app.domain.entities.document import Document
from app.domain.repositories.base_repository import BaseRepository

# CRUD
class DocumentRepository(BaseRepository[Document]):
    ...