from bartender.domain.models.base import EntityId
from bartender.domain.models.cocktail import Cocktail
from bartender.domain.models.cocktail_method import CocktailMethod
from bartender.domain.models.glass import Glass
from tests.domain.factories import CocktailFactory


class TestCocktailModel:
    """Test cases for Cocktail model."""
    def test_create_cocktail(self) -> None:
        cocktail: Cocktail = CocktailFactory()
        assert isinstance(cocktail, Cocktail)
        assert isinstance(cocktail.id, EntityId)
        assert isinstance(cocktail.name, str)
        assert isinstance(cocktail.description, str)
        assert isinstance(cocktail.image_url, str)
        assert isinstance(cocktail.garnish, str)
        assert isinstance(cocktail.rating, int)
        assert isinstance(cocktail.ingredients, list)
        assert isinstance(cocktail.tags, list)
        assert isinstance(cocktail.method, CocktailMethod)
        assert isinstance(cocktail.glass, Glass)
