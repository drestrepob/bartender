from typing import Final

# Glass capacity constraints
MIN_GLASS_CAPACITY: Final[int] = 10
MAX_GLASS_CAPACITY: Final[int] = 5_000

# Dilution constraints
MIN_DILUTION_PERCENTAGE: Final[int] = 0
MAX_DILUTION_PERCENTAGE: Final[int] = 100

# Ingredient strength constraints
MIN_INGREDIENT_STRENGTH: Final[int] = 0
MAX_INGREDIENT_STRENGTH: Final[int] = 100

# Ingredient unit cost constraints
MIN_INGREDIENT_UNIT_COST: Final[int] = 1
MAX_INGREDIENT_UNIT_COST: Final[int] = 100_000

# Cocktail ingredient amount constraints
MIN_COCKTAIL_INGREDIENT_AMOUNT: Final[int] = 1
MAX_COCKTAIL_INGREDIENT_AMOUNT: Final[int] = 1_000

# Cocktail rating constraints
MIN_COCKTAIL_RATING: Final[int] = 0
MAX_COCKTAIL_RATING: Final[int] = 5
