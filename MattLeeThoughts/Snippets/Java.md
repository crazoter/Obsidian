```java
# Region marker		 | Syntax		 | Name of snippet
#region SHORTSNIPPET | source.java   | priorityqueue
// Import: java.lang.* | java.util.*
// compare(x,y) = 0: if (x==y) , -1: if (x < y) , 1: if (x > y)
PriorityQueue<Integer> pq = new PriorityQueue<>((x, y) -> Integer.compare(y, x));
```