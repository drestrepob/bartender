from dataclasses import dataclass

from domain.models.base import TimeStampedModel


@dataclass
class Tag(TimeStampedModel):
    name: str
