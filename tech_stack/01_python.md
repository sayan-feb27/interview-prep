# Python

[Python Tips](https://book.pythontips.com/en/latest/index.html)

[What Is the Python Global Interpreter Lock (GIL)?](https://realpython.com/python-gil/)

[Memory Management in Python](https://realpython.com/python-memory-management/)

[Concurrency, Parallelism, Threads, Processes, Async, and Sync — Related?](https://medium.com/swift-india/concurrency-parallelism-threads-processes-async-and-sync-related-39fd951bc61d)

[В Python — нет переменных. И как теперь жить? Python Memory Management на пальцах](https://www.youtube.com/watch?v=8GpI0PAGniA)

## Общие вопросы

<details>
<summary>Какой сложностью в О-нотации обладает операция len у list?</summary>

> O(1) — Константное время, независимое от размера элемента.

</details>

<details>
<summary>А в О-нотации сложность получения элемента по индексу в list?</summary>

> O(n).

</details>

<details>
<summary>Какая структура заложена в реализации словарей? Как реализована борьба с коллизиями ключей?</summary>

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
</details>

<details>
<summary>Как работает Garbage Collector в Python?</summary>

> В Python существует сборщик мусора, который автоматически освобождает место в памяти, во время работы программы
> в случае, если количество ссылок на объект становится нулю. 
> 
> Reference counting.
</details>

<details>
<summary>С помощью какой структуры данных реализован set?</summary>
> Хеш-таблиц.
</details>

<details>
<summary>Что такое декораторы и как они работают?</summary>

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
</details>

<details>
<summary>Что такое генераторы и как они работают?</summary>

> Генераторы — это итератор, пройтись по которому можно только раз. Он не хранит все значения в памяти, а, собственно, генерирует их по одному.
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
</details>

<details>
<summary>Что такое менеджеры контекста и как они работают?</summary>

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
</details>

## Асинхронность и параллельность в Python

<details>

<summary>Что такое GIL? Для чего он нужен?</summary>

We'll understand why only I/O bound Python programs can leverage multithreading to speed up execution time. 
But first, a quick refresher of how Python works is necessary to understand the acronym GIL or global interpreter lock.

### How Python works

Python is an interpreted language, that is, there is no static time compiling as that happens in the case of Java, C or C++. 
The program that interprets user code is called the Interpreter. An interpreter is a program that executes other programs. 
At a higher level when we run a Python program (.py file), the Python interpreter compiles the source code into byte code. 
The generated byte code is a lower-level platform-independent representation that can be understood by the Python Virtual Machine (PVM). 
In the next step, the byte code is routed to the PVM for execution. Note that PVM isn't a separate component. 
Rather, it is just a loop in the Python interpreter that is responsible for executing byte code line by line. The PVM is really a part of the interpreter.

### Python Interpreter

The Python interpreter as explained is responsible for executing a program, __but it can only execute a single thread at a time__. 
This is the falling of the reference implementation of Python - CPython, called so because it is written in the C language. 
So if your machine has one, ten, or a hundred processors, the Python interpreter is only able to run a single thread at a time using a single processor. 
Two threads on a machine with two available processors can't be executed in parallel each running on a single CPU.

This design has direct consequences on the performance of CPU bound programs since they don't experience any speed-up in the presence of additional processors. 
In fact, they may run slower because of the additional housekeeping overhead required for running multiple threads.

### Why is that so?

One may wonder what was the design decision behind restricting the interpreter to run a single thread. 
__The answer lies in how memory management works in Python - reference counter__.

```python
import sys

# declare a variable
some_var = "Educative"

# check reference count
print (sys.getrefcount(some_var))

# create another refrence to someVar
another_var = some_var

# verify the incremented reference count
print (sys.getrefcount(some_var))
```

If you run the above snippet, you'll see the reference count of the variable some_var increase. When references to an object are removed, the reference count for an object is decremented. When the reference count becomes zero, the object is deallocated. The interpreter executes a single thread in order to ensure that the reference count for objects is safe from race conditions.

A reference count is associated with each object in a program. One possible solution could have been to associate one lock per object so that multiple threads could work on the object in a thread-safe manner. However, this approach would have resulted in too many locks being managed with the possibility of deadlocks. Thus, a compromise was made to have a single lock that provides exclusive access to the Python interpreter. This lock is known as the Global Interpreter Lock.

Execution of Python bytecode requires acquiring the GIL. This approach prevents deadlocks as there's a single global lock to manage and introduces little overhead. However, the cost is paid by making CPU-bound tasks essentially single-threaded.

</details>


<details>

<summary>Чем отличается поток от процесса?</summary>

> Process is an instance of a program.
> 
> A thread is the smallest unit of execution in a process which simply executes instructions serially. 
> A process can have multiple threads running as part of it. 
> Usually, there would be some state associated with the process that is shared among all the threads and in turn each thread would have some state private to itself.
> The globally shared state amongst the threads of a process is visible and accessible to all the threads, and special attention needs to be paid when any thread tries to read or write to this global shared state
> 
> Processes don't share any resources amongst themselves whereas threads of a process can share the resources allocated to that particular process, including memory address space.

</details>
   
<details>

<summary>Расскажите про состояние гонки и потокобезопасность.</summary>

> The primary motivation behind using multiple threads is improving program performance that may be measured with metrics such as throughput, responsiveness, latency, etc. Whenever threads are introduced in a program, the shared state amongst the threads becomes vulnerable to corruption. If a class or a program has immutable state then the class is necessarily thread-safe.
> 
> Race conditions happen when threads run through critical sections without thread synchronization. The threads "race" through the critical section to write or read shared resources and depending on the order in which threads finish the "race", the program output changes. In a race condition, threads access shared resources or program variables that might be worked on by other threads at the same time causing the application data to be inconsistent.
> 
> Deadlocks occur when two or more threads aren't able to make any progress because the resource required by the first thread is held by the second and the resource required by the second thread is held by the first.
> 
> Other than a deadlock, an application thread can also experience starvation when it never gets CPU time or access to shared resources. Other greedy threads continuously hog shared system resources not letting the starving thread make any progress.


</details>
   
<details>

<summary>Какие механизмы синхронизации доступа к общим ресурсам вы знаете?</summary>

> Mutex (monitor), Semaphore.

</details>
   
<details>

<summary>Какие механизмы взаимодействия процессов вы знаете?</summary>

> [Межпроцессное взаимодействие](https://ru.wikipedia.org/wiki/Межпроцессное_взаимодействие)

</details>
   
<details>

<summary>Что такое асинхронный ввод-вывод?</summary>

> асинхронный ввод/вывод является формой неблокирующей обработки ввода/вывода, который позволяет процессу продолжить выполнение не дожидаясь окончания передачи данных. 
> Входные и выходные операции на компьютере могут быть весьма медленными, по сравнению с обработкой данных.

</details>
   
<details>

<summary>Что такое корутины? Как они работают?</summary>

>

</details>
   
<details>

<summary>Для чего используется конструкция async/await в Python?</summary>

>

</details>
   
<details>

<summary>Как устроен EventLoop?</summary>

>

</details>
