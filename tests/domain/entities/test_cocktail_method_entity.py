from bartender.domain.models.base import EntityId
from bartender.domain.models.cocktail_method import CocktailMethod
from tests.domain.factories import CocktailMethodFactory


class TestCocktailMethodModel:
    """Test cases for CocktailMethod model."""
    def test_create_cocktail_method(self) -> None:
        cocktail_method: CocktailMethod = CocktailMethodFactory()
        assert isinstance(cocktail_method, CocktailMethod)
        assert isinstance(cocktail_method.id, EntityId)
        assert isinstance(cocktail_method.name, str)
        assert isinstance(cocktail_method.dilution_percentage, int)
