#BigData 
# Vertical Partitioning (by column)
![[Pasted image 20210923190104.png]]

# Horizontal Partitioning: Split by row
![[Pasted image 20210923190158.png]]
Partition = split rows and put in separate machines
#### Choosing a partition key
1. A column that often used by group-by queries
	1. No need to perform the group-by operation if the data is already grouped-by via partition; improves data locality

#### Partitioning Strategy
![[Pasted image 20210923190726.png]]
#### By range of values of the key
1. managed by an auto balancer
![[Pasted image 20210923190738.png]]
#### By hashing the key, then use the range approach
![[Pasted image 20210923191946.png]]
##### Consistent Hashing
1. Think of it as a circle (mod this max num of partitions)
2. Shift items to the closest node in clockwise

##### Replication Strategy
1. Replicate the data in say n nodes in front of main node, in clock-wise direction

#### MongoDB Architecture
![[Pasted image 20210923192349.png]]
Mongos: Controller
Config: metadata on where the data is, based on partition key e.g. on hashing
Shards: secondary are for duplication

![[Pasted image 20210923192539.png]]
![[Pasted image 20210923192638.png]]