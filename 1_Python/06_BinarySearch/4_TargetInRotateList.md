这道题要做对，需要对边界有清晰的认知

```python
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r: # 要包括相等的情况
            mid = (l+r)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] <= nums[r]: # 要包括右边界
                # 右半部分有序
                if nums[mid] < target <= nums[r]: # 要包括右边界
                    # target在右半部分
                    l = mid + 1
                else:
                    # target不在右半部分
                    r = mid - 1
            elif nums[mid] >= nums[l]: # 要包括左边界
                # 左半部分有序
                if nums[l] <= target < nums[mid]: # 要包括左边界
                    # target在左半部分
                    r = mid - 1
                else:
                    # target不在左半部分
                    l = mid + 1
        return -1
```