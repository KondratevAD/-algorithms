# https://contest.yandex.ru/contest/23759/run-report/52205481/
from typing import Optional


class MyDeque:
    def __init__(self, deque_size: int) -> None:
        """Принимает аргументы.

        Ключевые аргументы:
        deque -- дек.
        max_size -- максимальный размер дека.
        front -- начало дека.
        back -- конец дека.
        size -- размер дека
        """
        self.__deque = [None] * deque_size
        self.__max_size = deque_size
        self.__front = 0
        self.__back = 0
        self.__size = 0

    def is_empty(self) -> bool:
        """Проверяет пустой ли дек.

        Ключевые аргументы:
        size -- размер дека.
        """
        return self.__size == 0

    def is_full(self) -> bool:
        """Проверяет полный ли дек.

        Ключевые аргументы:
        max_size -- максимальный размер дека.
        size -- размер дека.
        """
        return self.__size == self.__max_size

    def push_back(self, value: int) -> None:
        """Добавляет элемент в конец дека.

        Ключевые аргументы:
        value -- значение элемента для добавления.
        deque -- дек.
        max_size -- максимальный размер дека.
        back -- конец дека.
        size -- размер дека.
        """
        if self.is_full():
            raise
        self.__back = (self.__back - 1) % self.__max_size
        self.__deque[self.__back] = value
        self.__size += 1

    def pop_back(self) -> int:
        """Удаляет элемент в конеце дека.

        Ключевые аргументы:
        deque -- дек.
        max_size -- максимальный размер дека.
        back -- конец дека.
        size -- размер дека.
        """
        if self.is_empty():
            raise
        value = self.__deque[self.__back]
        self.__back = (self.__back + 1) % self.__max_size
        self.__size -= 1
        return value

    def push_front(self, value: int) -> None:
        """Добавляет элемент в начало дека.

        Ключевые аргументы:
        value -- значение элемента для добавления.
        deque -- дек.
        max_size -- максимальный размер дека.
        front -- начало дека.
        size -- размер дека.
        """
        if self.is_full():
            raise
        self.__deque[self.__front] = value
        self.__front = (self.__front + 1) % self.__max_size
        self.__size += 1

    def pop_front(self) -> int:
        """Удаляет элемент в начале дека.

        Ключевые аргументы:
        deque -- дек.
        max_size -- максимальный размер дека.
        front -- начало дека.
        size -- размер дека.
        """
        if self.is_empty():
            raise
        self.__front = (self.__front - 1) % self.__max_size
        self.__size -= 1
        return self.__deque[self.__front]


def changes_deque(deque, command: list) -> Optional[int]:
    """Изменяет дек в соответствии с командой.

    Ключевые аргументы:
    deque -- объект класса дека.
    command -- команда на изменение дека.
    """
    commanda, *atribut = command
    return getattr(deque, commanda)(*atribut)


if __name__ == '__main__':
    command_count = int(input())
    deque_size = int(input())
    deque = MyDeque(deque_size)
    for _ in range(command_count):
        command = input().split()
        try:
            result = changes_deque(deque, command)
            if result:
                print(result)
        except Exception:
            print('error')
