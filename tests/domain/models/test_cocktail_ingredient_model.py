from bartender.domain.models.cocktail_ingredient import CocktailIngredient
from tests.domain.factories import CocktailIngredientFactory


class TestCocktailIngredientModel:
    """Test cases for CocktailIngredient model."""
    def test_create_cocktail_ingredient(self) -> None:
        cocktail_ingredient: CocktailIngredient = CocktailIngredientFactory()
        assert isinstance(cocktail_ingredient.is_optional, bool)
        assert cocktail_ingredient.amount
        assert cocktail_ingredient.unit
        assert cocktail_ingredient.note
        assert cocktail_ingredient.ingredient
