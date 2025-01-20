这道题是一个二分搜索的经典应用，核心在于找出吃香蕉的最小速度k，以保证所有香蕉在 h 小时内吃完。

题目要求:
* 你可以每小时选择一个香蕉堆吃，但每小时最多吃 k 根。
* 如果当前香蕉堆的香蕉少于 k，你只能把该堆吃完，不能去其他堆继续吃。
* 目标是找出最小的吃香蕉速度 k，使得你在 h 小时内吃完所有香蕉。

问题的本质:
* 我们需要解决的问题是：给定 k，判断在 h 小时内是否能吃完所有香蕉。

⚠️注意：本题的关键点：
* 只需要关注l，l代表的是最小的时间
* ceil用法

```py
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # h: max hour
        l = 1
        r = max(piles)
        while l <= r:
            mid_speed = (l + r) // 2
            hour_spent = sum ( (pile + mid_speed - 1) // mid_speed for pile in piles)
            if hour_spent > h: # 如果当前中点值 mid 不满足条件，我们增加左边界 l = mid + 1。
                l = mid_speed + 1
            else: # 如果当前中点值 mid 满足条件，我们缩小右边界 r = mid - 1。
                r = mid_speed - 1
            # 该逻辑保证了：
            # 左边界 l 始终指向可能满足条件的最小值。
            # 右边界 r 始终指向不满足条件的最大值。
        
        """
        当循环结束时，l > r：
            l 是第一个满足条件的位置。
            r 是最后一个不满足条件的位置。
        因此，l 代表满足条件的最小值。
        """
        return l
```