假如有list1和list2两个list，如何在不合并两个list的情况下快速找到中点。

这道题可以用第k小法解，但第k小的Ot(log(m+n))，这道题还有一个更优的解Ot(log(min(m,n)))

```python
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # 确保 nums1 是较短的数组，优化效率
        A, B = nums1, nums2
        if len(A) > len(B):
            A, B = B, A
        
        total = len(A) + len(B)  # 总长度
        half = total // 2  # 分割点
        
        # 二分查找初始化
        l, r = 0, len(A) - 1
        while True:
            # 当前 A 的分割点
            i = (l + r) // 2
            # B 的分割点通过总长度计算
            j = half - i - 2

            # 获取 A 和 B 分割点两侧的值，越界时用正负无穷
            Aleft = A[i] if i >= 0 else float("-infinity")
            Aright = A[i + 1] if (i + 1) < len(A) else float("infinity")
            Bleft = B[j] if j >= 0 else float("-infinity")
            Bright = B[j + 1] if (j + 1) < len(B) else float("infinity")

            # 检查是否找到合适的分割点
            if Aleft <= Bright and Bleft <= Aright:
                # 如果总长度是奇数，中位数是右半部分的最小值
                if total % 2:
                    return min(Aright, Bright)
                # 如果总长度是偶数，中位数是左侧最大值和右侧最小值的平均值
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            elif Aleft > Bright:
                # 分割点太靠右，向左移动
                r = i - 1
            else:
                # 分割点太靠左，向右移动
                l = i + 1
```