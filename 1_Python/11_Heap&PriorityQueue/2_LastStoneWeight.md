如果石头重量不是特别大，数量不是特别多的情况下，用Bucket Sorting会更高效。

Ot(nlogn), Os(n)
```python
import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if not stones:
            return 0
        heap = [-num for num in stones]
        heapq.heapify(heap)
        while len(heap) >= 2:
            x = - heapq.heappop(heap)
            y = - heapq.heappop(heap)
            if x != y:
                heapq.heappush(heap, y - x)

        return - heap[0] if heap else 0
```