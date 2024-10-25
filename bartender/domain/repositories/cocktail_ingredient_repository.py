from abc import ABC, abstractmethod

from bartender.domain.models.cocktail_ingredient import CocktailIngredient
from bartender.domain.interfaces.repository import Repository


class CocktailIngredientRepository(Repository[CocktailIngredient], ABC):
    """Interface for the CocktailIngredient repository."""

    @abstractmethod
    def add(self, cocktail_ingredient: CocktailIngredient) -> CocktailIngredient:
        pass

    @abstractmethod
    def get(self, id_: int) -> CocktailIngredient:
        pass

    @abstractmethod
    def delete(self, cocktail_ingredient: CocktailIngredient) -> None:
        pass

    @abstractmethod
    def list(self) -> list[CocktailIngredient]:
        pass

    @abstractmethod
    def update(self, cocktail_ingredient: CocktailIngredient) -> CocktailIngredient:
        pass
