from dataclasses import dataclass

from bartender.domain.models.base import TimeStampedModel
from bartender.domain.models.mixins.as_dict import DictSerializerMixin


@dataclass
class Glass(TimeStampedModel, DictSerializerMixin):
    """Represents a type of glassware."""
    name: str
    description: str
    capacity: int
    capacity_unit: str
