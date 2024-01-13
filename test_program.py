

import pytest

@pytest.fixture
def list_comparator():
    return ListComparator([1, 2, 3], [4, 5, 6])

def test_calculate_average(list_comparator):
    assert list_comparator.calculate_average([1, 2, 3]) == 2.0
    assert list_comparator.calculate_average([]) == 0

def test_compare_lists(list_comparator):
    assert list_comparator.compare_lists() == "Второй список имеет большее среднее значение"

def test_compare_lists_equal(list_comparator):
    list_comparator.list2 = [1, 2, 3]
    assert list_comparator.compare_lists() == "Средние значения равны"
