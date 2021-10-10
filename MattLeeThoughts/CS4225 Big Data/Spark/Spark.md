#BigData 

Motivation
 =
 
Mapreduce issues:
1. A lot of network and disk I/O (mapper to reducer etc)
2. Not suitable for iterative processes
	1. e.g. modifying small amounts of data repeatedly, sequential workflow etc
	2. Mapreduce is more suitable for batch jobs, not jobs with a large number of steps

Solution: Spark
 = 

- Spark stores intermediate results in memory, especially for interative processing
	- Spill to disk if memory is insufficient

Benefits
 = 
 1. Easier and faster to program (think Spark & Hadoop is like FastAI & Tensorflow)

Library
 = 
![[Pasted image 20211004223215.png]]

Architecture
 = 
 ![[Pasted image 20211004223307.png]]
 1. User will give their tasks to the driver process
 2. Driver Process will distribute the work to the executors (workers)
 3. Cluster Manager decides what tasks should be run on what machines (think of it as a look-up server)

Evolution of Spark
 =
![[Pasted image 20211004223650.png]]
**Resilient Distributed Datasets:**
![[Pasted image 20211004223954.png|400]]
More on [[Resilient Distributed Datasets]]

**DataFrames**: Higher level (works on RDDs), represent a table in SQL
- Spark takes SQL / exposes SQL-like API and converts it into RDD transformations
- more user friendly than RDD
- anything run in SQL can be run in Spark
- ![[Pasted image 20211005122410.png|300]]
- ![[Pasted image 20211005122650.png|300]]
- ![[Pasted image 20211005122706.png]]
- ![[Pasted image 20211005122813.png]]

**DataSets**: Same as DataFrame, but Type safe
- All the types of the columns are already specified
- Faster and checked during compilation
- ![[Pasted image 20211005123019.png]]

Spark example
https://colab.research.google.com/drive/18vqsZcie3UdlLiw-UGXw_LHnZVCcw4et