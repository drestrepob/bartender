from abc import ABC, abstractmethod
from typing import Generic, TypeVar

from bartender.domain.models.base import EntityId

T = TypeVar("T")


class Repository(Generic[T], ABC):
    """Abstract class that represents a repository."""

    @abstractmethod
    def add(self, entity: T) -> None:
        pass

    @abstractmethod
    def get(self, id_: EntityId) -> T:
        pass

    @abstractmethod
    def delete(self, entity: T) -> None:
        pass
