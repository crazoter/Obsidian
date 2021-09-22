#BigData 

L1 (CS4225), L1 (CS5425) - 02/09/2021 - 18:30

#### Distance / Similarity measures
- We formally define “near neighbors” as points that are a
"small distance” apart
- To measure the distance between objects x and y, we need a
function ((x, y) which we call a “distance measure”
- Similarity measures are the opposite: lower distance = higher
similarity, and vice versa

#### Metrics
##### Euclidean Distance (between points)
1. ![[Pasted image 20210918162340.png|300]]
##### Manhattan Distance (between points)
1. ![[Pasted image 20210918162405.png|300]]
2. ![[Pasted image 20210918162411.png|75]]
##### Cosine Similarity (between vectors)
1. From point of origin
2. (higher value cosTheta = more similar)
3. ![[Pasted image 20210918162222.png|300]]

##### Jaccard Similarity (between sets of objects)
1. Set intersection proportion
2. ![[Pasted image 20210918162552.png|400]]
3. **Jaccard Distance**
4. ![[Pasted image 20210918162717.png|300]]

#### Goals
##### All pairs Similarity
Given N documents, find all "near duplicate pairs" (within threshold)

##### Similarity search
Given document D, find all "near duplicates" with D

#### Challenges
1. Too many documents
2. Documents may be too large to handle efficiently on 1 machines

#### Essential steps
##### Shingling
1. Convert docs to sets of k-shingles / k-gram
![[Pasted image 20210918163153.png]]
2. Since documents are sets of shingles, we can use Jaccard similarity (set intersection proportion) to get similarity.
3. e.g. the one-hot-encoding table below, not necessary to construct 
4. ![[Pasted image 20210918163402.png]]

##### Min-hashing
1. Rationale: Many docs, don't want to compute pairwise set intersection proportion (Jaccard similarity)
	1. Convert these sets to short signatures of each document while preserving Similarity
	2. Signatures used as keys to find near-duplicates	
2. Thus: hash each column **C** to a signature **h(C)**
	1.  Small enough to fit in ram
	2. High similarity docs usually have same signature
3. MinHash algorithm:
	1. Shingles represent a document
	2. Hash each shingle to an int
	3. Get min of all hashes
	4. Pr[h(C1) = h(C2)] = Jaccard-Sim(C1, C2)
	5. ![[Pasted image 20210918164339.png]]
	6. We can then concat multiple hashes to create the signature
	7. Perform further checking to make sure they are actually similar 
	8. ![[Pasted image 20210918164722.png]]
	9. ![[Pasted image 20210918165019.png]]

#### Clustering
Group similar points together
##### K-Means
1. Find centroid (cluster centre) of K (hyperparam) clusters
2. Chicken & egg problem. So
3. Initialize K centroids as K random points
4. Assign each point to the nearest centroid
5. Shift centroid to average of assigned points
6. Repeat to convergence threshold 

###### Implementing K-Means using MapReduce
1. MapReduce is not very efficient for iterative algorithms
1. Map(clusterId, point): 
	1. newId = nearestClusterid(clusters, point)
	2. extendedPt = extendPoint(point)
		1. Extending a point is a trick
		2. Take data for point p (x,y)
		3. Add 1 more variable to keep track of counts (assigned to cluster)
		4. Honestly doesn't matter that much; just a way to track # of points in cluster.
	3. Aggregate counts into a hashtable (for each cluster)
	4. In method Close(): for every point in hashtable, emit(newId, point)
		1. Aggregating will reduce it to O(clusters * iterations * dimensions);
2. Reduce(clusterId, points):
	1. accumulate points assigned to cluster
	2. newCentroid = compute centroid for clusterId
	3. emit(clusterId, newCentroid)