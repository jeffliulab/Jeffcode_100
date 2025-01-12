这个和FindSum没什么区别，关键点就是找到l和r的移动逻辑。

只要能保证l和r移动更小的那一个，就可以保持更大的面积，从而保证不会遗漏更大的解。

```py
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        if not heights:
            return 0
        maxS = 0
        l = 0
        r = len(heights)-1
        while(l < r):
            S = min(heights[l], heights[r]) * (r - l)
            maxS = max(maxS, S)
            if heights[l] < heights[r]:
                l += 1
            elif heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
        return maxS
```