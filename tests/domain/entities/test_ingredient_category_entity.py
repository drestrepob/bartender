from bartender.domain.models.base import EntityId
from bartender.domain.models.ingredient_category import IngredientCategory
from tests.domain.factories import IngredientCategoryFactory


class TestIngredientCategoryModel:
    """Test cases for IngredientCategory model."""
    def test_create_ingredient_category(self) -> None:
        ingredient_category: IngredientCategory = IngredientCategoryFactory()
        assert isinstance(ingredient_category, IngredientCategory)
        assert isinstance(ingredient_category.id, EntityId)
        assert isinstance(ingredient_category.name, str)
        assert isinstance(ingredient_category.description, str)
