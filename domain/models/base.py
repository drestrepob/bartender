from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class TimeStampedModel:
    """A model that has a created and updated timestamp."""
    created_at: datetime = field(default_factory=datetime.now, init=False)
    updated_at: datetime = field(default_factory=datetime.now, init=False)
