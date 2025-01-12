Find two that the sum of them fits the target in a list.

Level1: make sure the input has only one valid output

Level2: no gurantee on input, need find all possible solutions

Level3: "three pointers"

Use two pointers to achieve Ot(n) and Os(1)

## Level1

找出一组组合

```py
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers)-1
        while(l < r):
            summ = numbers[l] + numbers[r]
            if summ == target:
                return [l, r] # 0-indexed, if it is 1-indexed, it should return [l+1, r+1]
            elif summ < target:
                l += 1
            elif summ > target:
                r -= 1
        return False
```

## Level2

找出所有的组合

```py
from typing import List

class Solution:
    def twoSumAllSolutions(self, numbers: List[int], target: int) -> List[List[int]]:
        l, r = 0, len(numbers) - 1
        results = []
        
        while l < r:
            current_sum = numbers[l] + numbers[r]
            if current_sum == target:
                results.append([l, r])  # 0-indexed
                # 跳过重复元素
                while l < r and numbers[l] == numbers[l + 1]:
                    l += 1
                while l < r and numbers[r] == numbers[r - 1]:
                    r -= 1
                # 移动指针
                l += 1
                r -= 1
            elif current_sum < target:
                l += 1
            else:
                r -= 1
        
        return results
```

## Level3

找出三个数的组合。用一个for i 循环，让这个问题转变为一个two pointers问题。

```py
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = []
        nums.sort()
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            l = i + 1
            r = len(nums) - 1
            while(l < r):
                summ = nums[i] + nums[l] + nums[r]
                if summ == 0:
                    output.append([nums[i],nums[l],nums[r]])
                    while(l<r and nums[l]==nums[l+1]):
                        l+=1
                    while(l<r and nums[r]==nums[r-1]):
                        r-=1
                    l+=1
                elif summ < 0:
                    l += 1
                elif summ > 0:
                    r -= 1
                
        return output
```

分析时间复杂度
```
要找到三个数，本质上是在寻找所有可能的三元组组合。
对于长度为 n 的数组，总的三元组组合数是 C(n,3) = n!/(3!(n-3)!) ≈ O(n³)
通过排序 + 双指针的方法，我们把最内层的查找从 O(n) 优化到了 O(1)
对于每个第一个数（n个选择）
使用双指针一次性处理剩下的两个数（O(n)时间）
所以总复杂度是 O(n * n) = O(n²)
```

