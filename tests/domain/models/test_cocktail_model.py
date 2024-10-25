from bartender.domain.models.cocktail import Cocktail
from tests.domain.factories import CocktailFactory


class TestCocktailModel:
    """Test cases for Cocktail model."""
    def test_create_cocktail(self) -> None:
        cocktail: Cocktail = CocktailFactory()
        assert cocktail.name
        assert cocktail.description
        assert cocktail.instructions
        assert cocktail.image_url
        assert cocktail.garnish
        assert cocktail.rating
        assert cocktail.ingredients
        assert cocktail.tags
        assert cocktail.method
        assert cocktail.glass
        assert cocktail.created_at
        assert cocktail.updated_at
