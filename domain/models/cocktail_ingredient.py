from dataclasses import dataclass, field

from domain.models.ingredient import Ingredient
from domain.models.mixins.as_dict import DictSerializerMixin


@dataclass
class CocktailIngredient(DictSerializerMixin):
    """Represents an ingredient in a cocktail recipe."""
    is_optional: bool
    amount: float
    unit: str
    note: str

    # Relationships
    ingredient: Ingredient
    substitutes: list["CocktailIngredient"] = field(default_factory=list)
