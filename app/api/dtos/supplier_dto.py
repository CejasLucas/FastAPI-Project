from uuid import UUID
from pydantic import BaseModel, EmailStr, ConfigDict


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


class SupplierDTO(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: UUID
    name: str
    email: str
    phone: str
    address: str
    locality: str
    nationality: str
    tax_id: str