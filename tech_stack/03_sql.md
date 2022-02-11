# SQL

Вопросы, направленные на знания SQL баз данных и SQL-диалекта. Вопросы могут быть адаптированы, например, к PostgreSQL или MySQL:

[Postgresql Documentation](https://www.postgresql.org/docs/14/index.html): главы 1, 2 и 6, чтобы просто вспомнить.

<details>
<summary>Что такое транзакция? Перечислите ее свойства.</summary>

>  Группа последовательных операций с базой данных, которая может быть выполнена либо целиком и успешно, соблюдая целостность данных и независимо от параллельно идущих других транзакций, либо не выполнена вообще, и тогда она не должна произвести никакого эффекта.
> 
> Требования к транзакционной системе:
> 
> Акроним ACID:
> 
> Atomicity - Атомарность: Атомарность гарантирует, что никакая транзакция не будет зафиксирована в системе частично. Будут либо выполнены все её подоперации, либо не выполнено ни одной
> 
> Consistency — Согласованность: Транзакция, достигающая своего нормального завершения (EOT — end of transaction, завершение транзакции) и тем самым фиксирующая свои результаты, сохраняет согласованность базы данных. Другими словами, каждая успешная транзакция по определению фиксирует только допустимые результаты. Это условие является необходимым для поддержки четвёртого свойства.
> 
> Isolation — Изолированность: Во время выполнения транзакции параллельные транзакции не должны оказывать влияния на её результат.
> 
> Durability — Прочность: Независимо от проблем на нижних уровнях (к примеру, обесточивание системы или сбои в оборудовании) изменения, сделанные успешно завершённой транзакцией, должны остаться сохранёнными после возвращения системы в работу.

</details>

<details>
<summary>Какие типы отношений между таблицами вы знаете?</summary>

> OneToOne, OneToMany, ManyToMany.

</details>

<details>
<summary>Какие типы JOIN вы знаете? Чем они отличаются?</summary>

> SELF, INNER, LEFT OUTER, RIGHT OUTER, FULL JOIN


![joins](https://www.postgresqltutorial.com/wp-content/uploads/2018/12/PostgreSQL-Joins.png)

</details>

<details>
<summary>Что такое селективность?</summary>
>
</details>

<details>
<summary>Приходилось ли вам профилировать запросы?</summary>
>
</details>

<details>
<summary>Чем отличается explain от explain analyze?</summary>
>
</details>

<details>
<summary>В каком порядке вычисляется SELECT-запрос?</summary>
>
</details>

<details>
<summary>Чем отличается `having` от `where`?</summary>

> The fundamental difference between WHERE and HAVING is this: WHERE selects input rows before groups and aggregates are computed (thus, it controls which rows go into the aggregate computation), whereas HAVING selects group rows after groups and aggregates are computed. Thus, the WHERE clause must not contain aggregate functions; it makes no sense to try to use an aggregate to determine which rows will be inputs to the aggregates. On the other hand, the HAVING clause always contains aggregate functions. (Strictly speaking, you are allowed to write a HAVING clause that doesn't use aggregates, but it's seldom useful. The same condition could be used more efficiently at the WHERE stage.)

</details>

  
<details>
<summary>Знаете что такое индекс?</summary>

> Индекс — специальная структура данных, создаваемая с целью повышения производительности поиска данных.

</details>

<details>
<summary>Какие индексы вы знаете?</summary>
>
</details>

<details>
<summary>Что такое B-Tree?</summary>
>
</details>
