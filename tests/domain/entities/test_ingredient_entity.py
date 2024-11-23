from bartender.domain.models.base import EntityId
from bartender.domain.models.ingredient_category import IngredientCategory
from bartender.domain.models.ingredient import Ingredient
from tests.domain.factories import IngredientFactory


class TestIngredientModel:
    """Test cases for Ingredient model."""
    def test_create_ingredient(self) -> None:
        ingredient: Ingredient = IngredientFactory()
        assert isinstance(ingredient, Ingredient)
        assert isinstance(ingredient.id, EntityId)
        assert isinstance(ingredient.name, str)
        assert isinstance(ingredient.description, str)
        assert isinstance(ingredient.origin, str)
        assert isinstance(ingredient.strength, float)
        assert isinstance(ingredient.unit, str)
        assert isinstance(ingredient.unit_cost, float)
        assert isinstance(ingredient.image_url, str)
        assert isinstance(ingredient.category, IngredientCategory)
        assert ingredient.proof == ingredient.strength * 2
