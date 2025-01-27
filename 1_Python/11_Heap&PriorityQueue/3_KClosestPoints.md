O(n+klogn)
```python
import heapq
import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # min-heap of tuple (distance, point)
        heap = []
        for point in points:
            distance = math.sqrt(point[0]**2+point[1]**2)
            heap.append((distance, point))
        
        heapq.heapify(heap)
        output = []
        for _ in range(k):
            min_distance_point = heapq.heappop(heap)[1]
            output.append(min_distance_point)
        
        return output
```

也可以Ot(nlogk)
```python
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxHeap = []
        for x, y in points:
            dist = -(x ** 2 + y ** 2)
            heapq.heappush(maxHeap, [dist, x, y])
            if len(maxHeap) > k:
                heapq.heappop(maxHeap)
        
        res = []
        while maxHeap:
            dist, x, y = heapq.heappop(maxHeap)
            res.append([x, y])
        return res
```