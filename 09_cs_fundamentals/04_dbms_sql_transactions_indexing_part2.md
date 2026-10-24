---
domain: cs
topic: dbms_sql_transactions_indexing
title: DBMS: SQL, transactions, indexing
tags: [dbms, sql, acid, indexing, normalization]
count: 103
part: 2/2
---
# DBMS: SQL, transactions, indexing (part 2)

## Transactions, ACID and logging
- [CS04-107] What is a transaction, and why are transactions important?
- [CS04-108] What are the ACID properties? Explain each with an example, such as a bank transfer.
- [CS04-109] You transfer money between two accounts in one transaction. What happens if the server crashes between the debit and the credit?
- [CS04-110] Which mechanisms in a database implement atomicity, consistency, isolation and durability?
- [CS04-111] How do databases implement atomicity and durability using undo logs, redo logs and recovery?
- [CS04-112] What is write-ahead logging, and how do checkpoints and group commit interact with it?
- [CS04-113] Can you have consistency without atomicity? What is the difference between logical and physical consistency?
- [CS04-114] What do COMMIT and ROLLBACK do, and what are savepoints used for?
- [CS04-115] What are the life-cycle states of a transaction, and can a committed transaction move to any other state?
- [CS04-116] What does AUTOCOMMIT do, and what risks arise when a connection leaves a transaction open?
- [CS04-117] Why is transaction scope a trade-off between consistency and concurrency?
- [CS04-118] What are the risks of long-running and very large transactions?
- [CS04-119] What are the roles of the redo log, undo log and binlog in MySQL, and how do redo log and binlog differ?
- [CS04-120] Why does MySQL use a two-phase commit between the redo log and the binlog, and what could go wrong without it?
- [CS04-121] What are the redo log flush policies (innodb_flush_log_at_trx_commit), and what is the durability versus performance trade-off?
- [CS04-122] How does the undo log support both rollback and MVCC, and what happens when long transactions keep old versions alive?
- [CS04-123] Describe how a database recovers after a crash using analysis, redo and undo phases (ARIES-style recovery).

## Isolation, locking, MVCC and deadlocks
- [CS04-124] If a database had no locking or concurrency control at all, what problems could occur?
- [CS04-125] Define dirty read, non-repeatable read, phantom read and lost update.
- [CS04-126] What is the difference between a non-repeatable read and a phantom read, and between a dirty read and a non-repeatable read?
- [CS04-127] What are the four standard isolation levels, and which anomalies does each allow or prevent?
- [CS04-128] How are isolation levels implemented in practice with locks or MVCC, and how does isolation prevent dirty reads?
- [CS04-129] What is the default isolation level in common relational databases such as MySQL InnoDB, and why was it chosen?
- [CS04-130] What are the performance trade-offs of SERIALIZABLE versus READ COMMITTED, and when would you choose a lower level?
- [CS04-131] Two concurrent transactions each check an account balance and then withdraw. How can this go wrong, and how do you prevent lost updates?
- [CS04-132] What is write skew, and why can MVCC snapshot isolation still allow it?
- [CS04-133] How does MVCC work, and how do version numbers, undo logs and read views let readers avoid blocking writers?
- [CS04-134] How does MVCC behave differently under READ COMMITTED and REPEATABLE READ?
- [CS04-135] What is the difference between a snapshot read and a current read?
- [CS04-136] Does MVCC fully prevent phantom reads in InnoDB? How do record, gap and next-key locks complement it?
- [CS04-137] Why can gap locking cause unexpected lock waits or deadlocks on concurrent inserts?
- [CS04-138] What are shared and exclusive locks, and why are intention locks needed?
- [CS04-139] Compare row-level, page-level and table-level locks, and explain lock escalation.
- [CS04-140] Why can an UPDATE that filters on a non-indexed column lock the whole table in InnoDB?
- [CS04-141] What is two-phase locking, how does it guarantee serializability, and why can it still deadlock?
- [CS04-142] What is serializability, and how do you test a schedule for it?
- [CS04-143] What is the difference between optimistic and pessimistic locking, and when is each appropriate?
- [CS04-144] How does SELECT ... FOR UPDATE differ from a plain SELECT inside a transaction?
- [CS04-145] How would you handle a hot-row update, such as decrementing inventory for a flash sale, without heavy lock contention?
- [CS04-146] What is a deadlock in a database, and why do deadlocks happen? Give an interleaving of two transactions that deadlock.
- [CS04-147] How does a database detect deadlocks and choose a victim, and how can you reduce their frequency in application design?
- [CS04-148] What are the Wait-Die and Wound-Wait schemes, and what is the trade-off between deadlock prevention and detection?

