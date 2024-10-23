from abc import ABC, abstractmethod

from domain.models.cocktail_method import CocktailMethod
from domain.interfaces.repository import Repository


class CocktailMethodRepository(Repository[CocktailMethod], ABC):
    """Interface for the CocktailMethod repository."""

    @abstractmethod
    def add(self, cocktail_method: CocktailMethod) -> CocktailMethod:
        pass

    @abstractmethod
    def get(self, id_: int) -> CocktailMethod:
        pass

    @abstractmethod
    def delete(self, cocktail_method: CocktailMethod) -> None:
        pass

    @abstractmethod
    def list(self) -> list[CocktailMethod]:
        pass

    @abstractmethod
    def update(self, cocktail_method: CocktailMethod) -> CocktailMethod:
        pass
