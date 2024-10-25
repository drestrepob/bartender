import factory

from bartender.domain.models.cocktail import Cocktail
from bartender.domain.models.cocktail_ingredient import CocktailIngredient
from bartender.domain.models.cocktail_method import CocktailMethod
from bartender.domain.models.glass import Glass
from bartender.domain.models.ingredient import Ingredient
from bartender.domain.models.ingredient_category import IngredientCategory
from bartender.domain.models.tag import Tag


class CocktailMethodFactory(factory.Factory):
    class Meta:
        model = CocktailMethod

    name = factory.Faker("word")
    dilution_percentage = factory.Faker("random_int", min=1, max=100)


class GlassFactory(factory.Factory):
    class Meta:
        model = Glass

    name = factory.Faker("word")
    description = factory.Faker("text")
    capacity = factory.Faker("random_int", min=50, max=1_000)
    capacity_unit = "ml"


class IngredientCategoryFactory(factory.Factory):
    class Meta:
        model = IngredientCategory

    name = factory.Faker("word")
    description = factory.Faker("text")


class TagFactory(factory.Factory):
    class Meta:
        model = Tag

    name = factory.Faker("word")


class IngredientFactory(factory.Factory):
    class Meta:
        model = Ingredient

    name = factory.Faker("word")
    description = factory.Faker("text")
    origin = factory.Faker("country")
    strength = factory.Faker("random_int", min=1, max=100)
    unit = "ml"
    unit_cost = factory.Faker("random_int", min=100, max=10_000)
    image_url = factory.Faker("image_url")
    category = factory.SubFactory(IngredientCategoryFactory)


class CocktailIngredientFactory(factory.Factory):
    class Meta:
        model = CocktailIngredient

    is_optional = factory.Faker("boolean")
    amount = factory.Faker("random_int", min=1, max=100)
    unit = "ml"
    note = factory.Faker("sentence")
    ingredient = factory.SubFactory(IngredientFactory)


class CocktailFactory(factory.Factory):
    class Meta:
        model = Cocktail

    name = factory.Faker("word")
    description = factory.Faker("country")
    instructions = factory.Faker("text")
    image_url = factory.Faker("image_url")
    garnish = factory.Faker("word")
    rating = factory.Faker("random_int", min=1, max=5)
    glass = factory.SubFactory(GlassFactory)
    method = factory.SubFactory(CocktailMethodFactory)
    tags = factory.List([factory.SubFactory(TagFactory)])
    ingredients = factory.List([factory.SubFactory(CocktailIngredientFactory)])
