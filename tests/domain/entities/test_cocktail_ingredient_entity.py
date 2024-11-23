from bartender.domain.models.base import EntityId
from bartender.domain.models.cocktail_ingredient import CocktailIngredient
from bartender.domain.models.ingredient import Ingredient
from tests.domain.factories import CocktailIngredientFactory


class TestCocktailIngredientModel:
    """Test cases for CocktailIngredient model."""
    def test_create_cocktail_ingredient(self) -> None:
        cocktail_ingredient: CocktailIngredient = CocktailIngredientFactory()
        assert isinstance(cocktail_ingredient, CocktailIngredient)
        assert isinstance(cocktail_ingredient.id, EntityId)
        assert isinstance(cocktail_ingredient.is_optional, bool)
        assert isinstance(cocktail_ingredient.amount, float)
        assert isinstance(cocktail_ingredient.unit, str)
        assert isinstance(cocktail_ingredient.note, str)
        assert isinstance(cocktail_ingredient.ingredient, Ingredient)
        assert isinstance(cocktail_ingredient.substitutes, list)
        assert len(cocktail_ingredient.substitutes) == 0
