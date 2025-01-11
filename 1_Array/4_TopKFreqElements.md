Input: nums = [1,2,2,3,3,3], k = 2

Output: [2,3]

Input: nums = [7,7], k = 1

Output: [7]

Solution Ot(n+ulogu), Os(u+k)
```python
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict_nums = {}
        for num in nums:
            dict_nums[num] = dict_nums.get(num, 0) + 1
        list_nums = list(dict_nums.items())
        list_nums = sorted(list_nums, key=lambda x:x[1], reverse=True)
        return [x[0] for x in list_nums[:k]]
```