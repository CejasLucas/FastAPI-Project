from pydantic import BaseModel

# ── Schemas ────────────────────────────────────────────────────────────────────
class CategoryCreateDTO(BaseModel):
    name: str
    description: str

class CategoryUpdateDTO(BaseModel):
    name: str | None = None
    description: str | None = None