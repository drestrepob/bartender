from abc import ABC, abstractmethod

from bartender.domain.models.base import EntityId
from bartender.domain.models.ingredient_category import IngredientCategory
from bartender.domain.interfaces.repository import Repository


class IngredientCategoryRepository(Repository[IngredientCategory], ABC):
    """Interface for the IngredientCategory repository."""

    @abstractmethod
    def add(self, ingredient_category: IngredientCategory) -> IngredientCategory:
        pass

    @abstractmethod
    def get(self, id_: EntityId) -> IngredientCategory:
        pass

    @abstractmethod
    def delete(self, ingredient_category: IngredientCategory) -> None:
        pass

    @abstractmethod
    def list(self) -> list[IngredientCategory]:
        pass

    @abstractmethod
    def update(self, id_: EntityId, fields: dict) -> None:
        pass
