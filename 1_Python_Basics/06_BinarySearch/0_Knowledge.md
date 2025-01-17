Binary Search

```py
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        while l <= r:  # 修改为 <=
            mid = l + (r - l) // 2  # 防止溢出
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                r = mid - 1  # 收缩右边界
            else:
                l = mid + 1  # 收缩左边界
        return -1
```