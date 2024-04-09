"""Сравнивает два списка."""

from __future__ import annotations


class NumsLists:
    """Сравнивает средние значения списков."""

    def __init__(self, lst1: list[int | float], lst2: list[int | float]):
        """
        Инициализирует экземпляр класса двумя списками.

        Параметры:
            lst1 (list[int | float]): Первый список.
            lst2 (list[int | float]): Второй список.
        """
        self.lst1 = lst1
        self.lst2 = lst2

    def get_lists_averages(self) -> tuple[float, float]:
        """
        Вычисляет и возвращает средние значения списков.

        Возвращает:
            tuple[float, float]: Кортеж, содержащий среднее значение `lst1` и `lst2`.
        """
        avg1 = 0
        if self.lst1:
            avg1 = sum(self.lst1) / len(self.lst1)

        avg2 = 0
        if self.lst2:
            avg2 = sum(self.lst2) / len(self.lst2)

        return avg1, avg2

    def compare_averages(self) -> None:
        """
        Сравнивает средние значения списков и выводит результат.

        Метод использует `get_lists_averages` для вычисления среднего значения и сравнивает их.
        
        Этот метод вычисляет средние значения двух списков с помощью метода `get_lists_averages`
        и сравнивает их.

        Параметры:
            self (ClassName): Экземпляр класса.

        Возвращает:
            None: Этот метод ничего не возвращает.
        """
        avg1, avg2 = self.get_lists_averages()
        if avg1 > avg2:
            print('Первый список имеет большее среднее значение.')
        elif avg1 < avg2:
            print('Второй список имеет большее среднее значение.')
        else:
            print('Средние значения равны.')
