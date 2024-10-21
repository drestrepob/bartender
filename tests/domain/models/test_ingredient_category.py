from domain.models.ingredient_category import IngredientCategory
from tests.domain.factories import IngredientCategoryFactory


class TestIngredientCategoryModel:
    """Test cases for IngredientCategory model."""
    def test_create_ingredient_category(self) -> None:
        ingredient_category: IngredientCategory = IngredientCategoryFactory()
        assert ingredient_category.name
        assert ingredient_category.description
        assert ingredient_category.created_at
        assert ingredient_category.updated_at
