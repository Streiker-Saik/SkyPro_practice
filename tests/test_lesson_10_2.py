import pytest

from src.lesson_10_2 import calculate_taxes


def test_calculate_taxes(price, tax_rate):

    assert calculate_taxes(price, tax_rate) == [11.526, 6.554, 10.961]

    with pytest.raises(ValueError) as exc_info_tax_rate:
        calculate_taxes(price, -1)
    assert str(exc_info_tax_rate.value) == "Неверный налоговый процент"

    with pytest.raises(ValueError) as exc_info_price:
        calculate_taxes([0], tax_rate)
    assert str(exc_info_price.value) == "Неверная цена"
