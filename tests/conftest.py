import pytest

@pytest.fixture
def price():
    return [10.2, 5.8, 9.7]

@pytest.fixture
def tax_rate():
    return 13.0