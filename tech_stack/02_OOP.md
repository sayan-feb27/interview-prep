# ООП

Про ООП чаще задают общие вопросы, но вам могут попасться вопросы, связанные именно с Python. Также речь может пойти про разные паттерны:

<details>
<summary>Расскажите про основные принципы ООП.</summary>

> Наследование – это свойство системы, позволяющее описать новый класс на основе уже существующего с частично или полностью заимствующейся функциональностью. Класс, от которого производится наследование, называется базовым или родительским. Новый класс – потомком, наследником или производным классом.
                                       
> Полиморфизм – это свойство системы использовать объекты с одинаковым интерфейсом без информации о типе и внутренней структуре объекта.

> Инкапсуляция – это свойство системы, позволяющее объединить данные и методы, работающие с ними, в классе и скрыть детали 
реализации от пользователя.

</details>

<details>
<summary>Знакомы с SOLID? Посмотрите на код, нарушены ли тут какие-либо принципы SOLID? Как это можно исправить?</summary>

1) Принцип единственной обязанности.
2) Принцип открытости/закрытости.
3) Принцип подстановки Лисков.
4) Принцип разделения интерфейсов
5) Принцип инверсии зависимостей

[S.O.L.I.D Principles explained in Python with examples.](https://levelup.gitconnected.com/s-o-l-i-d-principles-explained-in-python-with-examples-83b2b43bdcde)

[S.O.L.I.D принципы с примерами на Python](https://gist.github.com/pavel-loginov-dev/8f3ef63e265c15763d169eff4627265d)

[SOLID Coding in Python](https://towardsdatascience.com/solid-coding-in-python-1281392a6a94)

</details>

<details>
<summary>Какие паттерны ООП вам знакомы?</summary>
[Refactoring Guru](https://refactoring.guru/design-patterns/catalog)
</details>

<details>
<summary>Чем отличается интерфейс от абстрактного класса?</summary>

> An abstract class can have instance methods that implement a default behavior. An Interface can only declare constants and instance methods, but cannot implement default behavior and all methods are implicitly abstract. An interface has all public members and no implementation.

https://stackoverflow.com/a/1913185

</details>

<details>
<summary>Что такое методы класса, определяемые через декоратор @classmethod? Зачем они нужны?</summary>

> Метод класса получает класс как неявный первый аргумент cls, так же, как метод экземпляра получает экземпляр. Это означает, что можно использовать свойства класса внутри этого метода без создания конкретного экземпляра класса.
> 
> Декоратор @classmethod используется, когда необходимо получить методы, не относящиеся к конкретному экземпляру класса, но все таки, как то привязанные к этому классу. 
> Эти методы можно переопределять дочерними классами. Следовательно декоратор @classmethod уместно использовать в абстрактных классах для определения того, как метод должен себя вести, когда он вызывается дочерними классами.
> 
> Так же его можно использовать когда необходимо получить доступ к свойству класса в целом, а не к свойству конкретного экземпляра этого класса.
</details>

<details>
<summary> Расскажите, зачем нужен @staticmethod?</summary>

> @staticmethod — используется для создания метода, который ничего не знает о классе или экземпляре, через который он был вызван. Он просто получает переданные аргументы, без неявного первого аргумента, 
> и его определение неизменяемо через наследование.

</details>


<details>
<summary>Как в Python объявляются приватные атрибуты (реализована инкапсуляция в Python)?</summary>

> Через нижние подчеркивания перед именем атрибута `_` или `__'.
> 
> Одно нижнее подчеркивание — это индикатор того, что переменная должна считаться приватной.
>  `__`

</details>
  

<details>
<summary>Что такое MRO в Python?</summary>

Аббревиатура MRO — method resolution order, порядок разрешения методов.
Это порядок в котором ищутся методы в иерархии классов.
Сверху вниз, слева направо.

</details>