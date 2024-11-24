from abc import ABC, abstractmethod

from bartender.domain.models.base import EntityId
from bartender.domain.models.cocktail import Cocktail
from bartender.domain.interfaces.repository import Repository


class CocktailRepository(Repository[Cocktail], ABC):
    """Interface for the Cocktail repository."""

    @abstractmethod
    def add(self, cocktail: Cocktail) -> Cocktail:
        pass

    @abstractmethod
    def get(self, id_: EntityId) -> Cocktail:
        pass

    @abstractmethod
    def delete(self, cocktail: Cocktail) -> None:
        pass

    @abstractmethod
    def list(self) -> list[Cocktail]:
        pass

    @abstractmethod
    def update(self, id_: EntityId, fields: dict) -> None:
        pass