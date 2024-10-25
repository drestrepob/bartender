from dataclasses import dataclass

from bartender.domain.models.base import TimeStampedModel
from bartender.domain.models.mixins.as_dict import DictSerializerMixin


@dataclass
class CocktailMethod(TimeStampedModel, DictSerializerMixin):
    name: str
    dilution_percentage: int
