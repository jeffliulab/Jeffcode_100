# Counter Usage Guide

# Importing the Counter class
from collections import Counter

"""
最常见用法:
1. Counter(iterable)
2. counter.most_common(n)
3. counter.update()
4. counter.subtract()
"""

# ============================================
# =================全部功能=====================

# 1. Creating Counter Objects
# (1) From an iterable
example_list = ["A", "A", "B", "C", "A", "C"]
counter_from_list = Counter(example_list)
print(counter_from_list)  # Output: Counter({'A': 3, 'C': 2, 'B': 1})

# (2) From a string
example_string = "hello world"
counter_from_string = Counter(example_string)
print(counter_from_string)  # Output: Counter({'l': 3, 'o': 2, 'h': 1, 'e': 1, ' ': 1, 'w': 1, 'r': 1, 'd': 1})

# (3) From a dictionary
example_dict = {"A": 3, "B": 2, "C": 1}
counter_from_dict = Counter(example_dict)
print(counter_from_dict)  # Output: Counter({'A': 3, 'B': 2, 'C': 1})

# (4) Creating an empty Counter
empty_counter = Counter()
print(empty_counter)  # Output: Counter()

# 2. Accessing Counts
# Retrieve the count of a specific element
print(counter_from_list["A"])  # Output: 3
print(counter_from_list["D"])  # Output: 0 (returns 0 if the element is not present)

# 3. Updating Counts
# (1) Using an iterable
counter = Counter()
counter.update(["A", "B", "A"])
print(counter)  # Output: Counter({'A': 2, 'B': 1})

# (2) Using a dictionary
counter.update({"A": 1, "C": 2})
print(counter)  # Output: Counter({'A': 3, 'C': 2, 'B': 1})

# 4. Subtracting Counts
# Subtract elements using an iterable or dictionary
counter.subtract(["A", "C"])
print(counter)  # Output: Counter({'A': 2, 'B': 1, 'C': 1})

counter.subtract({"A": 1, "B": 1})
print(counter)  # Output: Counter({'A': 1, 'C': 1, 'B': 0})

# 5. Most Common Elements
# Retrieve the n most common elements
print(counter_from_list.most_common(2))  # Output: [('A', 3), ('C', 2)]

# 6. Elements Method
# Expand elements into an iterator (repeats each element based on its count)
print(list(counter_from_list.elements()))  # Output: ['A', 'A', 'A', 'B', 'C', 'C']

# 7. Mathematical Operations
counter1 = Counter(A=3, B=2, C=1)
counter2 = Counter(A=1, B=2, C=3)

# Addition
print(counter1 + counter2)  # Output: Counter({'A': 4, 'C': 4, 'B': 4})

# Subtraction
print(counter1 - counter2)  # Output: Counter({'A': 2})

# Intersection (minimum of counts)
print(counter1 & counter2)  # Output: Counter({'A': 1, 'B': 2, 'C': 1})

# Union (maximum of counts)
print(counter1 | counter2)  # Output: Counter({'A': 3, 'B': 2, 'C': 3})

# 8. Clearing a Counter
counter.clear()
print(counter)  # Output: Counter()

# 9. Removing Zero or Negative Counts
counter = Counter(A=3, B=0, C=-1)
counter += Counter()
print(counter)  # Output: Counter({'A': 3})

# 10. Combining with Other Collections
# Counter can be combined with lists, dictionaries, etc.
data = ["A", "A", "B", "C"]
counter = Counter(data)
counter.update({"D": 2})
print(counter)  # Output: Counter({'A': 2, 'D': 2, 'B': 1, 'C': 1})
