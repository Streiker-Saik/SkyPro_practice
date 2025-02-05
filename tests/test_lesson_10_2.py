import pytest

from src.lesson_10_2 import calculate_taxes, calculate_tax

@pytest.fixture()
def prices():
    return [100, 200, 300]
@pytest.mark.parametrize("tax_rate, expended",[(10, [110, 220, 330]),
                                               (15, [115, 230, 345]),
                                               (20, [120, 240, 360])])
def test_calculate_taxes(prices, tax_rate, expended):
    assert calculate_taxes(prices, tax_rate) == expended

def test_calculate_taxes_invalid_taxes(prices):
    with pytest.raises(ValueError):
        calculate_taxes(prices, tax_rate=-1)
    # assert str(exc_info_tax_rate.value) == "Неверный налоговый процент"

def test_calculate_taxes_invalid_price(prices):
    with pytest.raises(ValueError) as exc_info_price:
        calculate_taxes([0, -1], tax_rate=10)
    # assert str(exc_info_price.value) == "Неверная цена"

@pytest.mark.parametrize("price, tax_rate, expended",[(100, 10, 110), (50, 5, 52.5)])
def test_calculate_tax(price, tax_rate, expended):
    assert calculate_tax(price, tax_rate) == expended


def test_calculate_tax_invalid_price():
    with pytest.raises(ValueError):
        calculate_tax(-1, 10)
    # # проверяем при цене отрицательной
    # with pytest.raises(ValueError) as exc_info:
    #     calculate_tax(-1, tax_rate)
    # assert str(exc_info.value) == "Неверная цена"


def test_calculate_tax_invalid_taxes_below_zero():
    with pytest.raises(ValueError):
        calculate_tax(100, -1)
    # # проверяем при налоговом проценте 0%
    # with pytest.raises(ValueError) as exc_info:
    #     calculate_tax(price, 0)
    # assert str(exc_info.value) == "Неверный налоговый процент"


def test_calculate_tax_invalid_taxes_below_zero():
    with pytest.raises(ValueError):
        calculate_tax(100, 1000)
    # # проверяем при налоговом проценте 100%
    # with pytest.raises(ValueError) as exc_info:
    #     calculate_tax(price, 100)
    # assert str(exc_info.value) == "Неверный налоговый процент"


@pytest.mark.parametrize("price, tax_rate, discount, expended", [(100, 10, 0, 110),
                                                                 (100, 10, 10, 99.0),
                                                                 (100, 10, 100, 0)])
def test_calculate_tax_with_discount(price, tax_rate, discount, expended):
    assert calculate_tax(price, tax_rate, discount=discount) == expended

def test_calculate_tax_not_discount():
    assert calculate_tax(100, 10, ) == 110
    # assert calculate_tax(price, tax_rate, discount) == 10.37


@pytest.mark.parametrize("round_digits, expended", [(0, 99),
                                                    (1, 99.4),
                                                    (2, 99.42),
                                                    (3, 99.425)])
def test_calculate_tax_round(round_digits,  expended):
    assert calculate_tax(100, 2.5, discount=3, round_digits=round_digits) == expended


@pytest.mark.parametrize("price, tax_rate, discount, round_digits,", [("100", 10, 0, 1),
                                                                      (100, "10", 0, 1),
                                                                      (100, 10, "0", 1),
                                                                      (100, 10, 0, "1")])
def test_calculate_tax_wrong_type(price, tax_rate, discount, round_digits):
    with pytest.raises(TypeError):
        calculate_tax(price, tax_rate, discount=discount, round_digits=round_digits)
    # # проверяем при налоговом проценте -1%
    # with pytest.raises(ValueError) as exc_info:
    #     calculate_tax(price, -1)
    # assert str(exc_info.value) == "Неверный налоговый процент"
    #
    #
    # with pytest.raises(TypeError) as exc_info:
    #     calculate_tax("", tax_rate)
    # assert str(exc_info.value) == "Введены не цифровые значения"


def test_calculate_tax_wrong_type():
    with pytest.raises(TypeError):
        calculate_tax(2, 2, 3, 1)
