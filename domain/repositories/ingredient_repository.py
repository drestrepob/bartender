from abc import ABC, abstractmethod

from domain.models.ingredient import Ingredient
from domain.interfaces.repository import Repository


class IngredientRepository(Repository[Ingredient], ABC):
    """Interface for the Ingredient repository."""

    @abstractmethod
    def add(self, ingredient: Ingredient) -> Ingredient:
        pass

    @abstractmethod
    def get(self, id_: int) -> Ingredient:
        pass

    @abstractmethod
    def delete(self, ingredient: Ingredient) -> None:
        pass

    @abstractmethod
    def list(self) -> list[Ingredient]:
        pass

    @abstractmethod
    def update(self, ingredient: Ingredient) -> Ingredient:
        pass
