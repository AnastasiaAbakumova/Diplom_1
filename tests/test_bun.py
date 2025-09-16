import pytest
from praktikum.bun import Bun


def test_bun_init():
    bun = Bun("Белая булочка", 100.0)
    assert bun.name == "Белая булочка"
    assert bun.price == 100.0


def test_get_name():
    bun = Bun("Черная булочка", 120.0)
    assert bun.get_name() == "Черная булочка"


def test_get_price():
    bun = Bun("Сырная булочка", 150.0)
    assert bun.get_price() == 150.0
