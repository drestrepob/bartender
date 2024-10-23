from abc import ABC, abstractmethod
from typing import Any, Generic, TypeVar

T = TypeVar("T")


class Repository(Generic[T], ABC):
    """Abstract class that represents a repository."""

    @abstractmethod
    def add(self, entity: T) -> None:
        pass

    @abstractmethod
    def get(self, id_: Any) -> T:
        pass

    @abstractmethod
    def delete(self, entity: T) -> None:
        pass
