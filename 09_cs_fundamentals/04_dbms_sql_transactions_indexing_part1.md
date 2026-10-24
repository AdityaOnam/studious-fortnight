---
domain: cs
topic: dbms_sql_transactions_indexing
title: DBMS: SQL, transactions, indexing
tags: [dbms, sql, acid, indexing, normalization]
count: 106
part: 1/2
---
# DBMS: SQL, transactions, indexing (part 1)

## Relational model, keys and constraints
- [CS04-001] What is a DBMS, and what advantages does it have over storing data in plain files?
- [CS04-002] What is the difference between a database, a DBMS, a database system and a DBA?
- [CS04-003] What makes a database relational? Define table, row (tuple), column (attribute) and schema.
- [CS04-004] What is the difference between OLTP and OLAP systems?
- [CS04-005] What are the main differences between SQL and NoSQL databases, and how would you choose between them?
- [CS04-006] Explain the three-level architecture of a DBMS and what logical and physical data independence mean.
- [CS04-007] What are the core relational algebra operations (selection, projection, join, union, difference) and how do they map to SQL?
- [CS04-008] What are primary and foreign keys, and why are keys important in a relational database?
- [CS04-009] What is the difference between a primary key, a unique key and a foreign key?
- [CS04-010] Define super key, candidate key, primary key and alternate key, and say what prime and non-prime attributes are.
- [CS04-011] What is a composite key, and when would you use one?
- [CS04-012] Why can't a primary key contain NULL values?
- [CS04-013] Why isn't a foreign key necessarily unique, and can a table have more than one foreign key?
- [CS04-014] What happens when you delete a row that is referenced by a foreign key, and what do CASCADE, SET NULL and RESTRICT do?
- [CS04-015] Why do many large-scale systems avoid foreign key constraints and cascading deletes in the database?
- [CS04-016] Compare natural keys and surrogate keys as primary keys.
- [CS04-017] Which kinds of constraints does SQL support (NOT NULL, UNIQUE, CHECK, DEFAULT, PRIMARY KEY, FOREIGN KEY)?
- [CS04-018] Why enforce integrity constraints in the database rather than only in application code?
- [CS04-019] What is the difference between CHAR and VARCHAR, and why is declaring every column VARCHAR(255) not free of cost?
- [CS04-020] Why should money be stored as DECIMAL or integer minor units rather than FLOAT or DOUBLE?
- [CS04-021] How do DATETIME, TIMESTAMP and integer epoch columns differ, and why should dates not be stored as strings?
- [CS04-022] Why is storing large TEXT or BLOB values, such as images, in ordinary tables discouraged?
- [CS04-023] Why can an auto-increment primary key have gaps after rollbacks, failed inserts or restarts?

## ER modeling, schema design and normalization
- [CS04-024] What is data modeling, and how do conceptual, logical and physical data models differ?
- [CS04-025] What is an ER diagram, and how do you map entities and relationships to tables?
- [CS04-026] What kinds of relationships exist between entities (one-to-one, one-to-many, many-to-many)?
- [CS04-027] What is the difference between a strong entity and a weak entity?
- [CS04-028] What types of attributes exist in an ER diagram (simple, composite, multivalued, derived)?
- [CS04-029] How do you resolve a many-to-many relationship, and represent a ternary relationship, in a relational schema?
- [CS04-030] What is the difference between total and partial participation?
- [CS04-031] How do you represent inheritance (specialization and generalization) from an ER diagram in tables?
- [CS04-032] How would you model students enrolling in courses across semesters, with a grade per enrollment? Which tables and keys do you need?
- [CS04-033] What steps and considerations guide you when designing the schema for a new application?
- [CS04-034] What is normalization, why is it needed, and what problems does it prevent?
- [CS04-035] What are insertion, update and deletion anomalies? Give a small example of each.
- [CS04-036] What is a functional dependency, and how do dependencies lead to anomalies?
- [CS04-037] What is a transitive dependency? Explain with an example.
- [CS04-038] A table stores a comma-separated list of tags in one column. Which normal form does it violate and how do you fix it?
- [CS04-039] Explain 1NF, 2NF, 3NF and BCNF with an example violation of each.
- [CS04-040] What is the difference between 3NF and BCNF, and why do we need BCNF?
- [CS04-041] Can a relation be in 2NF but not in 1NF?
- [CS04-042] Given R(A,B,C,D) with A->B, B->C and C->D, find the candidate keys and the highest normal form of R.
- [CS04-043] Is more normalization always better?
- [CS04-044] When would you deliberately denormalize a schema, and what do you give up?
- [CS04-045] Besides duplicating columns, what other ways (summary tables, materialized views, caching) speed up reads without denormalizing the source of truth?
- [CS04-046] What are lossless-join decomposition and dependency preservation, and why do they matter when decomposing a relation?
- [CS04-047] What is a multivalued dependency, and what does 4NF fix that BCNF does not?
- [CS04-048] Compare an adjacency list, nested sets and a closure table for storing hierarchical data such as categories or org charts.

