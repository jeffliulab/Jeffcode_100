这道题找的是总储水量，所以只需要考虑每个i上方的储水量，并确定左侧max和右侧max就行了。

L1: leetcode hard题，求总储水量
Two pointers
```py
class Solution:
    def trap(self, height: List[int]) -> int:
        h = height
        l, r = 0, len(h)-1
        lmax = h[l]
        rmax = h[r]
        S = 0
        while(l < r):
            if lmax < rmax:
                l += 1
                lmax = max(h[l], lmax)
                S += lmax - h[l] # if same height, +0 in fact
            else: # include same condition
                r -= 1
                rmax = max(h[r], rmax)
                S += rmax - h[r]
        return S
```

L2: 在leetcode题的基础上，考虑连续存储的最大水量
如果考虑局部问题，双指针就不那么好用了，回归到单调栈解法上：
```py
def maxLocalWater(height):
    n = len(height)
    stack = []  # 存储下标，保持栈中高度单调递减
    max_water = 0
    
    for i in range(n):
        print(stack)
        while stack and height[i] >= height[stack[-1]]:
            mid = stack.pop()
            print(mid)
            if stack:  # 确保有左边界
                h = min(height[i], height[stack[-1]]) - height[mid]
                w = i - stack[-1] - 1
                max_water = max(max_water, h * w)
        stack.append(i)
    
    return max_water

x = [0,1,0,2,1,0,1,3,2,1,2,1]
print(maxLocalWater(x))
```

该单调递减栈思路：
```
对于序列 [0,1,0,2,1,0,1,3]，栈的变化过程是：

放入0: stack = [0]
来了1比0大，0出栈，放入1: stack = [1]
来了0比1小，放入0: stack = [1,0]
来了2比0大，0出栈，比1大，1出栈，放入2: stack = [2]
来了1比2小，放入1: stack = [2,1]
来了0比1小，放入0: stack = [2,1,0]
来了1比0大，0出栈...

栈中元素保持从大到小的顺序，这样当遇到一个更高的柱子时，就可以找到一个完整的储水区域：

右边界就是当前遍历到的这个高柱子
中间是刚刚被弹出的矮柱子
左边界是新的栈顶元素

这就是为什么要用单调递减栈：它能帮我们找到"凹"字形的区域，这些区域是可能储水的地方。
```