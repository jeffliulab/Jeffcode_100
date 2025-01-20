这道题本来是找中位数，但是由于用该方法找中位数不是最优解，所以我单独拿了出来做讨论。

假设有list1和list2两个list，用O(log(m+n))的时间复杂度找到第k小的数字。

第k小法：（找中点k的情况）
```
1、假如两个list一共100个数字，那么就要找到第50小的数字（暂时先讨论思路，不讨论奇数偶数）
2、判断list1和list2的中点并进行比较，现在两个中点加起来一共有50个数字。如果list1的中点比list2小，那么第50小的数字一定不会出现在list1的前一半中。将list1的左边界更新为list1的中点。
3、假如list1的中点前面有10个数字，那么现在就排除掉了第1-第10小的数字，接下来要找的就是剩下的数字中第40小的数字。
4、接着比较，接着剔除，直到剩下找的是第1小的数字，也就是下一个数字
```

```python
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # 定义查找第 k 小的数字逻辑
        def findKth(A, B, k):
            l1, l2 = 0, 0  # 两个数组的起始位置
            while True:
                # 如果 A 被排空，直接返回 B 的第 k 小
                if l1 == len(A):
                    return B[l2 + k - 1]
                # 如果 B 被排空，直接返回 A 的第 k 小
                if l2 == len(B):
                    return A[l1 + k - 1]
                # 如果只需要找第 1 小，返回两个数组当前首元素的较小值
                if k == 1:
                    return min(A[l1], B[l2])

                # 计算两数组当前中间位置
                mid1 = min(len(A), l1 + k // 2) - 1
                mid2 = min(len(B), l2 + k // 2) - 1
                # 中间元素的值
                A_val = A[mid1]
                B_val = B[mid2]

                # 排除较小部分元素
                if A_val <= B_val:
                    k -= (mid1 - l1 + 1)  # 排除掉 A 的左半部分
                    l1 = mid1 + 1        # 更新 A 的起始位置
                else:
                    k -= (mid2 - l2 + 1)  # 排除掉 B 的左半部分
                    l2 = mid2 + 1         # 更新 B 的起始位置

        # 总长度
        total_len = len(nums1) + len(nums2)
        if total_len % 2 == 1:
            # 奇数长度，直接找第 (total_len // 2 + 1) 小的数字
            return findKth(nums1, nums2, total_len // 2 + 1)
        else:
            # 偶数长度，找第 (total_len // 2) 和 (total_len // 2 + 1) 小的数字，取平均值
            return (findKth(nums1, nums2, total_len // 2) + findKth(nums1, nums2, total_len // 2 + 1)) / 2
```