from dataclasses import dataclass

from bartender.domain.models.base import TimeStampedModel
from bartender.domain.models.mixins.as_dict import DictSerializerMixin


@dataclass
class IngredientCategory(TimeStampedModel, DictSerializerMixin):
    """Represents a category of ingredients."""
    name: str
    description: str
