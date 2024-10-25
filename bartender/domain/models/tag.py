from dataclasses import dataclass

from bartender.domain.models.base import TimeStampedModel


@dataclass
class Tag(TimeStampedModel):
    name: str
