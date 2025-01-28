def calculate_taxes(prices: list[float], tax_rate: float) -> list[float]:
    """Функция вычисляет стоимость товаров с учётом налога."""

    if tax_rate < 0:
        raise ValueError("Неверный налоговый процент")

    taxed_prices = []

    for price in prices:
        if price <= 0:
            raise ValueError("Неверная цена")
        tax = price * tax_rate / 100
        taxed_prices.append(round(price + tax, 2))

    return taxed_prices


def calculate_tax(price: list[float], tax_rate: float, discount: float = 0.0) -> list[float]:
    """Функция вычисляет стоимость товара с учётом налога."""

    if (
        not isinstance(price, (int, float))
        or not isinstance(tax_rate, (int, float))
        or not isinstance(discount, (int, float))
    ):
        raise TypeError("Введены не цифровые значения")

    if price < 0:
        raise ValueError("Неверная цена")

    if tax_rate <= 0 or tax_rate >= 100:
        raise ValueError("Неверный налоговый процент")

    tax = price * tax_rate / 100

    if discount == 0.0:
        result = price + tax

    else:
        price_discount = (price + tax) * discount / 100
        result = price + tax - price_discount

    return round(result, 2)
