## list (dynamic array)
```python
list_x = []

list_x = [1, 2, 3, 4, 5]

list_x = [x**2 for x in range(5)]

list_x.append(element)

list_x[::-1] # 反转, return a copy, so needs assignment

if element in list_x: # O(n)
    continue

for i, n in enumerate(list_x):
    print(f"index: {i}, value: {n}")

if not list_x:
    print("list has no element")

list_x.sort() # 数组排序（升序）
list_x.sort(reverse=True) # 降序排序
```

## dict (Hash Map, key-value pairs)
```python
dict_x = {}

dict_x = {"a": 1, "b": 2, "c": 3}

dict_x = dict(a=1, b=2, c=3)  # 注意键名不能有特殊字符

dict_x = {x: x**2 for x in range(5)}  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

dict_x[element] # return the value of element

dict_x.get(element, 0) # Default is None, if only use dict_x.get(char)

dict_x[element] = value # dict cannot use append or add

dict_x[element] = dict_x.get(element, 0) + 1 # a very common usage

# find key
for key in dict_x: 
    print(f"key: {key}")

# find value
for value in dict_x.values(): 
    print(f"value: {value}")

for key, value in dict_x.items():
    print(f"key: {key}, value: {value}")

list(dict_x.values) # 将dict的values组合成一个list（无顺序）

list(dict_x.items()) # 将dict的key-value pairs组合成一个list
```

## set (Hash Set - hash table based, unique elements)
```python
set_x = set()

set_x = {1, 2, 3, 4, 5}

set_x = set([1, 2, 3, 4, 5])  # 将列表或其他可迭代对象转换为集合

set_x = {x**2 for x in range(5)}  # {0, 1, 4, 9, 16}

set_x.add(element)

if element in set_x: # O(1)
    continue

for item in set_x:
    print(f"element: {item}")
```

## sorted()
```python
string = "eat"
result = sorted(string)
print(result)  # output: ['a', 'e', 't']

# sorted(iterable, *, key=None, reverse=False) False是升序
dict_nums = {'a': 3, 'b': 1, 'c': 2}
items = list(dict_nums.items()) # 将字典转换为键值对列表
sorted_items = sorted(items, key=lambda x: x[1], reverse=True) # 按值排序
print("按值排序后的列表：", sorted_items)
```

## .join
```python
words = ['hello', 'world', 'python']
result = ' '.join(words)  # 用空格作为分隔符
print(result)  # 输出: 'hello world python'

words = ['apple', 'banana', 'cherry']
result = ', '.join(words)  # 用逗号+空格作为分隔符
print(result)  # 输出: 'apple, banana, cherry'

## .join高级用法

''.join(f"some string with {s}" for s in strs)
s = ['3', '#25', 'kk'] # .join的高级用法
string = ''.join(f"#{len(s)}#{s.replace('#', '##')}" for s in strs)
```

## list comprehension 
## 列表推导式: 从一个可迭代对象中提取数据并生成新的列表
```python
[expression for variable in iterable if condition]

list_freq = [(1, 3), (2, 2), (3, 1)]
result = [item[0] for item in list_freq[:2]] # 提取出list_freq中的前两个元素
```

## string
```python
list_s = string.split(',') #把string按照逗号分割并保存为list
```

## CAST
```python
# 1. 转换为整数 (int)
num = 3.5
result = int(num)  # 结果: 3

# 2. 转换为浮点数 (float)
num = "3"
result = float(num)  # 结果: 3.0

# 3. 转换为字符串 (str)
num = 42
result = str(num)  # 结果: "42"

# 4. 转换为布尔值 (bool)
num = 0
result = bool(num)  # 结果: False

# 5. 转换为列表 (list)
data = (1, 2, 3)
result = list(data)  # 结果: [1, 2, 3]

# 6. 转换为元组 (tuple)
data = [1, 2, 3]
result = tuple(data)  # 结果: (1, 2, 3)

# 7. 转换为集合 (set)
data = [1, 2, 2, 3]
result = set(data)  # 结果: {1, 2, 3}

# 8. 转换为二进制、八进制、十六进制字符串
num = 10
binary = bin(num)    # 二进制: '0b1010'
octal = oct(num)     # 八进制: '0o12'
hexadecimal = hex(num)  # 十六进制: '0xa'

# 9. 隐式转换 (自动完成)
result = 3 + 2.5  # 自动将整数 3 转为浮点数，结果: 5.5
```

## PREFIX PRODUCT and SUFFIX PRODUCT

参见1-6

```