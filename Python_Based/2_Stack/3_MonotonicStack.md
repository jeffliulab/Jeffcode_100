## The Problem

Output how many days until the next higher temperature day:
```
Input: temperatures = [30,38,30,36,35,40,28]

Output: [1,4,1,2,1,0,0]

Input: temperatures = [22,21,20]

Output: [0,0,0]
```

Solution Ot(n^2):
```python
# 直观思路
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ls = temperatures
        output = []
        if not temperatures:
            return output
        while len(ls) > 1:
            today = ls[0]
            i = 1
            while(ls[i] <= today and i < len(ls) - 1):
                i += 1
            if ls[i] > today:
                output.append(i)
            else:
                output.append(0)
            ls = ls[1:]
        output.append(0)
        return output
```

However, this method has high Ot and needs to be optimized.

## Monotonic Stack (单调递减栈)

解决思路
```
重新看这个问题：你想知道每一天需要等多少天才能遇到比当天温度更高的温度。如果未来没有更高温度，就返回 0。

例如： 输入 [73, 74, 75, 71, 69, 72, 76, 73]，我们希望输出： [1, 1, 4, 2, 1, 1, 0, 0]

单调栈的核心思想：

栈中存放的是索引，栈内的温度对应索引保持 递减顺序。
每次遍历新的温度时：
如果发现当前温度比栈顶索引对应的温度高，那么栈顶索引的答案可以确定。
弹出栈顶，计算两个索引的差值（天数差），更新答案数组。
主要步骤：

遍历 temperatures，用 i 表示当前天的索引。
当栈非空且当前温度比栈顶温度高时：
弹出栈顶索引 prev_index，说明当前温度是 prev_index 对应的“下一个更高温度”。
更新答案：output[prev_index] = i - prev_index。
将当前天的索引 i 压入栈，表示“还没找到答案”。
结果：

遍历结束后，栈中剩下的索引表示这些天没有找到更高温度，因此答案保持为 0。
```

Solution Ot(n):
```python
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ls = temperatures
        output = [0 for i in range(len(ls))]
        stack = []
        if not ls:
            return output
        for i in range(len(ls)):
            if not stack:
                stack.append(i)
            else:
                # compare num and top temp
                # if num is larger, pop the top, update output
                while stack and ls[i] > ls[stack[-1]]:
                    output[stack[-1]] = i - stack[-1]
                    stack.pop()
                stack.append(i)
        return output

```