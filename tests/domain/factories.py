import factory

from bartender.domain.constants.models.constraints import (
    MAX_COCKTAIL_INGREDIENT_AMOUNT,
    MAX_COCKTAIL_RATING,
    MAX_DILUTION_PERCENTAGE,
    MAX_GLASS_CAPACITY,
    MAX_INGREDIENT_STRENGTH,
    MAX_INGREDIENT_UNIT_COST,
    MIN_COCKTAIL_INGREDIENT_AMOUNT,
    MIN_COCKTAIL_RATING,
    MIN_DILUTION_PERCENTAGE,
    MIN_GLASS_CAPACITY,
    MIN_INGREDIENT_STRENGTH,
    MIN_INGREDIENT_UNIT_COST,
)
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

    name = factory.Faker("uuid4")
    dilution_percentage = factory.Faker("random_int", min=MIN_DILUTION_PERCENTAGE, max=MAX_DILUTION_PERCENTAGE)


class GlassFactory(factory.Factory):
    class Meta:
        model = Glass

    name = factory.Faker("uuid4")
    description = factory.Faker("text")
    capacity = factory.Faker("random_int", min=MIN_GLASS_CAPACITY, max=MAX_GLASS_CAPACITY)
    capacity_unit = "ml"


class IngredientCategoryFactory(factory.Factory):
    class Meta:
        model = IngredientCategory

    name = factory.Faker("uuid4")
    description = factory.Faker("text")


class TagFactory(factory.Factory):
    class Meta:
        model = Tag

    name = factory.Faker("uuid4")


class IngredientFactory(factory.Factory):
    class Meta:
        model = Ingredient

    name = factory.Faker("uuid4")
    description = factory.Faker("text")
    origin = factory.Faker("country")
    strength = factory.Faker(
        "pyfloat", min_value=MIN_INGREDIENT_STRENGTH, max_value=MAX_INGREDIENT_STRENGTH
    )
    unit = "ml"
    unit_cost = factory.Faker(
        "pyfloat", positive=True, min_value=MIN_INGREDIENT_UNIT_COST, max_value=MAX_INGREDIENT_UNIT_COST
    )
    image_url = factory.Faker("image_url")
    category = factory.SubFactory(IngredientCategoryFactory)


class CocktailIngredientFactory(factory.Factory):
    class Meta:
        model = CocktailIngredient

    is_optional = factory.Faker("boolean")
    amount = factory.Faker(
        "pyfloat", min_value=MIN_COCKTAIL_INGREDIENT_AMOUNT, max_value=MAX_COCKTAIL_INGREDIENT_AMOUNT
    )
    unit = "ml"
    note = factory.Faker("sentence")
    ingredient = factory.SubFactory(IngredientFactory)


class CocktailFactory(factory.Factory):
    class Meta:
        model = Cocktail

    name = factory.Faker("uuid4")
    description = factory.Faker("text")
    instructions = factory.Faker("text")
    image_url = factory.Faker("image_url")
    garnish = factory.Faker("word")
    rating = factory.Faker("random_int", min=MIN_COCKTAIL_RATING, max=MAX_COCKTAIL_RATING)
    glass = factory.SubFactory(GlassFactory)
    method = factory.SubFactory(CocktailMethodFactory)
    tags = factory.List([factory.SubFactory(TagFactory)])
    ingredients = factory.List([factory.SubFactory(CocktailIngredientFactory)])
