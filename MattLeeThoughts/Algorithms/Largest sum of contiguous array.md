#algorithms

Initialize:
    max_so_far = INT_MIN
    max_ending_here = 0

Loop for each element of the array
  (a) max_ending_here = max_ending_here + a[i]
  (b) if(max_so_far < max_ending_here)
            max_so_far = max_ending_here
  (c) if(max_ending_here < 0)
            max_ending_here = 0
return max_so_far

Explanation
 ===
Variables:
1. max_so_far: the value to store the answer (the name is self-explanatory)
2. max_ending_here: this variable is not very well-named; a better name would be "current largest sum" or something.

Key steps:
(a): max_ending_here (or current largest sum) basically acts as an accumulating value, adding the current value as it iterates across the array. Nothing much to see here.
(b): If your current largest sum is larger than the max sum we've seen so far, then we update the max sum. Again, nothing exciting.
(c): This step is deceitfully simple, and it's the core idea behind this algorithm. The idea is this:

1. Assume we have accumulated a bunch of numbers (e.g. the first n numbers) and the total sum of these numbers is negative.
2. Because it's negative, we know that including the first n numbers into our current largest sum will just decrease it. 
	1. After all, even if we were to encounter +ve numbers in the future, we will get a larger sum by omitting the 1st n numbers.
3. Thus, whenever the sum reaches negative, we simply say "okay, let's restart and not use the previous contiguous subarray we've explored". This is why the value is reset to 0, because it's in essence discarding the previous entries.
4. LIkewise, if the current sum doesn't reach 0, then we know that it can be added to future subarrays without decreasing its value; thus we don't discard it and thus we don't reset the current largest sum to 0.
5. Let's look at the correctness of the answer. Even if the value decreases in the future by encountering negative numbers, we are assured that the max value is recorded properly at step (b). 