# https://contest.yandex.ru/contest/23390/run-report/52115791/
from typing import Union


def calculation_on_the_right(
    home_map: Union[str, list],
    count_place: int
) -> dict:
    """Находит расстояние от пустого участка до дома
        прямым проходом по карте и карту пустых участков.

        Ключевые аргументы:
        count_place -- количество участков
        home_map -- карта свободных/занятых участков
        """
    right_map = list()
    empty_map = list()
    distace_to_zero = 0
    for i in range(count_place):
        if home_map[i] == '0':
            distace_to_zero = 0
            empty_map.append(i)
            right_map.append(distace_to_zero)
        else:
            distace_to_zero += 1
            right_map.append(distace_to_zero)
    return {
        'right_map': right_map,
        'empty_map': empty_map
    }


def calculation_on_the_left(
    home_map: Union[str, list],
    count_place: int
) -> list:
    """Находит расстояние от пустого участка до дома
        обратным проходом по карте.

        Ключевые аргументы:
        count_place -- количество участков
        home_map -- карта свободных/занятых участков
        """
    left_map = list()
    distace_to_zero = 0
    for i in range(count_place-1, -1, -1):
        if home_map[i] == '0':
            distace_to_zero = 0
            left_map.append(distace_to_zero)
        else:
            distace_to_zero += 1
            left_map.append(distace_to_zero)
    return left_map[::-1]


def find_distance(
    home_map: Union[str, list],
    left_map: list,
    right_empty_map: dict,
    count_place: int
) -> list:
    """Находит расстояние от дома до ближайщего пустого участка.

        Ключевые аргументы:
        home_map -- карта свободных/занятых участков
        left_map -- карта расстояний от пустого до занятого участка
                    обратным проходом по карте
        right_empty_map -- карта расстояний от пустого до занятого участка
                            прямым проходом по карте и карта пустых участков
        count_place -- количество участков
        """
    result = list()
    empty_map = right_empty_map['empty_map']
    right_map = right_empty_map['right_map']
    len_empty_map = len(empty_map)
    if home_map[0] == '0':
        result.append(0)
        i = 0
    for i in range(0, empty_map[0]):
        result.append(left_map[i])
    for i in range(i+1, empty_map[len_empty_map-1]):
        if left_map[i] < right_map[i]:
            result.append(left_map[i])
        else:
            result.append(right_map[i])
    for i in range(i+1, count_place):
        result.append(right_map[i])
    return result


if __name__ == '__main__':
    input()
    home_map = input().split()
    count_place = len(home_map)
    right_empty_map = calculation_on_the_right(home_map, count_place)
    left_map = calculation_on_the_left(home_map, count_place)
    result = find_distance(home_map, left_map, right_empty_map, count_place)
    print(*result)
