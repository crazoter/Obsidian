 #BigData

Motivation: Traditional distributed systems
 = 
- Master server calls compute server to get data frp, storage server
- Inefficient; a lot of IO to transfer data from storage to compute
![[Pasted image 20210912171908.png|500]]
**CORE IDEA OF DISTRIBUTED FILE SYSTEM:** make the server containing the data run the processing of the data instead (i.e. run the mapper functions on the distributed servers directly)

![[Pasted image 20210912172047.png|500]]
   
As a result, we can scale sideways rather than stacking powerful compute servers:

![[Pasted image 20210912172106.png|500]]

We don't want too many small files (too much overhead of reading metadata), so we store files as chunks.

![[Pasted image 20210912172827.png|500]]

In this module we use hadoop terminology

![[Pasted image 20210912172833.png|300]]
   

![[Pasted image 20210912172849.png]]
![[Pasted image 20210912172856.png]]   

When interacting with the hadoop filesystem:
1. User uses the application (the HDFS client) to interact with the file system.
2. File system comprises of the HDFS namenode (lookup) and HDFS datanodes (storage nodes).
3. application will check in with HDFS namenode to lookup where the data is stored.
4. Datanode will directly send the data to the application (HDFS client).
	1. Hadoop may duplicate the same data on multiple datanodes for data redundancy. 
	2. Namenode will return the closest / best datanode containing the relevant data.

For writing files, it's the reverse process:

1.  Application sends req to namenode
2.  Namenode tells application where to send it to and involved datanodes (on different racks) for replicas.
3.  Application sends to datanode
4.  Application will send to first datanode
5.  First datanode will forward to 2nd datanode, who will forward to 3rd datanode etc.

![[Pasted image 20210912172914.png]]

Mapreduce tasks can be executed on the hadoop datanodes (distributed computation).

![[Pasted image 20210912172932.png]]
![[Pasted image 20210912172941.png]]

Questions from Tutorial 2

**a) MapReduce and the Google File System (GFS) were designed to work well together. What important optimization in MapReduce is enabled by having GFS expose block replica locations via an API?**

Block replica locations: basically blocks of data in different servers.
Optimization: The MapReducer scheduler can arrange the map function to be run on the server housing the data instead of moving the data into a computing server.

**b) List two features that are originally designed for relational databases and are now integrated into the MapReduce/Hadoop software stack.**

- High level languages (for querying)
- Column stores (column families)
