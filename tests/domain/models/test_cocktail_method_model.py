from bartender.domain.models.cocktail_method import CocktailMethod
from tests.domain.factories import CocktailMethodFactory


class TestCocktailMethodModel:
    """Test cases for CocktailMethod model."""
    def test_create_cocktail_method(self) -> None:
        cocktail_method: CocktailMethod = CocktailMethodFactory()
        assert cocktail_method.name
        assert cocktail_method.dilution_percentage
        assert cocktail_method.created_at
        assert cocktail_method.updated_at
