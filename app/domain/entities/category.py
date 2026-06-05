from uuid import UUID
from datetime import datetime
from dataclasses import dataclass, field

@dataclass
class Category:
    id: UUID | None = None

    name: str = ""

    description: str | None = None

    uploaded_at: datetime = field(default_factory=datetime.now)