## SQL fundamentals and clauses
- [CS04-049] What is SQL, and what are the DDL, DML, DCL and TCL command categories?
- [CS04-050] What is the difference between SQL and PL/SQL?
- [CS04-051] What is the difference between DELETE, TRUNCATE and DROP regarding rollback, speed, triggers and storage?
- [CS04-052] Which statements (DML or DDL) can be rolled back, and why does it vary by database?
- [CS04-053] Why must you be careful to include a filter in UPDATE and DELETE statements, and how can you guard against mistakes in production?
- [CS04-054] How do you retrieve distinct values from a column?
- [CS04-055] What is the difference between WHERE and HAVING?
- [CS04-056] What does GROUP BY do, can you group by several columns, and how does it differ from ORDER BY?
- [CS04-057] What happens if you use aggregate functions in a SELECT with non-aggregated columns but no GROUP BY?
- [CS04-058] Can ORDER BY use a column that is not in the SELECT list, and what is ORDER BY with a column position?
- [CS04-059] What is the logical processing order of a SELECT statement (FROM, WHERE, GROUP BY, HAVING, SELECT, ORDER BY, LIMIT)?
- [CS04-060] Which aggregate functions does SQL provide, and why can't they be used in a WHERE clause?
- [CS04-061] What is the difference between COUNT(*), COUNT(column) and COUNT(DISTINCT column), and how do aggregates treat NULLs?
- [CS04-062] How do you test for NULL, and what does `col <> 5` return for rows where col is NULL?
- [CS04-063] How does NULL behave in comparisons, joins, GROUP BY and ORDER BY? What is three-valued logic?
- [CS04-064] What is the difference between NULL and an empty string, and how do NULLs affect indexes and performance?
- [CS04-065] What is the difference between the BETWEEN and IN operators?
- [CS04-066] How does pattern matching with LIKE work, and how would you find names starting with 'M' regardless of case?
- [CS04-067] What is the SQL CASE expression used for? Give an example.

## Joins, set operations and subqueries
- [CS04-068] What are the different types of SQL joins (inner, left, right, full outer, cross), and how do they differ?
- [CS04-069] Write a query that joins two tables and returns only rows with matching keys.
- [CS04-070] What is the difference between INNER JOIN, LEFT JOIN and FULL JOIN, and which is the default join?
- [CS04-071] How do you join more than two tables? Show a query that joins three.
- [CS04-072] What is a self join, and when would you use one?
- [CS04-073] What are cross joins and natural joins, and what happens if you omit the join condition?
- [CS04-074] Why would you ever use a RIGHT JOIN when a LEFT JOIN can satisfy the requirement?
- [CS04-075] In which scenarios would you use INNER JOIN, LEFT JOIN, RIGHT JOIN, UNION and subqueries respectively?
- [CS04-076] You LEFT JOIN two tables but filter on a right-table column in the WHERE clause. Why does it behave like an inner join, and how do you fix it?
- [CS04-077] What is the difference between UNION and UNION ALL, and how do you merge result sets without duplicates?
- [CS04-078] How do INTERSECT and MINUS/EXCEPT work, and how would you fetch the common records of two tables?
- [CS04-079] What is a subquery, what types exist, and when would you use one (including in UPDATE and DELETE)?
- [CS04-080] What is the difference between correlated and non-correlated subqueries? When can one be rewritten as a join?
- [CS04-081] When would you use EXISTS versus IN versus a JOIN for filtering?
- [CS04-082] What are the performance implications of subqueries versus joins? Why might a join on a subquery be slow?
- [CS04-083] What is the difference between a temporary table and a common table expression (CTE)?
- [CS04-084] A join between orders and order_items inflates SUM(order_total). Why does it happen and how do you avoid it?

## Window functions and SQL query problems
- [CS04-085] How do window functions differ from GROUP BY, and what do PARTITION BY and ORDER BY inside OVER() do?
- [CS04-086] Compare ROW_NUMBER, RANK and DENSE_RANK with a tie example. Why does RANK skip numbers?
- [CS04-087] How do aggregate window functions with frame clauses compute running totals or moving averages?
- [CS04-088] How do LAG and LEAD work, and how would you compute month-over-month change?
- [CS04-089] Write a query that returns each department's name and its employee count.
- [CS04-090] Write a query to find the Nth highest salary. How do you handle ties?
- [CS04-091] How would you find the Nth highest salary, or the top earners including ties, within each department?
- [CS04-092] Given a table of user transactions, write a query that returns the third transaction of every user.
- [CS04-093] Write a query to find employees who earn more than their managers.
- [CS04-094] Write a query to find duplicate rows or duplicate emails in a table.
- [CS04-095] Write a query to delete duplicate rows while keeping the row with the lowest id.
- [CS04-096] How can you delete duplicate records in a table that has no primary key?
- [CS04-097] How would you find customers who have never placed an order? Compare NOT IN, NOT EXISTS and LEFT JOIN with IS NULL.
- [CS04-098] Write a query that finds numbers appearing at least three times consecutively in a log table.
- [CS04-099] Given an IMPRESSIONS table with ad_id, click and date, write a query for the click-through rate of each ad by month.
- [CS04-100] How do you pivot rows into columns in SQL using CASE expressions and conditional aggregation?
- [CS04-101] How would you query a tree or hierarchy stored in a table, for example with a recursive CTE?
- [CS04-102] How do you fetch alternate rows from a table?
- [CS04-103] Write a query that counts employees by gender whose date of birth falls between two given dates.
- [CS04-104] How would you find users with activity on consecutive days, or build sessions from an events table (gaps and islands)?
- [CS04-105] A reviewer proposes adding SELECT DISTINCT to make a duplicate-row test pass after a join. What is your response?
- [CS04-106] How would you prevent join fan-out (row duplication) bugs from reaching dashboards?
