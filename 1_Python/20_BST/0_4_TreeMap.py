class TreeMap:
    def __init__(self):
        self.elements = {}  # 使用字典存储键值对

    # 添加键值对
    def put(self, key, value):
        self.elements[key] = value
        self.elements = dict(sorted(self.elements.items()))  # 保持键有序

    # 删除键值对
    def remove(self, key):
        if key in self.elements:
            del self.elements[key]

    # 获取值
    def get(self, key):
        return self.elements.get(key, None)  # 如果键不存在返回 None

    # 检查键是否存在
    def contains_key(self, key):
        return key in self.elements

    # 打印 TreeMap 的内容
    def print(self):
        print(self.elements)

if __name__ == "__main__":
    # TreeMap 示例
    tree_map = TreeMap()
    tree_map.put("Alice", 123)
    tree_map.put("Brad", 345)
    tree_map.put("Collin", 678)
    print("\nInitial TreeMap:", end=" ")
    tree_map.print()  # 输出: {'Alice': 123, 'Brad': 345, 'Collin': 678}
    print("Value for 'Alice':", tree_map.get("Alice"))  # 输出: 123
    print("Is 'David' in TreeMap?", tree_map.contains_key("David"))  # 输出: False
    tree_map.remove("Brad")
    print("TreeMap after removing 'Brad':", end=" ")
    tree_map.print()  # 输出: {'Alice': 123, 'Collin': 678}
