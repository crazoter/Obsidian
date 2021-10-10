#snippets 

https://explainextended.com/2009/09/15/not-in-vs-not-exists-vs-left-join-is-null-sql-server/

## [NOT IN vs. NOT EXISTS vs. LEFT JOIN / IS NULL: SQL Server](https://explainextended.com/2009/09/15/not-in-vs-not-exists-vs-left-join-is-null-sql-server/)

![[Pasted image 20211006160835.png]]

Which method (NOT IN vs. NOT EXISTS vs. LEFT JOIN / IS NULL) is best to select values present in one table but missing in another one?

tl;dr: method 2 and 3 are same timing. method 1 takes the longest because it has to create the whole left table first.