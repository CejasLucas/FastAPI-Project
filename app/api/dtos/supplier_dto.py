from pydantic import BaseModel, EmailStr

# ── Schemas ────────────────────────────────────────────────────────────────────
class SupplierCreateDTO(BaseModel):
    name: str
    email: EmailStr
    phone: str
    address: str
    locality: str
    nationality: str
    tax_id: str

class SupplierUpdateDTO(BaseModel):
    name: str | None = None
    email: EmailStr | None = None
    phone: str | None = None
    address: str | None = None
    locality: str | None = None
    nationality: str | None = None
    tax_id: str | None = None