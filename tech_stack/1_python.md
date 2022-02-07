# Python

[Python Tips](https://book.pythontips.com/en/latest/index.html)

## Общие вопросы

- Какой сложностью в О-нотации обладает операция len у list?

> O(1) — Константное время, независимое от размера элемента.

- А в О-нотации сложность получения элемента по индексу в list?

> O(n).

- Какая структура заложена в реализации словарей? Как реализована борьба с коллизиями ключей?

> Хеш-таблицы.
> 
> Это структура данных, реализующая интерфейс ассоциативного массива, а именно, она позволяет хранить пары (ключ, значение) и выполнять три операции: операцию добавления новой пары, операцию поиска и операцию удаления пары по ключу.
> 
> Существуют два основных варианта хеш-таблиц: с цепочками и открытой адресацией. Хеш-таблица содержит некоторый массив 
H, элементы которого есть пары (хеш-таблица с открытой адресацией) или списки пар (хеш-таблица с цепочками).
> 
> В Python `dict` использует открытую адресацию.
> 
> Ситуация, когда для различных ключей получается одно и то же хеш-значение, называется коллизией.

- Как работает Garbage Collector в Python?

> В Python существует сборщик мусора, который автоматически освобождает место в памяти, во время работы программы
> в случае, если количество ссылок на объект становится нулю. 
> 
> Reference counting.

- С помощью какой структуры данных реализован set?
> Хеш-таблиц.

- Что такое декораторы и как они работают?

> Функция, которая принимает другую функцию в качестве аргумента и возвращает другую функцию.
> 
```python
def power_result_by_two(fn):
    def inner(*args):
        return fn(*args) ** 2
    return inner


def power_result_by(arg):
    def power_by(fn):
        def inner(*args):
            return fn(*args) ** power
        return inner

    if callable(arg):
        power = 2
        return power_by(arg)
    power = arg
    return power_by


# @power_result_by_two
# @power_result_by(5)
@power_result_by
def add_together(a: int, b: int) -> int:
    return a + b


print(add_together(5, 4))

```

- Что такое генераторы и как они работают?

> Генераторы — это итератор, пройтись по которому можно только раз. Он не хранит все значения в памяти, а, собственно, генерирует их.
> 
> `Iterable` — объект у которого определен метод `__iter__` (или `__getitem__`), возвращающий `Iterator`.
> 
> `Iterator` — объект у которого реализован метод `__next__`.

Пример итератора:
```python
class MyIter:

    def __init__(self, n):
        self.n = n
        self.num = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.n > self.num:
            cur, self.num = self.num, self.num + 1
            return cur

        raise StopIteration
```

Пример генератора:
```python
def fib_n(n):
    a = b = 1
    for i in range(n):
        yield a
        a, b = b, a + b


for x in fib_n(1000):
    print(x)

```


- Что такое менеджеры контекста и как они работают?

https://book.pythontips.com/en/latest/context_managers.html
https://habr.com/ru/post/196382/

> Контекстные менеджеры это специальные конструкции, которые представляют из себя блоки кода, заключенные в инструкцию `with`.
> 
> Контекстный менеджер используется для выполнения каких либо действий до входа в блок и после выхода из него.

Возьмем к примеру работу с файлами:
```python
file = open('some_file', 'w')
try:
    file.write('Hola!')
finally:
    file.close()

# что равно

with open('some_file', 'w') as opened_file:
    opened_file.write('Hola!')

```

Контекстный менеджер можно реализовать самому, определив методы `__enter__` и `__exit__`.

```python
class File(object):
    def __init__(self, file_name, method):
        self.file_obj = open(file_name, method)
    def __enter__(self):
        return self.file_obj
    def __exit__(self, type, value, traceback):
        self.file_obj.close()

with File('demo.txt', 'w') as opened_file:
    opened_file.write('Hola!')

# Output: Exception has been handled
```

Или через генераторы и декораторы
```python
from contextlib import contextmanager

@contextmanager
def open_file(name):
    f = open(name, 'w')
    try:
        yield f
    finally:
        f.close()

with open_file('some_file') as f:
    f.write('hola!')

```

## Асинхронность и параллельность в Python

- Что такое корутины и как они работают?
