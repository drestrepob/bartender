from dataclasses import dataclass, field
from datetime import datetime
from typing import Any

from fastnanoid import generate

from bartender.domain.constants.models.field_names import ID_STR, VALUE_STR


@dataclass(frozen=True)
class EntityId:
    """A unique identifier for an entity."""
    value: str = field(default="")

    def __post_init__(self) -> None:
        if not self.value:
            object.__setattr__(self, VALUE_STR, generate())

    def __str__(self) -> str:
        return self.value

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__}>({self.value})"

    def __hash__(self) -> int:
        return hash(self.value)

    def __eq__(self, other: Any) -> bool:
        if isinstance(other, type(self)):
            return self.value == other.value
        return False


@dataclass(kw_only=True)
class BaseModel:
    """Base model for all models."""
    id: EntityId = field(default_factory=EntityId)

    def __post_init__(self) -> None:
        if not isinstance(self.id, EntityId):
            object.__setattr__(self, ID_STR, EntityId(value=str(self.id)))

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__}>({self.id.value})"

    def __str__(self) -> str:
        return self.id.value

    def __eq__(self, other: Any) -> bool:
        if isinstance(other, type(self)):
            return self.id == other.id
        return False
