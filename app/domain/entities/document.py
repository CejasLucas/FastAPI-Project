from uuid import UUID
from datetime import datetime
from dataclasses import dataclass, field


@dataclass
class Document:
    id: UUID | None = None

    file_url: str = ""

    filename: str = ""

    purchase_id: UUID | None = None

    uploaded_at: datetime = field(default_factory=datetime.now)