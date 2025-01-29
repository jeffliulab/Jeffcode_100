这道题直观来讲用sorted(ls)很简单，注意中位数是mid = (ls[l//2-1] + ls[l//2])/2和mid = ls[l//2]。

但是sorting的方法太过低效，Ot(nlogn)，所以需要用heap来存储。

但是用heap又有一个问题，那就是heap的访问效率不是O1。heap的主要访问操作是访问heap top，
所以这道题可以巧妙地转换为维护两个heap。

DeepSeek优化版（非常巧妙！）
```python
import heapq
class MedianFinder:

    def __init__(self):
        self.large = [] # large side is minHeap
        self.small = [] # small side is maxHeap

    def addNum(self, num: int) -> None:
        # 将元素加入 small 堆（大顶堆）
        heapq.heappush(self.small, -num) 

        # 将 small 堆的最大元素移动到 large 堆（小顶堆）
        heapq.heappush(self.large, -heapq.heappop(self.small)) 

        # 如果 large 堆的大小大于 small 堆，将 large 堆的最小元素移动到 small 堆
        if len(self.large) > len(self.small): 
            heapq.heappush(self.small, -heapq.heappop(self.large))

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -self.small[0]  # small 堆的最大元素
        else:
            return (-self.small[0] + self.large[0]) / 2  # 两个堆的堆顶元素的平均值
```


上面这个优化版（不需要比较两个heap，return的时候也不需要判断奇偶性）的思路：
```
1. 为什么优化版本不需要显式比较？
在原始代码中，显式地比较了 num 和 self.large[0]，以决定将 num 加入 self.small 还是 self.large。而在优化版本中，通过以下方式避免了显式比较：
    步骤 1：先将 num 加入 self.small 堆
        无论 num 的大小如何，都先将其加入 self.small 堆（大顶堆）。
        这一步的目的是确保 self.small 堆始终包含较小的一半元素。
    步骤 2：将 self.small 堆的最大元素移动到 self.large 堆
        通过 heapq.heappush(self.large, -heapq.heappop(self.small))，将 self.small 堆的最大元素移动到 self.large 堆。
        这一步的目的是确保 self.large 堆始终包含较大的一半元素。
    步骤 3：调整堆的平衡
        如果 self.large 堆的大小大于 self.small 堆，则将 self.large 堆的最小元素移动回 self.small 堆。
        这一步的目的是确保两个堆的大小差不超过 1。
通过这种方式，优化版本避免了显式比较 num 和 self.large[0]，而是通过堆的性质自动完成了元素的分配。

2. 为什么优化版本不需要判断奇偶性？
在原始代码中，findMedian 方法中判断了数据流的总长度是奇数还是偶数，然后根据奇偶性返回不同的结果。而在优化版本中，通过以下方式避免了显式的奇偶性判断：
    堆的大小关系直接反映了数据流的奇偶性
        如果 self.small 堆的大小大于 self.large 堆，说明数据流的总长度是奇数，且中位数是 self.small 堆的最大元素。
        如果两个堆的大小相等，说明数据流的总长度是偶数，且中位数是 self.small 堆的最大元素和 self.large 堆的最小元素的平均值。
    通过堆的大小关系直接返回中位数
        如果 len(self.small) > len(self.large)，直接返回 -self.small[0]（即 self.small 堆的最大元素）。
        否则，返回 (-self.small[0] + self.large[0]) / 2（即两个堆的堆顶元素的平均值）。
这种方式利用了堆的大小关系直接反映了数据流的奇偶性，因此不需要显式判断奇偶性。
```

自己写的原版（ChatGPT和Claude都看不出我的原本代码的问题，DeepSeek一眼看出来了）
```
import heapq
class MedianFinder:

    def __init__(self):
        self.large = [] # large side is minHeap
        self.small = [] # small side is maxHeap

    def addNum(self, num: int) -> None:
        # 如果large还没有东西，就把第一个元素加入到large里
        if not self.large:
            heapq.heappush(self.large, num)
            return
        
        # 和large里的最小元素进行比较，判断加入到哪一侧
        # BUG：这里重复判断了！
        mid_large = self.large[0]
        if mid_large <= num: 
            heapq.heappush(self.large, num)
        else:
            heapq.heappush(self.small, - num)

        # 如果两侧不平衡，将大的一侧的元素分到小的一侧，保证len相差不超过1
        while len(self.large) - len(self.small) > 1:
            heapq.heappush(self.small, - heapq.heappop(self.large))
        while len(self.small) - len(self.large) > 1:
            heapq.heappush(self.large, - heapq.heappop(self.small))


    def findMedian(self) -> float:
        if not self.small and not self.large:
            return 0
        if not self.small:
            return self.large[0]
        if not self.large:
            return - self.small[0]

        if (len(self.large) + len(self.small)) % 2 == 0:
            return (self.large[0] - self.small[0])/2
        else:
            if len(self.large) > len(self.small):
                return self.large[0]
            else:
                return - self.small[0]

```