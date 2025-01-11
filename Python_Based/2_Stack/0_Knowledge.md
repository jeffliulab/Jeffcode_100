## stack
```python
栈 是一种 后进先出（LIFO, Last In First Out） 的数据结构。
想象一个叠盘子的场景：

你总是从顶部放盘子（入栈）。
你总是从顶部拿盘子（出栈）。
在计算机中，栈是一种用于临时存储数据的结构，典型的特点是只能从栈的“顶端”进行操作（比如添加或移除元素）。

栈的基本操作：
Push（入栈）: 把一个元素压入栈顶。
Pop（出栈）: 从栈顶取出一个元素。
Peek（查看栈顶）: 查看栈顶的元素，但不移除它。
isEmpty（判断栈是否为空）: 检查栈中是否还有元素。
```
## stack in python
```python
stack = []  # 用列表实现栈

# 1. 入栈（Push）
stack.append(1)  # 栈顶放入 1
stack.append(2)  # 栈顶放入 2
stack.append(3)  # 栈顶放入 3
print(stack)     # 输出 [1, 2, 3]

# 2. 出栈（Pop）
top = stack.pop()  # 移除栈顶元素 3
print(top)         # 输出 3
print(stack)       # 输出 [1, 2]

# 3. 查看栈顶元素（Peek）
print(stack[-1])   # 输出 2 （栈顶元素）

# 4. 判断栈是否为空
print(len(stack) == 0)  # False，栈非空
```