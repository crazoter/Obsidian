#BigData 

Reducer secondary sorting

Problem: 
 = 
You want the values to be sorted (by a 2nd key) in the reducer.

Solution: 
 = 
- Mapper sends tuples to reducer in <key, <2nd key, value>> format.
- Each reducer will handle a separate key.
- Each reducer can then sort their data by the 2nd key.



![[Pasted image 20210918153941.png]]
