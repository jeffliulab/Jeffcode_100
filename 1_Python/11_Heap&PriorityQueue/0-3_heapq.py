import heapq

#############################################
# Basic heapq operations (Default: Min-Heap)

# Build a Min-Heap
nums = [3, 1, 2]
heapq.heapify(nums)  # Convert the list into a Min-Heap
print("Min-Heap:", nums)

# Push an element into the heap
heapq.heappush(nums, 0)  # Add 0 to the heap
print("Heap after pushing 0:", nums)

# Pop the smallest element
smallest = heapq.heappop(nums)  # Remove and return the smallest element
print("Popped smallest element:", smallest)
print("Heap after popping:", nums)

# Push and pop an element in one operation
result = heapq.heappushpop(nums, -1)  # Push -1 and then pop the smallest element
print("Pushed -1 and popped:", result)
print("Heap after pushpop:", nums)

# Replace the smallest element
result = heapq.heapreplace(nums, 4)  # Pop the smallest and push 4
print("Replaced and popped:", result)
print("Heap after replacement:", nums)

# Get the largest n elements from the heap
largest = heapq.nlargest(3, nums)  # Get the 3 largest elements
print("3 largest elements:", largest)

# Get the smallest n elements from the heap
smallest = heapq.nsmallest(3, nums)  # Get the 3 smallest elements
print("3 smallest elements:", smallest)

#######################################
# Merge multiple heaps

# 假设有三个已 heapify 的堆
heap1 = [1, 3, 5]
heap2 = [2, 4, 6]
heap3 = [0, 7, 8]

# 使用 heapq.merge 合并多个堆，return一个有序迭代器（iterator）
merged_iter = heapq.merge(heap1, heap2, heap3)

# 将结果转为列表并重新 heapify
new_heap = list(merged_iter)
heapq.heapify(new_heap)

# 打印新的堆
print(new_heap)  # 输出: [0, 1, 5, 3, 4, 6, 8, 7, 2]



#######################################
# Max-Heap implementation using negation

# Create a Max-Heap by negating elements
max_heap = []
heapq.heappush(max_heap, -3)  # Push -3
heapq.heappush(max_heap, -1)  # Push -1
heapq.heappush(max_heap, -2)  # Push -2
print("Max-Heap (stored as negatives):", max_heap)
print("Popped max value:", -heapq.heappop(max_heap))  # Pop the maximum value (invert sign)

# Use case 1: Priority Queue
tasks = [(3, "low priority"), (1, "high priority"), (2, "medium priority")]
heapq.heapify(tasks)  # Create a Min-Heap based on priority
while tasks:
    priority, task = heapq.heappop(tasks)  # Process tasks based on priority
    print(f"Processing task: {task} with priority {priority}")

# Use case 2: Maintain the kth largest element in a stream
k = 3
nums = [3, 2, 1, 5, 6, 4]
min_heap = []
for num in nums:
    heapq.heappush(min_heap, num)  # Push the number into the heap
    if len(min_heap) > k:
        heapq.heappop(min_heap)  # Remove the smallest element if the heap size exceeds k
print(f"The {k}rd largest element is:", min_heap[0])  # The smallest element in the heap is the kth largest
