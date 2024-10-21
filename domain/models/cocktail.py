from dataclasses import dataclass, field

from domain.models.base import TimeStampedModel
from domain.models.cocktail_method import CocktailMethod
from domain.models.cocktail_ingredient import CocktailIngredient
from domain.models.glass import Glass
from domain.models.mixins.as_dict import DictSerializerMixin
from domain.models.tag import Tag


@dataclass
class Cocktail(TimeStampedModel, DictSerializerMixin):
    """Represents a cocktail recipe."""
    name: str
    description: str
    instructions: str
    image_url: str
    garnish: str
    rating: int

    # Relationships
    glass: Glass
    method: CocktailMethod
    tags: list[Tag] = field(default_factory=list)
    ingredients: list[CocktailIngredient] = field(default_factory=list)
