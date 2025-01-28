import pytest

from src.lesson_10_2 import calculate_taxes, calculate_tax


def test_calculate_taxes(prices, tax_rate):

    assert calculate_taxes(prices, tax_rate) == [11.53, 6.55, 10.96]

    with pytest.raises(ValueError) as exc_info_tax_rate:
        calculate_taxes(prices, -1)
    assert str(exc_info_tax_rate.value) == "Неверный налоговый процент"

    with pytest.raises(ValueError) as exc_info_price:
        calculate_taxes([0], tax_rate)
    assert str(exc_info_price.value) == "Неверная цена"


def test_calculate_tax(price, tax_rate, discount):

    assert calculate_tax(price, tax_rate) == 11.53

    # проверяем при цене отрицательной
    with pytest.raises(ValueError) as exc_info:
        calculate_tax(-1, tax_rate)
    assert str(exc_info.value) == "Неверная цена"

    # проверяем при налоговом проценте 0%
    with pytest.raises(ValueError) as exc_info:
        calculate_tax(price, 0)
    assert str(exc_info.value) == "Неверный налоговый процент"

    # проверяем при налоговом проценте 100%
    with pytest.raises(ValueError) as exc_info:
        calculate_tax(price, 100)
    assert str(exc_info.value) == "Неверный налоговый процент"

    # проверяем при налоговом проценте -1%
    with pytest.raises(ValueError) as exc_info:
        calculate_tax(price, -1)
    assert str(exc_info.value) == "Неверный налоговый процент"

    assert calculate_tax(price, tax_rate, discount) == 10.37

    with pytest.raises(TypeError) as exc_info:
        calculate_tax("", tax_rate)
    assert str(exc_info.value) == "Введены не цифровые значения"
