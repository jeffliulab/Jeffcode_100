
## Queue

在Python中Queue的所有功能都能在Deque中实现，可以先学习Deque的使用方法。

## Deque

```py
from collections import deque

def demonstrate_deque_usage():
    print("\n=== 1. 初始化队列 ===")
    q = deque()  # 空队列
    print("空队列:", q)

    q = deque([1, 2, 3])  # 带初始值的队列
    print("初始化带元素的队列:", q)

    print("\n=== 2. 基本操作 ===")
    # 添加元素
    q.append(4)  # 右侧添加
    print("右侧添加 4:", q)

    q.appendleft(0)  # 左侧添加
    print("左侧添加 0:", q)

    # 删除元素
    q.pop()  # 右侧删除
    print("右侧删除:", q)

    q.popleft()  # 左侧删除
    print("左侧删除:", q)

    print("\n=== 3. 查看队列 ===")
    print("队列第一个元素:", q[0])
    print("队列最后一个元素:", q[-1])
    print("队列长度:", len(q))

    print("\n=== 4. 清空队列 ===")
    q.clear()
    print("清空后的队列:", q)

    print("\n=== 5. 队列旋转 ===")
    q = deque([1, 2, 3, 4])
    print("原始队列:", q)

    q.rotate(1)  # 向右旋转 1 步
    print("右旋转 1 步:", q)

    q.rotate(-2)  # 向左旋转 2 步
    print("左旋转 2 步:", q)

    print("\n=== 6. 最大长度 ===")
    q = deque(maxlen=3)  # 最大长度为 3
    q.append(1)
    q.append(2)
    q.append(3)
    print("初始化最大长度为 3 的队列:", q)

    q.append(4)  # 超过长度，最左侧元素被挤出
    print("添加 4 后:", q)

    print("\n=== 7. 队列实现队列 (FIFO) ===")
    q = deque()
    q.append(1)
    q.append(2)
    q.append(3)
    print("队列状态:", q)
    print("出队:", q.popleft())
    print("队列状态:", q)

    print("\n=== 8. 队列实现栈 (LIFO) ===")
    stack = deque()
    stack.append(1)
    stack.append(2)
    stack.append(3)
    print("栈状态:", stack)
    print("出栈:", stack.pop())
    print("栈状态:", stack)

    print("\n=== 9. 滑动窗口最大值示例 ===")
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3
    q = deque()
    result = []

    for i in range(len(nums)):
        # 移除超出窗口范围的元素
        if q and q[0] < i - k + 1:
            q.popleft()

        # 移除队列中比当前元素小的所有元素
        while q and nums[q[-1]] < nums[i]:
            q.pop()

        # 添加当前索引
        q.append(i)

        # 如果窗口大小达到 k，记录最大值
        if i >= k - 1:
            result.append(nums[q[0]])

    print("滑动窗口最大值结果:", result)

if __name__ == "__main__":
    demonstrate_deque_usage()

```