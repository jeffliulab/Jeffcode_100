在 Python 中，元组 (tuple) 是一种数据结构，用来存储多个值。元组是不可变的，一旦创建，元组中的值就不能更改。
```python
import heapq  # Import heapq module to use heap functionalities

# 1. Creating Tuples 
# 元组用圆括号 () 表示，多个值用逗号 , 分隔。
# 元素可以是任何类型（数字、字符串、列表、字典等）
t = (1, 2, 3)           # Can assign integers
t = ("a", "b", "c")      # Can assign strings
t = (1, "hello", [3, 4]) # Can assign mixed data types
t = ()                   # Empty tuple
t = (5,)                 # Single-element tuple, note the trailing comma

# unpack tuple的一般方法：
t = (1, x, y)
a, b, c = t

# 2. Accessing Tuple Elements
# 元组是有序的，可以通过索引访问元素
t = (10, 20, 30, 40)
print(t[0])    # Access first element, output: 10
print(t[-1])   # Access last element, output: 40
print(t[1:3])  # Slice tuple, output: (20, 30)

# 3. Tuples are Immutable
# 元组不可变，不能修改元素
t = (1, 2, 3)
# t[0] = 10  # Uncommenting this will raise TypeError

# 4. Tuple Operations
t1 = (1, 2, 3)
t2 = (4, 5)
print(t1 + t2)     # Concatenation, output: (1, 2, 3, 4, 5)
print(t1 * 3)      # Repetition, output: (1, 2, 3, 1, 2, 3, 1, 2, 3)
print(2 in t1)     # Membership check, output: True
print(5 in t1)     # Membership check, output: False

# 5. Tuple Functions
t = (10, 20, 30, 40, 50)
print(len(t))         # Length of tuple, output: 5
print(max(t))         # Maximum value, output: 50
print(min(t))         # Minimum value, output: 10
print(t.index(30))    # Index of 30, output: 2
print(t.count(20))    # Count occurrences of 20, output: 1

# 6. Packing and Unpacking
packed_tuple = 1, 2, 3  # Packing a tuple (parentheses are optional)
a, b, c = packed_tuple  # Unpacking tuple values
print(a, b, c)          # Output: 1 2 3

# 7. Nested Tuples
nested_t = ((1, 2), (3, 4), (5, 6))  # Tuple of tuples
print(nested_t[1])       # Access inner tuple, output: (3, 4)
print(nested_t[1][0])    # Access element of inner tuple, output: 3

# 8. Tuples as Dictionary Keys
dict_with_tuple_keys = {
    (1, 2): "Point A",
    (3, 4): "Point B"
}
print(dict_with_tuple_keys[(1, 2)])  # Access value by tuple key, output: "Point A"
```

Python 的 heapq 模块可以存储 tuple 元组，并且会按照元组的第一个元素进行排序。
```
为什么元组可以用于堆？
堆是一种特殊的数据结构，heapq 是 Python 的堆实现，基于二叉堆。在存储元组时：

堆默认使用元组的第一个元素作为优先级进行比较。
如果第一个元素相同，则比较第二个元素，依次类推。
```

for example:
```python
import heapq  # Import heapq module to use heap functionalities

# Create a list to serve as the min-heap
heap = []

# Add tuples (distance, point) to the heap
# Each tuple contains:
# - distance: a number representing some value (e.g., distance from the origin)
# - point: the coordinates of the point in 2D space
heapq.heappush(heap, (5, [2, 3]))  # Add a point with distance 5
heapq.heappush(heap, (2, [1, 2]))  # Add a point with distance 2
heapq.heappush(heap, (8, [4, 6]))  # Add a point with distance 8
heapq.heappush(heap, (2, [0, 1]))  # Add another point with distance 2

# The heap automatically sorts based on the first element of the tuple (distance)
print(heap)
# Output: [(2, [0, 1]), (2, [1, 2]), (8, [4, 6]), (5, [2, 3])]

# Pop the smallest element (root of the heap)
smallest = heapq.heappop(heap)
print(smallest)  # Output: (2, [0, 1])

# Example of finding k closest points
# List of points in 2D space
points = [[1, 3], [-2, 2], [5, 8], [0, 1]]

# Create a heap to store tuples (distance, point)
heap = []

# Iterate through each point
for x, y in points:
    # Calculate the squared Euclidean distance from the origin (0, 0)
    # Avoid computing square root for efficiency; the squared distance is sufficient for comparison
    distance = x**2 + y**2
    # Push the tuple (distance, point) into the heap
    heapq.heappush(heap, (distance, [x, y]))

# Extract the k closest points from the heap
k = 2
closest_points = [heapq.heappop(heap)[1] for _ in range(k)]
print(closest_points)
# Output: [[-2, 2], [0, 1]]

```