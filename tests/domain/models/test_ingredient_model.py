from bartender.domain.models.ingredient import Ingredient
from tests.domain.factories import IngredientFactory


class TestIngredientModel:
    """Test cases for Ingredient model."""
    def test_create_ingredient(self) -> None:
        ingredient: Ingredient = IngredientFactory()
        assert ingredient.name
        assert ingredient.description
        assert ingredient.origin
        assert ingredient.strength
        assert ingredient.unit
        assert ingredient.unit_cost
        assert ingredient.image_url
        assert ingredient.category
        assert ingredient.created_at
        assert ingredient.updated_at
        assert ingredient.proof == ingredient.strength * 2
