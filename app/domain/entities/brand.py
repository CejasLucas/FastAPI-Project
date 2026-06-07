from uuid import UUID
from datetime import datetime
from dataclasses import dataclass, field


@dataclass
class Brand:
    id: UUID | None = None

    name: str = ""

    active: bool = True

    nationality: str = ""

    uploaded_at: datetime = field(default_factory=datetime.now)