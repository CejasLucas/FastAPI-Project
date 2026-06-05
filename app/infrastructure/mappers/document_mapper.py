from app.domain.entities.document import Document
from app.infrastructure.database.models.document_model import DocumentModel

def to_domain(model: DocumentModel) -> Document:
    return Document(
        id=model.id,
        file_url=model.file_url,
        filename=model.filename,
        purchase_id=model.purchase_id,
        uploaded_at=model.uploaded_at
    )


def to_model(entity: Document) -> DocumentModel:
    return DocumentModel(
        id=entity.id,
        file_url=entity.file_url,
        filename=entity.filename,
        purchase_id=entity.purchase_id,
        uploaded_at=entity.uploaded_at
    )
