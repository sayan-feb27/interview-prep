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

> Создавая индексы с целью ускорения доступа к данным, нужно учитывать предполагаемую долю строк таблицы (селективность), выбираемых при выполнении типичных запросов, в которых создаваемый индекс будет использоваться.
> 
> Если эта доля велика (т. е. селективность — низкая), тогда наличие индекса может не дать ожидаемого эффекта.
> 
> Индексы более полезны, когда из таблицы выбирается лишь небольшая доля строк, т. е. при высокой селективности выборки.
</details>

<details>
<summary>Приходилось ли вам профилировать запросы?</summary>

> [Nooope](https://www.youtube.com/watch?v=mJXYMDu6dpY).

</details>

<details>
<summary>Чем отличается explain от explain analyze?</summary>

> explain in postgresql just estimates the cost of a query and explain analyze does the same and also executes a query and gives the actual results 
</details>

<details>
<summary>В каком порядке вычисляется SELECT-запрос?</summary>

>  https://docs.microsoft.com/en-us/sql/t-sql/queries/select-transact-sql?redirectedfrom=MSDN&view=sql-server-ver15#logical-processing-order-of-the-select-statement
> 
> The following steps show the logical processing order, or binding order, for a SELECT statement. 
> This order determines when the objects defined in one step are made available to the clauses in subsequent steps. 
> For example, if the query processor can bind to (access) the tables or views defined in the FROM clause, these objects and their columns are made available to all subsequent steps. 
> Conversely, because the SELECT clause is step 8, any column aliases or derived columns defined in that clause cannot be referenced by preceding clauses. However, they can be referenced by subsequent clauses such as the ORDER BY clause. 
> Note that the actual physical execution of the statement is determined by the query processor and the order may vary from this list.
> 
> 1. FROM
> 2. ON
> 3. JOIN
> 4. WHERE
> 5. GROUP BY
> 6. WITH CUBE or WITH ROLLUP
> 7. HAVING
> 8. SELECT
> 9. DISTINCT
> 10. ORDER BY
> 11. TOP

![s](https://i.stack.imgur.com/6YuwE.jpg)

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

> [Index Types](https://www.postgresql.org/docs/14/indexes-types.html)

</details>

<details>
<summary>Что такое B-Tree?</summary>

> — структура данных, дерево поиска. 
> С точки зрения внешнего логического представления - сбалансированное, сильно ветвистое дерево.
> 
> Часто используется для хранения данных во внешней памяти.
> 
> Структура B-дерева применяется для организации индексов во многих современных СУБД.

</details>
