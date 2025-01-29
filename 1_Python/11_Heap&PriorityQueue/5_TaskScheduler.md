这道题除了用maxHeap的方法，还可以用greedy和纯math的方法解决，参见后面的greedy章节和math章节。

maxHeap, Ot(m), Os(1) since max 26 characters
```python
import heapq
from collections import Counter, deque

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        time = 0
        q = deque()

        count = Counter(tasks)
        heap = [-count for count in count.values()]
        heapq.heapify(heap)

        while q or heap:
            time += 1

            if not heap:
                time = q[0][1]
            else:
                cur_max_count = heapq.heappop(heap) + 1
                if cur_max_count != 0:
                    q.append((cur_max_count, time+n))
            
            if q and time == q[0][1]:
                heapq.heappush(heap, q.popleft()[0])

        return time
```

这道题初见较难，因此做了一个详细的说明：
```python
from collections import Counter, deque
import heapq

class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        """
        这段代码的目的是将任务的出现频率转化为一个最大堆
        以便我们能够优先处理频率最高的任务。
        从频率最高的任务开始安排，尽量减少空闲时间 idle。
        """
        # 统计每个任务的频率
        count = Counter(tasks)
        # 构建最大堆：存储负的频率值，以便通过 Python 的最小堆实现最大堆效果
        heap = [-count for count in count.values()]
        heapq.heapify(heap)

        # 模拟任务调度过程 的核心逻辑，通过 time 变量模拟 CPU 的时钟
        # 结合最大堆 maxHeap 和 队列 q 确保任务按照冷却时间 n 的约束被正确安排执行。
        time = 0  # time 要一直增加，模拟 CPU 时钟
        q = deque()  # pairs of [-count, idleTime]，用来暂存冷却中的任务

        while heap or q:  # 循环条件：只要堆里有任务（heap）或冷却队列中有任务（q），就继续执行
            time += 1  # 每次循环，time +1，模拟 CPU 时钟的推进

            # 如果堆为空，但冷却队列 q 中还有任务
            if not heap:
                # 优化：直接跳到冷却队列中第一个任务的冷却结束时间，避免无意义的逐步等待
                # 注意：这里假设 q 按冷却结束时间排序（FIFO 保证），所以直接跳到 q[0][1]
                time = q[0][1]

            else:
                # 从堆中弹出一个任务（频率最高的任务）
                cnt = 1 + heapq.heappop(heap)  # 执行一次任务，频率 -1
                if cnt:  # 如果任务还有剩余频率（cnt != 0）
                    # 将任务加入冷却队列，记录其冷却结束时间 time + n
                    q.append([cnt, time + n])

            # 检查冷却队列中的任务是否完成冷却
            if q and q[0][1] == time:  # 如果当前时间达到冷却结束时间
                # 将冷却完成的任务重新加入堆
                heapq.heappush(heap, q.popleft()[0])

        return time  # 返回完成所有任务所需的总时间

        """
        关键补充：
        1. 冷却队列的顺序是否有保证？
           - 冷却时间总是按 `time + n` 计算，任务调度顺序由堆决定，
             因此冷却结束时间在队列中是递增的。
           - 如果冷却结束时间可以不同，则需要用优先队列来管理冷却任务，
             而不能使用 deque。

        2. 为什么需要直接跳到冷却结束时间？
           - 如果堆为空，只能等待冷却任务完成。
           - 为了减少无意义的空闲时间推进，可以直接跳到下一个冷却任务的结束时间。

        3. Python 中 cnt == 0 会被视为 False。
           - 在任务频率减到 0 时，表示任务已经完全执行完，
             不需要再加入冷却队列。

        4. deque 是否总是适用？
           - 当前逻辑下，冷却时间总是递增，因此 deque 保证 FIFO。
           - 如果冷却时间不一致（例如任务有动态冷却时间），则需要改用优先队列。
        """
```