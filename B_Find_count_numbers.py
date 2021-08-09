# https://contest.yandex.ru/contest/23390/run-report/52116958/
from typing import Union


def sum_equal_button(field_button_numbers: list, j: int) -> int:
    """Находит кол-во клавиш с одинаковым числом

        Ключевые аргументы:
        field_button_numbers -- поле клавиш с числами
        j -- число на клавише
        """
    return field_button_numbers.count(j)


def sum_variants_button(
    field_button: Union[str, list],
    count_button: str
) -> int:
    """Находит сумму вариантов клавиш с одинаковым числом
                не превышающих заданное кол-во

        Ключевые аргументы:
        field_button -- поле клавиш
        count_button -- заданное возможное кол-во клавиш
        """
    field_button_numbers = list()
    result = 0
    for i in field_button:
        if i != '.':
            field_button_numbers.append(int(i))
    for j in set(field_button_numbers):
        if sum_equal_button(field_button_numbers, j) <= count_button * 2:
            result += 1
    return result


if __name__ == '__main__':
    count_button = int(input())
    field_button = list()
    for _ in range(0, 4):
        field_button.extend(list(input()))
    result = sum_variants_button(field_button, count_button)
    print(result)
