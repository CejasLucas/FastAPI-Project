from pydantic import BaseModel

# ── Schemas ────────────────────────────────────────────────────────────────────
class BrandCreateDTO(BaseModel):
    name: str
    nationality: str
    active: bool = True

class BrandUpdateDTO(BaseModel):
    name: str | None = None
    nationality: str | None = None
    active: bool | None = None
