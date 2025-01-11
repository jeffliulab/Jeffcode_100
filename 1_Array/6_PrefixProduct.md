知识点: prefix product and suffix product

Given an integer array nums, return an array output where output[i] is the product of all the elements of nums except nums[i].

Input: nums = [1,2,4,6]

Output: [48,24,12,8]

Input: nums = [-1,0,1,2,3]

Output: [0,-6,0,0,0]

Solution Ot(n), Os(n)
```python
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        list_product = [1]*len(nums)
        prefix_product = [1]*len(nums)
        suffix_product = [1]*len(nums)
        for i in range(1,len(nums)):
            prefix_product[i] = prefix_product[i-1] * nums[i-1] # 这里后面的nums[i-1]很关键，一开始写成nums[i]了
        for i in range(len(nums)-2, -1, -1):
            suffix_product[i] = suffix_product[i+1] * nums[i+1]
        for i in range(len(nums)):
            list_product[i] = prefix_product[i] * suffix_product[i]
        return list_product
```

减少list使用：(本质上并没有降低空间复杂度) 滞后指针的思想非常好
如果output不算在complexity里的话，这个解法的complexity是Os(1)
```python
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        list_product = [1]*len(nums)
        prefix = 1
        suffix = 1
        for i in range(0,len(nums)):
            list_product[i] = prefix
            prefix *= nums[i] # update prefix，这里有一个滞后，也就是这里算的prefix是用在下一次循环时计算的
        for i in range(len(nums)-1, -1, -1):
            list_product[i] *= suffix 
            suffix *= nums[i]
        return list_product

```
