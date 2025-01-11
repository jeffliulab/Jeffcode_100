Input: 
nums = [3,4,5,6], target = 7

Output: [0,1]

Input: nums = [4,5,6], target = 10

Output: [0,2]

Input: nums = [5,5], target = 10

Output: [0,1]

Solution: O(n)
```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in hashmap:
                return [hashmap[diff], i]
            else:
                hashmap[n] = i
```