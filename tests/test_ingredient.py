import pytest
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_FILLING, INGREDIENT_TYPE_SAUCE


class TestIngredient:
    @pytest.mark.parametrize("ing_type,name,price", [
        (INGREDIENT_TYPE_FILLING, "Cheese", 2.5),
        (INGREDIENT_TYPE_SAUCE, "Ketchup", 1.0)
    ])
    def test_ingredient_init(self, ing_type, name, price):
        ing = Ingredient(ing_type, name, price)
        assert ing.type == ing_type
        assert ing.name == name
        assert ing.price == price

    def test_get_price(self):
        ing = Ingredient("FILLING", "Bacon", 3.0)
        assert ing.get_price() == 3.0

    def test_get_name(self):
        ing = Ingredient("SAUCE", "Mayo", 1.5)
        assert ing.get_name() == "Mayo"

    def test_get_type(self):
        ing = Ingredient("FILLING", "Lettuce", 0.5)
        assert ing.get_type() == "FILLING"
