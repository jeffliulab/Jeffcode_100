
## set (Hash Set - hash table based, unique elements)
```python
set_x = set()

set_x = {1, 2, 3, 4, 5}

set_x.clear() # delete all elements but keep the set

len(set_x)

set_x = set([1, 2, 3, 4, 5])  # 将列表或其他可迭代对象转换为集合

set_x = {x**2 for x in range(5)}  # {0, 1, 4, 9, 16}

set_x.add(element)

if element in set_x: # O(1)
    continue

for item in set_x:
    print(f"element: {item}")


x = set()
x.remove(1) # 如果要删除的元素不存在，会抛出 KeyError。
x.discard(5)  # 安全，不抛出异常
x.pop() # 使用 pop() 随机删除并返回一个元素。如果集合为空，会抛出 KeyError。

x.clear() # 清空集合
```


集合运算
```python
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(set1 | set2)  # {1, 2, 3, 4, 5}  并集
print(set1 & set2)  # {3}             交集
print(set1 - set2)  # {1, 2}          差集
print(set1 ^ set2)  # {1, 2, 4, 5}    对称差集
```


