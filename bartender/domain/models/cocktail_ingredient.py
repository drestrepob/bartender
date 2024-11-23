from collections.abc import Sequence
from dataclasses import dataclass, field

from bartender.domain.models.base import BaseModel
from bartender.domain.models.ingredient import Ingredient
from bartender.domain.models.mixins.as_dict import DictSerializerMixin


@dataclass(slots=True)
class CocktailIngredient(BaseModel, DictSerializerMixin):
    """Represents an ingredient in a cocktail recipe."""
    is_optional: bool
    amount: float
    unit: str  # TODO: Model as a ValueObject
    note: str

    # Relationships
    ingredient: Ingredient
    substitutes: Sequence["CocktailIngredient"] = field(default_factory=list)
