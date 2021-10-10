1)Initialization
 =
```python
arrayOfData = ['Alice','Bob','Carol','Daniel']
numOfPartitions = 3

dataRDD = sparkContext.parallelize(arrayOfData, numOfPartitions)
```
- Immutable
	- Create new RDDs to change data
- From user's perspective, the RDD looks like it's a single object
	- In reality, it's partitioned by the Spark Context (sc); in the above example it's split into 3 partitions

2)Transformations (i.e. mapreduce stuff)
 =
 RDD --> RDD in another form
```python
# Transformations
newRDD = dataRDD.[map](lambda x : f(x))
# Transformations are lazy
# Transformation list: map, order, groupBy, filter, join, select
```
- Transformations are lazy
- Transformations are executed in parallel, based on how the data is distributed.
![[Pasted image 20211005111700.png|200]]
- Two types of transformations:
- **Narrow Dependencies**: Only need data from 1 partition
	- map, filters, contains
- **Wide Dependencies**: Need data from M partitions
	- groupBy, orderBy

3)Actions: Executing the transformations
 =
- Getting the data from the RDD, triggering the transformations
```python
newRDD.collect()
# [5,3,5,6]
```
- Warning: Each action will read the file again and trigger every transformation again.

3.5)Caching (performing n actions without recomputing)
 =
 - Caching is an action to tell Spark to execute the previous transformations and save it in memory (of each worker node)
 - Subsequent transformations will build on this cached data.
 - If workers run out of memory, evict "least used" RDDs
	 - Cache small and commonly used data
```python
# Initialization
lines = spark.textFile('hdfs://...')
# Transformations
errors = lines.filter(lambda s : s.startswith('E'))
msgs = errors.map(lambda s : s.split("\t")[1])
# Cache (action)
msgs.cache()
# Alternatives: msgs.persist() to save to disk of the workers
# msg.save(): send results back to driver to save it to hdfs
# Subsequent transformation + action uses cache
msgs.filter(lambda s : "mysql" in s).count()
msgs.filter(lambda s : "php" in s).count()

```

Other examples
 =
![[Pasted image 20211005111843.png]]

Internals of Spark: DAG
 =
- Stores RDDs and transformations applied to them as a DAG format
- Transformations that require M partitions (**Wide Dependencies**) will create a new "stage".
- The idea is that Spark will try to perform consecutive transformations on the same machine without network I/O or shuffling.

Images below are optional; already summarized above
![[Pasted image 20211005114422.png|300]]

![[Pasted image 20211005115648.png|300]]

Fault Tolerance
 = 
- Spark stores data in RAM
- can't use Hadoop's idea of duplication data for fault tolerance (too much RAM used)
- uses "lineages"

Lineages
 =
- If a worker node goes down:
	- Spark has the DAG to represent all RDDs and their transformations
	- Spark inits a new worker node 
	- Spark uses the DAG to identify the RDDs & transformations by the downed node and uses the new node to compute it