# Алгоритмы

## Описание
Обучение алгоритмам и структурам данных

## Техническое описание
* Решения проверялись на https://contest.yandex.ru/
* Технология - Python

## Стек технологий
Python 3

# A_Deque.py
* Формат ввода
В первой строке записано количество команд n — целое число, не превосходящее 5000. Во второй строке записано число m — максимальный размер дека. Он не превосходит 1000. В следующих n строках записана одна из команд:
push_back(value) – добавить элемент в конец дека. Если в деке уже находится максимальное число элементов, вывести «error».
push_front(value) – добавить элемент в начало дека. Если в деке уже находится максимальное число элементов, вывести «error».
pop_front() – вывести первый элемент дека и удалить его. Если дек был пуст, то вывести «error».
pop_back() – вывести последний элемент дека и удалить его. Если дек был пуст, то вывести «error».
Value — целое число, по модулю не превосходящее 1000.
* Формат вывода
Вывод результата выполнения каждой команды на отдельной строке. Для успешных запросов push_back(x) и push_front(x) ничего не выводится.

# A_Distance_to_the_zero.py
* Формат ввода
В первой строке дана длина улицы —– n (1 ≤ n ≤ 106). В следующей строке записаны n целых неотрицательных чисел — номера домов и обозначения пустых участков на карте (нули). Гарантируется, что в последовательности есть хотя бы один ноль. Номера домов (положительные числа) уникальны и не превосходят 109.
* Формат вывода
Для каждого из участков выведите расстояние до ближайшего нуля. Числа выводите в одну строку, разделяя их пробелами.

# A_search_in_array.py
* Формат ввода
Функция принимает массив натуральных чисел и искомое число k. Длина массива не превосходит 10000. Элементы массива и число k не превосходят по значению 10000.
В примерах: В первой строке записано число n –— длина массива. Во второй строке записано положительное число k –— искомый элемент. Далее в строку через пробел записано n натуральных чисел, каждое из которых не превосходит 200000.
* Формат вывода
Функция должна вернуть индекс элемента, равного k, если такой есть в массиве (нумерация с нуля). Если элемент не найден, функция должна вернуть −1. Изменять массив нельзя. Для отсечения неэффективных решений ваша функция будет запускаться от 100000 до 1000000 раз.

# B_Find_count_numbers.py
* Формат ввода
В первой строке дано целое число k (1 ≤ k ≤ 5).
В четырёх следующих строках задан вид тренажёра –— по 4 символа в каждой строке. Каждый символ —– либо точка, либо цифра от 1 до 9. Символы одной строки идут подряд и не разделены пробелами.
* Формат вывода
Выведите единственное число –— максимальное количество баллов, которое смогут набрать Гоша и Тимофей.

# B_Polish_calculator.py
* Формат ввода
В единственной строке дано выражение, записанное в обратной польской нотации. Числа и арифметические операции записаны через пробел.
На вход могут подаваться операции: +, -, *, / и числа, по модулю не превосходящие 10000.
Гарантируется, что значение промежуточных выражений в тестовых данных по модулю не больше 50000.
* Формат вывода
Выведите единственное число — значение выражения.

# B_in_place_quick_sort.py
* Формат ввода
В первой строке задано число участников n, 1 ≤ n ≤ 100 000.
В каждой из следующих n строк задана информация про одного из участников.
i-й участник описывается тремя параметрами:
уникальным логином (строкой из маленьких латинских букв длиной не более 20)
числом решённых задач Pi
штрафом Fi
Fi и Pi — целые числа, лежащие в диапазоне от 0 до 109.
* Формат вывода
Для отсортированного списка участников выведите по порядку их логины по одному в строке.
