这道题本来是SlidingWindow里的，但是本着从上往下，从易到难的态度，故而在这里直接进入Deque的部分。


非优化deque: Ot(n*k)
```py
from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque(maxlen=k)  # 用来存储当前窗口的值
        result = []  # 用来存储每个窗口的最大值
        
        for i in range(len(nums)):
            # 把新的元素加入队列
            q.append(nums[i])
            if len(q) == k:
                result.append(max(q))  # 遍历队列找最大值
        
        return result
```

优化deque： （只在deque中存储index，并保持deque的递减）
```py
from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        r = []
        for i in range(len(nums)):
            # add into q
            while(q and nums[q[-1]] < nums[i]):
                q.pop()
            q.append(i)

            # remove front
            while(q and q[0] < i-k+1):
                q.popleft()
            
            # remember result
            if i-k+1 >= 0:
                r.append(nums[q[0]])
        
        return r
```