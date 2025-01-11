寻找最长子序列的长度，注意，这里暂时不考虑list的原始数据，也就是说对list排序后的连续数列也算。

Solution Ot(n):
```python
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums = set(nums)
        longest = 1
        for num in nums:
            if num - 1 in nums:
                continue

            current_longest = 1
            n = num
            while(n+1 in nums):
                current_longest += 1
                n += 1

            longest = max(longest, current_longest)
            
        return longest
```


## Backup Solutions

初见：
```python
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums.sort()
        longest_set = set()
        longest = 1
        for i in range(0, len(nums)-1):
            if nums[i] + 1 == nums[i+1]:
                longest += 1
            elif nums[i] == nums[i+1]:
                continue
            else:
                longest_set.add(longest)
                longest = 1
        longest_set.add(longest)
        ls = sorted(longest_set, reverse=True)
        return ls[0]
```

优化（去掉set）
```python
from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0  # 如果数组为空，直接返回 0

        nums.sort()  # 对数组排序
        longest = 0  # 用于记录最长连续序列的长度
        current_length = 1  # 当前连续序列的长度

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                # 如果当前数字与前一个数字相同，跳过
                continue
            elif nums[i] == nums[i - 1] + 1:
                # 如果当前数字是连续的，增加当前序列长度
                current_length += 1
            else:
                # 如果不连续，更新最长长度，并重置当前长度
                longest = max(longest, current_length)
                current_length = 1

        # 最后再检查一次当前序列的长度
        return max(longest, current_length)
```