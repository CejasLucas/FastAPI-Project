from app.domain.entities.supplier import Supplier
from app.infrastructure.database.models.supplier_model import SupplierModel

def to_domain(model: SupplierModel) -> Supplier:
    return Supplier(
        id=model.id,
        name=model.name,
        email=model.email,
        phone=model.phone,
        tax_id=model.tax_id,
        uploaded_at=model.uploaded_at
    )

def to_model(entity: Supplier) -> SupplierModel:
    return SupplierModel(
        id=entity.id,
        name=entity.name,
        email=entity.email,
        phone=entity.phone,
        tax_id=entity.tax_id,
        uploaded_at=entity.uploaded_at
    )
