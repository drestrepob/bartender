from dataclasses import dataclass
from bartender.domain.models.base import BaseModel
from bartender.domain.models.mixins.as_dict import DictSerializerMixin


@dataclass(slots=True)
class Tag(BaseModel, DictSerializerMixin):
    name: str
