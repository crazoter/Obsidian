#BigData 
# MapReduce

![[Pasted image 20210912161500.png]] 
| Bandwidth | Latency                                           |
| --------- | ------------------------------------------------- |
| GB/s      | Time taken by packet for 1-way / round-trip in ms |

![[Pasted image 20210912161519.png]]
**Storage Hierarchy:**

| Local Server   | Rack       | Datacenter   |
| -------------- | ---------- | ------------ |
| Fast but small | In-between | Big but slow |

![[Pasted image 20210912161542.png]]
## Challenges
- How do we assign work units to workers?
- What if we have more work units than workers?
- What if workers need to share partial results?
- How do we aggregate partial results?
- How do we know all the workers have finished?
- What if workers die/fail?

## Typical Big Data Problem
- Iterate over a large number of records
- Extract something of interest from each
- Shuffle and sort intermediate results
- Aggregate intermediate results
- Generate final output

## Introducing MapReduce
![[Pasted image 20210912162056.png]]
![[Pasted image 20210918171759.png]]
   
**Initial State**: The initial state is (k1, v1); k1 can be just the booth id etc.

**Map stage**: Workers map their data to kvp, and then concatenate in 1 big pile.

**Shuffle**: Sort pile by key.

**Reduce**: Reduce all the values into something which can then be stored in the database.
- In MapReduce, this operation takes in the entire list

![[Pasted image 20210912162204.png]]
o Programmers specify two functions:
1. map (k, V) → List(k2, v2)
2. reduce (k2, List(v2)) → List(k3, V3)
• All values with the same key are sent to the same reducer
o Not quite...usually, programmers optionally also specify:
partition
• Used to decide which reducer will handle each key
combine
• Mini-reducers that run in memory after the map phase
• Used as an optimization to reduce network traffic

![[Pasted image 20210912162246.png]]
   

Logically looks like this ^, but note that for MapReduce, the "Fold" step takes in the full array

   
![[Pasted image 20210912162322.png]]

**Implementation**:
1.  Split your kvp data into chunks
2.  Pass them into your mapper workers
3.  Each mapper worker will partition by key on the intermediate files
4.  Each reducer worker will handle 1 unique key (in this case, 0 / 1):
	- By default, assignment of key -> worker is done by hash function
	- Hash(key) mod reducerCount.
	- Basically partition into the reducers we want to use to handle the key
1.  They will read from the partitions and output to the file (technically the shuffle step)
2.  Reducers must wait for Mappers, but can start once there is data in intermediate files
3.  Workers operate in <label class="ob-comment" title="" style=""> parallel <input type="checkbox"> <span style=""></span></label>
4.  Master will keep track of Workers (re-assign task if they fail)

## Combiners
**Combiner**: combine output from Mappers (so as to make it more efficient by reducing final I/O by Reducer)
![[Pasted image 20210912163330.png]]
 ### Correctness of combiner
1. Reducer operations must be runnable in any order without affecting correctness (e.g. max, min, sum).
2.**Reducer / Combiner Operation** must be **Associative** & **Commutative**.
 ![[Pasted image 20210912163702.png]]
- Correctness of Combiner
	- The user must ensure that the combiner does not affect the
	correctness of the final output, whether the combiner runs 0, I,
	or multiple times
	- Example: in election example, the combiner and reducer are a “sum"
	over values with the same key. Summing can be done in any order
	without affecting correctness:
		- e.g. sum(sum(1, 1), 1, sum(1, 1, 1)) = sum(1, 1, 1, 1, 1, 1) = 6
- The same holds for “max” and “min”
- How about "mean" or "minus”?
	- Answer: No! E.g. mean(mean(1, 1), 2) # mean(1, 1, 2).
		- (Optional) In general, it is correct to use reducers as combiners if the
		reduction involves a binary operation (e.g. +) that is both
		- Associative: a + (b + c) = (a + b) + c
		- Commutative: a + b = b + a
 ![[Pasted image 20210918172132.png]]

 
 ![[Pasted image 20210912164830.png]]
    
- Sort because we want the keys to be grouped together (in their own partitions; each partition can have multiple keys inside).
- 1 partition to 1 reducer
- N keys to 1 partition
- We can extend the sort function to sort by secondary keys (but it'll still be partitioned by the main key)

![[Pasted image 20210912170912.png]]
Try to minimize I/O
Make sure memory of machines can handle memory required
![[Pasted image 20210912170945.png]]
![[Pasted image 20210912170940.png]]
   

"counts" map in this case falls under "state"