## Indexes and B+ trees
- [CS04-149] How does a database index work, and why does it speed up reads?
- [CS04-150] What are the disadvantages of indexes, and why do too many indexes hurt write-heavy workloads?
- [CS04-151] What is the difference between a clustered and a non-clustered index?
- [CS04-152] Why can a table have only one clustered index? What happens when you insert into a table with a clustered index?
- [CS04-153] What are fill factor and page splits, and when does a page split occur?
- [CS04-154] When would you choose a non-clustered (secondary) index, and why can a secondary-index lookup need a second lookup into the clustered index?
- [CS04-155] Why do databases use B+ trees for indexes rather than binary trees, red-black trees or hash tables?
- [CS04-156] What is the difference between a B-tree and a B+ tree, and why is the B+ tree better for range queries?
- [CS04-157] When is a hash index preferable to a B+ tree index, and what queries can it not support?
- [CS04-158] A table has 100 million rows and a B+ tree index with fan-out of about 500. Roughly how many page reads does a point lookup need?
- [CS04-159] What is a composite index, and why does column order matter? Can a composite index be unique?
- [CS04-160] What is the leftmost-prefix rule? If a three-column composite index is used with a WHERE on only two columns, will it be used?
- [CS04-161] When should you use one composite index versus several single-column indexes?
- [CS04-162] What is a covering index, and why does it avoid table lookups? Is SELECT * always bad for index usage?
- [CS04-163] What is index selectivity (cardinality), and how do you decide which columns to index?
- [CS04-164] Which index types exist (unique, partial, prefix, full-text, spatial) and what is each good for?
- [CS04-165] Why doesn't every query use an index? Name common causes such as functions on columns, implicit casts and OR conditions.
- [CS04-166] Why can LIKE '%abc' not use a B+ tree index, and what alternatives exist for substring search?
- [CS04-167] How do the optimizer and index merge handle OR conditions, and why can IN or NOT IN lead to full scans?
- [CS04-168] What is index condition pushdown, and when does it reduce table lookups?
- [CS04-169] How can ORDER BY with LIMIT end up using filesort or a poor index, and how would you fix it?
- [CS04-170] Compare auto-increment, UUID and snowflake IDs as primary keys. Why do random UUIDs hurt in a clustered-index engine?
- [CS04-171] What is a function-based (expression) index, and when would you use one?
- [CS04-172] What is a bitmap index, and why is it used in analytical rather than transactional systems?

## Query execution and optimization
- [CS04-173] What happens when an application sends a query to the database? Describe parsing, optimization and execution.
- [CS04-174] What is an EXPLAIN plan, what does it contain, and how do you read it (type, key, rows, Extra)?
- [CS04-175] What is the difference between EXPLAIN and EXPLAIN ANALYZE?
- [CS04-176] What do the access types ALL, index, range, ref, eq_ref and const tell you about performance?
- [CS04-177] What do Using filesort and Using temporary mean in an execution plan, and how do you eliminate them?
- [CS04-178] What is the difference between a table scan and an index seek, and when is a full scan actually faster?
- [CS04-179] How would you optimize a slow SQL query?
- [CS04-180] A query that was fast last week now takes seconds. How would you investigate using slow query logs, execution plans and statistics?
- [CS04-181] How do table statistics influence the optimizer, why can stale statistics cause a bad plan, and when do you refresh them?
- [CS04-182] What are query hints, and when is it appropriate to use them?
- [CS04-183] How do nested loop, hash and sort-merge joins work, and when does the optimizer choose each?
- [CS04-184] Why does a join on columns with different data types or character sets perform poorly?
- [CS04-185] Why can splitting a large join into several simple queries sometimes be faster?
- [CS04-186] How would you optimize deep pagination such as LIMIT 1000000, 20?
- [CS04-187] What is the difference between keyset (seek) and offset pagination?
- [CS04-188] Why can COUNT(*) be slow on large InnoDB tables, and how do you speed up counting?
- [CS04-189] What is a database buffer pool (buffer cache), and how do its size and hit ratio affect performance?
- [CS04-190] Why was the MySQL query cache removed in 8.0, and why was it ineffective under write-heavy workloads?
- [CS04-191] Compare InnoDB and MyISAM in terms of transactions, locking granularity, crash recovery, foreign keys and index layout.
- [CS04-192] How would you add a column or an index to a billion-row production table without downtime?
- [CS04-193] What is the difference between a cost-based and a rule-based optimizer, and how does a cost-based optimizer pick a plan?
- [CS04-194] A parameterized query is fast for some parameter values and slow for others. What could explain it (plan caching, skewed data) and how would you fix it?

## Views, stored procedures, triggers and cursors
- [CS04-195] What is a view (a virtual table), and why do we use views? What are their limitations, such as updatability?
- [CS04-196] What is the difference between a view and a materialized view, and when does a materialized view make sense?
- [CS04-197] What are the performance implications of using views?
- [CS04-198] How can views be used for security, such as hiding columns or restricting rows for a role?
- [CS04-199] What is a stored procedure, and what are its advantages and drawbacks compared with application-side SQL?
- [CS04-200] What is the difference between a stored procedure and a user-defined function?
- [CS04-201] What are user-defined functions, and what types exist (scalar, table-valued)?
- [CS04-202] What is a trigger, and why do we need triggers?
- [CS04-203] What types of triggers exist (BEFORE, AFTER, INSTEAD OF, row-level, statement-level), and when do you use each?
- [CS04-204] What risks do triggers bring to maintainability and performance?
- [CS04-205] What is a database cursor, and why can row-by-row cursor processing be slow?
- [CS04-206] When would you avoid views, triggers and cursors, and what do you use instead?
- [CS04-207] How would you implement an audit trail of changes to a table: trigger, application code or change data capture?
- [CS04-208] What is a prepared statement, and why does it help with performance and SQL injection?
- [CS04-209] What is the N+1 query problem, and how do you solve it?
