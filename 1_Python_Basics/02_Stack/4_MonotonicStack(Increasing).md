## The Problem (Largest Rectangle In Histogram)

```
You are given an array of integers heights where heights[i] represents the height of a bar. The width of each bar is 1.

Return the area of the largest rectangle that can be formed among the bars.

Note: This chart is known as a histogram.

Example 1:

Input: heights = [7,1,7,2,2,4]

Output: 8

Example 2:

Input: heights = [1,3,7]

Output: 7
```

## Solution

解题思路
```
在上道题的基础上，继续深入学习 Monotonic Stack，这次来看一个递增的情况。

在2-3中，每次遍历一个新的温度时，如果当前温度比栈顶温度更高，就说明栈顶温度的“下一个更高温度”已经找到，因此我们需要弹出栈顶，计算两者的索引差值。

在这道题中，我们需要找到每个矩形的左边界和右边界。换句话说，也可以理解为不可抵达的边柱子。
比如说，在7，1，7，2，2，4中，第一个柱子的index是0，然后他的边界显然是柱子0的左右边。
由于柱子的编号是整数，所以这个柱子的宽度也可以看作是柱子0左右两个柱子的index的差值-1，
也就是说：width(i==0) = 1 - (-1) - 1
这里之所以要减去1，是因为在计算时不包括两个边柱。
就好比问：1月1日和1月3日之间有几天（不包括两边的日子），那么答案是3-1-1=1天。

左边柱：以当前柱子为高度，矩形能向左延伸到的最远位置的不被算进来的那个矩形（最远的左侧“挡住它延伸”的柱子）
右边柱：以当前柱子为高度，矩形能向右延伸到的最远位置的不被算进来的那个矩形（最远的右侧“挡住它延伸”的柱子）
计算宽度 = 右边柱index - 左边柱index - 1
（这里假设第一个柱子左边有一个index为-1的柱子（其实就是sentinel），最右边有一个index为len(height)的柱子，这两个柱子不被计算在内）

该矩形处要计算的面积 = 计算宽度 * 该矩形的高度

所以这道题就是traverse一遍存着height的list，然后把每个矩形处对应的面积求出来。
所以关键点就是找到左边界柱子和右边界柱子。

由于这些边界的特点是:它们是第一个比当前柱子矮的柱子。
这正好符合单调栈的特性 - 它可以帮我们找到第一个比当前元素大/小的元素。
```

Monotonic Stack思路
```
这个算法的精妙之处在于：

不是在遍历到某个柱子时计算它的面积
而是在遍历到一个更矮的柱子时，回头计算之前更高柱子的面积
通过单调递增栈，我们可以确保：

栈顶元素 = 当前要计算的柱子
新的栈顶 = 左边第一个比它矮的柱子(左边界)
当前遍历位置 = 右边第一个比它矮的柱子(右边界)

这样我们就能一次遍历同时得到左右边界，高效地计算面积。

在计算面积时：

右边界由当前遍历到的位置i给出
左边界由新的栈顶给出(如果栈空则为-1)
宽度 = 右边界 - 左边界 - 1

以1、5、6、2为例
1、5、6一直在增高，所以进入stack，到2的时候，stack=[0,1,2]
然后因为2比6低，所以算6的面积=6*(3-1-1)=6
然后2还比5低，所以继续算5的面积=5*(3-0-1)=10
然后2不比1低，所以2进stack，stack现在是[0,3]
然后右边是假设的sentinel，index=4，height=0，所以比2低，
计算2的面积=2*(4-0-1)=6
接着计算1的面积=1*(4-(-1)-1)=4，这里的-1指的是1左边的sentinel（index=-1）
其中1、5、6的部分就是单调递增阶段的stack，
换句话说，
stack永远都保持着单调递增的状态
所以这个方法叫做increasing monotonic stack
```

Solution Ot(n):
```py
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxS = 0
        h = heights + [0]
        for i in range(len(h)):
            while(stack and h[i] < h[stack[-1]]):
                height = h[stack.pop()]
                left_side = stack[-1] if stack else -1
                maxS = max(maxS, (i - left_side - 1) * height)
            stack.append(i)
        return maxS
```