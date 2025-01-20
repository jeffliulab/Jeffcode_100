思路：
* 用l、r两个指针
* 总是比较mid和r，来决定收缩方向

```python
class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1  # 注意：右边界是索引，而不是值
        while l < r:  # 这里是严格小于，避免无限循环
            mid = (l + r) // 2
            if nums[mid] > nums[r]:  # 最小值在右边
                l = mid + 1
            else:  # 最小值在左边或就是 mid
                r = mid
        return nums[l]  # 此时 l == r，返回最小值
```

Q: 为什么逼近时是 l = mid + 1, r = mid？
```
在二分查找中，每次判断后，必须确保新的搜索范围依然包含最小值。我们来看具体的逻辑：

条件 1: nums[mid] > nums[r]
如果中间值 nums[mid] 比右边界值 nums[r] 大，说明最小值一定在右半部分。
例如，nums = [4, 5, 6, 1, 2]：
初始 l = 0, r = 4，mid = 2，nums[mid] = 6，nums[r] = 2。
很明显，最小值在右半部分，所以我们更新 l = mid + 1。

条件 2: nums[mid] <= nums[r]
如果中间值 nums[mid] 小于或等于右边界值 nums[r]，说明最小值在左半部分，或者就是 mid 本身。
例如，nums = [6, 1, 2, 3, 4]：
初始 l = 0, r = 4，mid = 2，nums[mid] = 2，nums[r] = 4。
最小值可能是 mid 或在左半部分，所以我们更新 r = mid。
通过这样的更新方式，我们确保 l 和 r 的范围始终包含最小值。
```