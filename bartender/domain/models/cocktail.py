from collections.abc import Sequence
from dataclasses import dataclass, field

from bartender.domain.models.base import BaseModel
from bartender.domain.models.cocktail_method import CocktailMethod
from bartender.domain.models.cocktail_ingredient import CocktailIngredient
from bartender.domain.models.glass import Glass
from bartender.domain.models.mixins.as_dict import DictSerializerMixin
from bartender.domain.models.tag import Tag


@dataclass(slots=True)
class Cocktail(BaseModel, DictSerializerMixin):
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
    tags: Sequence[Tag] = field(default_factory=list)
    ingredients: Sequence[CocktailIngredient] = field(default_factory=list)
