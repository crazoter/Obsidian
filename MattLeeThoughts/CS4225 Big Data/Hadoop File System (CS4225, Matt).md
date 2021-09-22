 #BigData

**Distributed file system**
Traditional: Master server calling compute server which uses storage server
- Not very efficient as there's a lot of moving of data to the compute nodes
![[Pasted image 20210912171908.png]]
![[Pasted image 20210912172047.png]]
   

Have many commodity hardware (scale sideways) rather than stacking a cracked computer
![[Pasted image 20210912172106.png]]
We don't want too many small files (too much overhead of reading metadata)
![[Pasted image 20210912172827.png]]
![[Pasted image 20210912172833.png]]
   

Generally use hadoop terminology for this course
![[Pasted image 20210912172849.png]]
![[Pasted image 20210912172856.png]]   

Datanode will directly send the data to the application (HDFS client)

HDFS namenode is just a lookup

Can have multiple datanodes with the same data (data redundancy). Namenode will decide which datanode is closest to the client.

For writing files, it's the reverse process:

1.  Application sends req to namenode
2.  Namenode tells application where to send it to and involved datanodes (on different racks) for replicas.
3.  Application sends to datanode
4.  Application will send to first datanode
5.  First datanode will forward to 2nd datanode, who will forward to 3rd datanode etc.

![[Pasted image 20210912172914.png]]
Same machines used for the mapreduce task stuff and the hadoop file system
![[Pasted image 20210912172932.png]]
![[Pasted image 20210912172941.png]]