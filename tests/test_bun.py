import pytest
from praktikum.bun import Bun


class TestBun:
    def test_bun_init(self):
        bun = Bun("Белая булочка", 100.0)
        assert bun.name == "Белая булочка"
        assert bun.price == 100.0

    def test_get_name(self):
        bun = Bun("Черная булочка", 120.0)
        assert bun.get_name() == "Черная булочка"

    def test_get_price(self):
        bun = Bun("Сырная булочка", 150.0)
        assert bun.get_price() == 150.0
