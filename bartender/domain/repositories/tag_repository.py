from abc import ABC, abstractmethod

from domain.models.tag import Tag
from domain.interfaces.repository import Repository


class TagRepository(Repository[Tag], ABC):
    """Interface for the Tag repository."""

    @abstractmethod
    def add(self, tag: Tag) -> Tag:
        pass

    @abstractmethod
    def get(self, id_: int) -> Tag:
        pass

    @abstractmethod
    def delete(self, tag: Tag) -> None:
        pass

    @abstractmethod
    def list(self) -> list[Tag]:
        pass

    @abstractmethod
    def update(self, tag: Tag) -> Tag:
        pass
