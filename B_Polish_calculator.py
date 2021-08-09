# https://contest.yandex.ru/contest/23759/run-report/52193531/
class Stack:
    def __init__(self) -> None:
        """
        Ключевые аргументы:
        items -- стек элементов.
        """
        self.items = []

    def push(self, item: int) -> None:
        """Добавляет элемент в стек.

        Ключевой аргумент:
        item -- элемент для добавления.
        """
        self.items.append(item)

    def get_items(self) -> int:
        """Возвращает и удаляет последний элемент стека.

        Ключевой аргумент:
        items -- стек элементов.
        """
        try:
            return self.items.pop()
        except IndexError:
            raise


def get_calculation(polish_notation: list) -> int:
    """Вычисляет значение польской нотации.

        Ключевые аргументы:
        polish_notation -- обратная польская нотация.
        """
    stack = Stack()
    operations = {
        '+': lambda a, b: b + a,
        '-': lambda a, b: b - a,
        '*': lambda a, b: b * a,
        '/': lambda a, b: b // a,
    }
    for i in polish_notation:
        if i in operations:
            result = operations[i](stack.get_items(), stack.get_items())
            stack.push(int(result))
        else:
            stack.push(int(i))
    return stack.items[-1]


if __name__ == '__main__':
    polish_notation = input().split()
    try:
        result = get_calculation(polish_notation)
        print(result)
    except IndexError:
        print('Число операций превосходит количество чисел на входе.')
