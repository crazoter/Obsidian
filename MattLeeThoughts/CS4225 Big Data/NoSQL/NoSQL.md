#BigData #NoSQL #MongoDB

1. Non-relational DB
2. More recently understood as "not-only SQL"; using relational & non-relational DB for the data they are suitable for

##### Properties
- No fixed schema
- No relations (tables)
- Weaker consistency, higher availabilty ([[Strong vs Eventual Consistency]], [[ACID vs BASE]])
- [[Duplication]] (i.e. denormalization)
- ![[Pasted image 20210919214751.png]]

##### Traits
- Horizontally scalable (rather than making machines more powerful)
- Replicate / distribute data over many servers
- Simple call interface
- Weaker concurrency than RDMBS
- Efficient use of distributed indexes and RAM
- Flexible Schema


#### Types
#####  Document store
1. Has multiple Collections ("Tables")
2. Collections can have multiple documents (JSON objects)
3. API: CRUD (no need to memorize)
	1. Allow some querying based on JSON fields
	2. **Create**: Insert JSON into Collection
		1. `db.users.insert({kvp});`
	3. **Read**:
		1. ![[Pasted image 20210919210918.png|300]]
	4. **Update**:
		1. ![[Pasted image 20210919211022.png|300]]
	5. **Delete**
		1. ![[Pasted image 20210919211108.png|300]]
####  Key-Value store
1. Keys are primitive and can be queried, value can be anything
2. API:
	1. Get
	2. Put
	3. Multi-get / Multi-put
	4. Range queries
3. Uses:
	1. Quick small continuous reads & writes
	2. Storing basic info
	3. Slow for complex queries
4. Examples:
	1. Caches
	2. Data that is processed individually e.g. user data
5. Implementation:
	1. Non-persistent: hashtable
		1. Memcached, redis
	2. Persistent: data stored to disk

#### Wide Column Store
![[Pasted image 20210919212216.png|500]]
- **Rows** describe entities
- **Columns** are attributes
- **Column families**: Columns can be grouped
	- Columns must be unique, but only within a family (allowed dupe in another family)
- **Sparsity:** If cell doesn't store anything, it doesn't take up any space (scalability)

#### Graph Databases
- Discuss in last few weeks of class

#### Trying MongoDB out on web
[MongoDB getting started](https://docs.mongodb.com/manual/tutorial/getting-started/)