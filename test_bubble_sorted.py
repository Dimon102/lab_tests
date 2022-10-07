import pytest
import main


# Тест функции, которая проверяет, что значения во входном списке упорядочены от мин к макс
class TestIsOrdered:

    # Функция возвращает данные для выполнения теста - упорядоченный от мин к макс список
    @pytest.fixture
    def ordered_example(self):
        return [1, 2, 3]

    # Функция возвращает данные для выполнения теста - неупорядоченный список
    @pytest.fixture
    def unordered_example(self):
        return [1, 3, 2]

    # Функция возвращает данные для выполнения теста - массив равных по величине значений
    @pytest.fixture
    def equal_example(self):
        return [1, 1, 1]

    # Тест функции на упорядоченных от мин к макс значениях
    def test_on_ordered(self, ordered_example):
        assert main.is_sorted_from_min_to_max(ordered_example) is True

    # Тест функции на неупорядоченных значениях
    def test_on_unordered(self, unordered_example):
        assert main.is_sorted_from_min_to_max(unordered_example) is False

    # Тест функции на равных по величине значениях
    def test_on_equal(self, equal_example):
        assert main.is_sorted_from_min_to_max(equal_example) is True