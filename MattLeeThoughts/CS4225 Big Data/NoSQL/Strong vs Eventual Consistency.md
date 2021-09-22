#NoSQL 

![[Pasted image 20210919213545.png]]
**Strong consistency**: Any reads immediately after an update will give the same result for all observers
- Involves blocking reads until the data centers are updated

**Eventual consistency**: Eventually all reads will return the last written value (data will eventually be propagated to all data centers)

##### Implications of Eventual consistency
- Weaker consistency 
- Higher availability
- In practice, NoSQL systems can be modified to tune this trade-off (tunable consistency)
- 