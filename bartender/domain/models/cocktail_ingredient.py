from dataclasses import dataclass, field

from bartender.domain.models.base import TimeStampedModel
from bartender.domain.models.ingredient import Ingredient
from bartender.domain.models.mixins.as_dict import DictSerializerMixin


@dataclass
class CocktailIngredient(TimeStampedModel, DictSerializerMixin):
    """Represents an ingredient in a cocktail recipe."""
    is_optional: bool
    amount: float
    unit: str
    note: str

    # Relationships
    ingredient: Ingredient
    substitutes: list["CocktailIngredient"] = field(default_factory=list)
