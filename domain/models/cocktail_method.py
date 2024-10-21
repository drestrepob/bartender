from dataclasses import dataclass

from domain.models.base import TimeStampedModel
from domain.models.mixins.as_dict import DictSerializerMixin


@dataclass
class CocktailMethod(TimeStampedModel, DictSerializerMixin):
    name: str
    dilution_percentage: int
