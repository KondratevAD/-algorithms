# https://contest.yandex.ru/contest/24735/run-report/52298865/
from dataclasses import dataclass


@dataclass(order=True)
class Player:
    score: int
    penalty: int
    name: str

    def __post_init__(self):
        self.score = -int(self.score)
        self.penalty = int(self.penalty)


def quick_sort(arr: list, less: int, greater: int) -> int:
    """Сортирует список.

    Ключевые аргументы:
    arr -- сортируемый список.
    less -- индекс начального элемента.
    greater -- индекс конечного элемента.
    """
    pivot = less
    less += 1
    while less <= greater:
        if arr[pivot] < arr[greater]:
            greater -= 1
        elif arr[pivot] > arr[less]:
            arr[pivot], arr[less] = arr[less], arr[pivot]
            pivot = less
            less += 1
        else:
            arr[greater], arr[less] = arr[less], arr[greater]
            arr[pivot], arr[less] = arr[less], arr[pivot]
            pivot = less
            greater -= 1
            less += 1
    return pivot


def partition(arr: list, end=None, start=0):
    """Рекурсивно вызывает сортировку списока.

    Ключевые аргументы:
    arr -- сортируемый список
    end -- индекс конечного элемента.
    start -- индекс начального элемента.
    """
    if end is None:
        end = len(arr) - 1

    def _partition(arr: list, end: int, start: int):
        if start >= end:
            return
        pivot = quick_sort(arr, start, end)
        _partition(arr, end, pivot+1)
        _partition(arr, pivot-1, start)
    return _partition(arr, end, start)


if __name__ == '__main__':
    players_count = int(input())
    arr = []
    for _ in range(players_count):
        name, score, penalty = input().split()
        arr += [Player(score, penalty, name)]
    partition(arr)
    [print(arr[i].name) for i in range(players_count)]

#с классом выдал TL