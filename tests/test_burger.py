import pytest
from unittest.mock import Mock
from praktikum.burger import Burger


@pytest.fixture
def bun_mock():
    bun = Mock()
    bun.get_price.return_value = 50
    bun.get_name.return_value = "White Bun"
    return bun


@pytest.fixture
def ingredient_mock():
    ing = Mock()
    ing.get_price.return_value = 10
    ing.get_name.return_value = "Cheese"
    ing.get_type.return_value = "FILLING"
    return ing


class TestBurger:
    def test_set_buns(self, bun_mock):
        burger = Burger()
        burger.set_buns(bun_mock)
        assert burger.bun == bun_mock

    def test_add_ingredient(self, ingredient_mock):
        burger = Burger()
        burger.add_ingredient(ingredient_mock)
        assert ingredient_mock in burger.ingredients

    def test_remove_ingredient(self, ingredient_mock):
        burger = Burger()
        burger.add_ingredient(ingredient_mock)
        burger.remove_ingredient(0)
        assert ingredient_mock not in burger.ingredients

    def test_move_ingredient(self, ingredient_mock):
        burger = Burger()
        ing2 = Mock()
        burger.add_ingredient(ingredient_mock)
        burger.add_ingredient(ing2)

        burger.move_ingredient(0, 1)
        assert burger.ingredients[1] == ingredient_mock

    def test_get_price(self, bun_mock, ingredient_mock):
        burger = Burger()
        burger.set_buns(bun_mock)
        burger.add_ingredient(ingredient_mock)
        burger.add_ingredient(ingredient_mock)

        # 2 булки по 50 + 2 ингредиента по 10 = 120
        assert burger.get_price() == 120

    def test_get_receipt(self, bun_mock, ingredient_mock):
        burger = Burger()
        burger.set_buns(bun_mock)
        burger.add_ingredient(ingredient_mock)

        receipt = burger.get_receipt()

        expected = (
            f"(==== {bun_mock.get_name()} ====)\n"
            f"= {ingredient_mock.get_type().lower()} {ingredient_mock.get_name()} =\n"
            f"(==== {bun_mock.get_name()} ====)\n\n"
            f"Price: {burger.get_price()}"
        )

        assert receipt == expected
