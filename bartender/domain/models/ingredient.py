from dataclasses import dataclass

from bartender.domain.models.base import TimeStampedModel
from bartender.domain.models.ingredient_category import IngredientCategory
from bartender.domain.models.mixins.as_dict import DictSerializerMixin


@dataclass
class Ingredient(TimeStampedModel, DictSerializerMixin):
    """Represents an ingredient used in a cocktail recipe."""
    name: str
    description: str
    origin: str
    strength: float | None
    unit: str
    unit_cost: float
    image_url: str

    # Relationships
    category: IngredientCategory

    @property
    def proof(self) -> float:
        """
        The two main methods for indicating the alcoholic content of a beverage
        are alcohol-by-volume (ABV) and proof. In usa, a spirit’s proof is
        simply double the abv.

        Returns:
            The proof of the ingredient.
        """
        return self.strength * 2
