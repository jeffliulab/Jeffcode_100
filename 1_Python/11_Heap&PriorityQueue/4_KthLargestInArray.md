Ot(nlogk)
```python
class Solution:
    def findKthLargest(self, nums, k):
        return heapq.nlargest(k, nums)[-1]
```

Min-Heap
```python
import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # max-heap
        heap = []
        for num in nums:
            if len(heap) < k:
                heap.append(num)
            else:
                break
        heapq.heapify(heap)
                
        for i in range(k,len(nums)):
            heapq.heappush(heap,nums[i])
            heapq.heappop(heap)
        
        return heap[0]
```