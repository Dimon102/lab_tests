import main
import pytest


# Тест функции, находящей простые числа, меньше заданного n
class TestCalc:

    # Тестируем программу на коррктных данных. Функция возвращает списко элементов.
    def test_on_correct_n(self):
        assert main.calc("2+5") == 7

    # Тестируем программу на некоррктных данных. Функция вызывает исключение IndexError.
    def test_on_zero(self):
        with pytest.raises(IndexError):
            main.calc("2 + 5")

