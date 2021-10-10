#NoSQL 

[[Strong vs Eventual Consistency]]
ACID
atomicity, consistency, isolation, durability

ACID vs BASE: Relational DBMS provide stronger (ACID)
guarantees, but many NoSQL system relax this to weaker

"BASE” approach:
- Basically Available: basic reading and writing operations are
available most of the time
- Soft State: without guarantees, we only have some probability of
knowing the state at any time
- Eventually consistent: Contrast to "strong consistency":
