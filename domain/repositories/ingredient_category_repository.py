from abc import ABC, abstractmethod

from domain.models.ingredient_category import IngredientCategory
from domain.interfaces.repository import Repository


class IngredientCategoryRepository(Repository[IngredientCategory], ABC):
    """Interface for the IngredientCategory repository."""

    @abstractmethod
    def add(self, ingredient_category: IngredientCategory) -> IngredientCategory:
        pass

    @abstractmethod
    def get(self, id_: int) -> IngredientCategory:
        pass

    @abstractmethod
    def delete(self, ingredient_category: IngredientCategory) -> None:
        pass

    @abstractmethod
    def list(self) -> list[IngredientCategory]:
        pass

    @abstractmethod
    def update(self, ingredient_category: IngredientCategory) -> IngredientCategory:
        pass
