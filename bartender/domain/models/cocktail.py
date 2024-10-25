from dataclasses import dataclass, field

from bartender.domain.models.base import TimeStampedModel
from bartender.domain.models.cocktail_method import CocktailMethod
from bartender.domain.models.cocktail_ingredient import CocktailIngredient
from bartender.domain.models.glass import Glass
from bartender.domain.models.mixins.as_dict import DictSerializerMixin
from bartender.domain.models.tag import Tag


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
