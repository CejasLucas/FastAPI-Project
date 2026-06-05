from uuid import UUID
from datetime import datetime
from dataclasses import dataclass, field


@dataclass
class Supplier:
    id: UUID | None = None

    name: str = ""

    email: str = ""

    phone: str = ""

    tax_id: str = ""

    uploaded_at: datetime = field(default_factory=datetime.now)