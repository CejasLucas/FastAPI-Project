from uuid import UUID
from pydantic import BaseModel, ConfigDict


class BrandCreateDTO(BaseModel):
    name: str
    active: bool = True
    nationality: str


class BrandUpdateDTO(BaseModel):
    name: str | None = None
    active: bool | None = None
    nationality: str | None = None


class BrandDTO(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: UUID
    name: str
    active: bool
    nationality: str