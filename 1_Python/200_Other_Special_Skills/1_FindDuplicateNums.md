Prerequisite: 01_List, 03_TwoPointers,05_LinkedList(FastSlowPointers)

## Solution1: Negative Marking

Ot(n), Os(1)

```py
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for num in nums :
            idx = abs(num) - 1 
            if nums[idx] < 0 :
                return abs(num)
            nums[idx] *= -1
        return -1
```

## Solution2: Fast and Slow Pointers

Ot(n), Os(1)

```py
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow
```