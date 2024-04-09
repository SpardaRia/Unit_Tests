"""Тестирование программы."""
import pytest

from HW_06.task_01.list_comparison import NumsLists


@pytest.fixture
def list1():
    """
    Возвращает список [1, 2, 3, 4, 5].
    """
    return [1, 2, 3, 4, 5]


@pytest.fixture
def list2():
    """Возвращает список [2, 3, 4, 5, 6]"""
    return [2, 3, 4, 5, 6]


def test_init(list1, list2):
    """Проверка корректности инициализации класса."""
    nums_list = NumsLists(list1, list2)
    assert nums_list.lst1 == list1
    assert nums_list.lst2 == list2


def test_averages(list1, list2):
    """Проверяет среднее значение списков, длинной более одного элемента."""
    nums_list = NumsLists(list1, list2)
    assert nums_list.get_lists_averages() == (3, 4)


@pytest.mark.parametrize('lst1, lst2, result', [([1, 2, 3], [], (2, 0)),
                                                ([], [1, 2, 3], (0, 2)), ([], [], (0, 0))])
def test_empty_averages(lst1, lst2, result):
    """Проверяет среднее значение если есть пустые списки"""
    nums_list = NumsLists(lst1, lst2)
    assert nums_list.get_lists_averages() == result


@pytest.mark.parametrize('lst1, lst2, result', [([1, 2, 3], [5], (2, 5)),
                                                ([5], [1, 2, 3], (5, 2)), ([5], [5], (5, 5))])
def test_one_elemented_averages(lst1, lst2, result):
    """Проверяет среднее значение, если в списках по одному элементу."""
    nums_list = NumsLists(lst1, lst2)
    assert nums_list.get_lists_averages() == result


def test_first_average_more(list1, list2, capfd):
    """Проверяет сообщение, если среднее значение первого списка больше второго."""
    nums_list = NumsLists(list2, list1)
    nums_list.compare_averages()
    captured = capfd.readouterr()
    assert captured.out.strip() == 'Первый список имеет большее среднее значение.'


def test_second_average_more(list1, list2, capfd):
    """Проверяет сообщение, если среднее значение второго списка больше первого."""
    nums_list = NumsLists(list1, list2)
    nums_list.compare_averages()
    captured = capfd.readouterr()
    assert captured.out.strip() == 'Второй список имеет большее среднее значение.'


def test_equal_averages(list1, capfd):
    """Проверяет сообщение, если средние значения списков равны."""
    nums_list = NumsLists(list1, list1)
    nums_list.compare_averages()
    captured = capfd.readouterr()
    assert captured.out.strip() == 'Средние значения равны.'