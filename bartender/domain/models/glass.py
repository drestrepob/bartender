from dataclasses import dataclass

from bartender.domain.models.base import BaseModel
from bartender.domain.models.mixins.as_dict import DictSerializerMixin


@dataclass(slots=True)
class Glass(BaseModel, DictSerializerMixin):
    """Represents a type of glassware."""
    name: str
    description: str
    capacity: int
    capacity_unit: str
