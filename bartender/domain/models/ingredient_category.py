from dataclasses import dataclass

from bartender.domain.models.base import BaseModel
from bartender.domain.models.mixins.as_dict import DictSerializerMixin


@dataclass(slots=True)
class IngredientCategory(BaseModel, DictSerializerMixin):
    """Represents a category of ingredients."""
    name: str
    description: str
