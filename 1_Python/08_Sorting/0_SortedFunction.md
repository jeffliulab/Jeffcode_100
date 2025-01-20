sorted(iterable, key, reverse)

注意事项:
* sorted() 不会改变原始数据，而是返回一个新列表。
* key 函数的返回值必须是可比较的，比如数字、字符串等。
* 如果排序依据有多个层次，可以在 key 中使用元组。

其他用法：
```python
# 按元组的第二个元素排序
pairs = [(1, 3), (2, 2), (3, 1)]
sorted(pairs, key=lambda x: x[1])
# [(3, 1), (2, 2), (1, 3)]
```