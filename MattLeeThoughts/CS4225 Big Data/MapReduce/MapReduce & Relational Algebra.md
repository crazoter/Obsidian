#BigData 

MapReduce to implement relational algebra:
#### Projection (Select columns)
![[Pasted image 20210912173008.png|350]] 
Implement via: Map to extract attributes from tuples

-------------------------------------

#### Selection (Select tuples)
![[Pasted image 20210912173015.png|300]]
Implement via: Map to emit only tuples that match condition

-------------------------------------

#### Groupby
![[Pasted image 20210912173025.png|300]]
Implement via: Map to perform the groupby, Reducer to perform the aggregation Method

-------------------------------------

L1 (CS4225), L1 (CS5425) - 02/09/2021 - 18:30

#### Inner Join:
![[Pasted image 20210918154353.png|200]]
Methods for implementing Inner Join with MapReduce:
##### 1. Map / Broadcast Join
1. Perform the join in the mapper:
2. Store 1 table in memory as a hashtable, the key being the column to join by
3. For every record in big table, find tuples that match the join column,
	1. then generate records that join with smaller table
4. Cannot work if both tables too big to fit into memory
5. ![[Pasted image 20210918154734.png|400]]
###### Reduce-side ("Common") Join
1. Perform the join in the Reducer.
2. Mapper: Emit kvp <key, <2nd key, value>>:
	1. Key				  = the column to join by
	2. 2ndary key	= the table name
	3. Value			= the remaining attributes
![[Pasted image 20210918155815.png|600]]
3. Reducer:
	1. Perform [[MapReduce Secondary Sort]]
	2. ![[Pasted image 20210918161553.png|250]]
	3. Reducers handle only 1 key each, so can just cross join by table name
		1. For all tuples in X, Join it with all tuples from Y