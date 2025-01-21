class TreeSet:
    def __init__(self):
        self.elements = []  # 使用列表存储元素

    # 添加元素
    def add(self, value):
        if value not in self.elements:  # 确保唯一性
            self.elements.append(value)
            self.elements.sort()  # 保持有序

    # 删除元素
    def remove(self, value):
        if value in self.elements:
            self.elements.remove(value)

    # 检查元素是否存在
    def contains(self, value):
        return value in self.elements

    # 打印 TreeSet 的内容
    def print(self):
        print(self.elements)

if __name__ == "__main__":
    # 创建一个 TreeSet
    tree_set = TreeSet()

    # 添加元素
    tree_set.add("Alice")
    tree_set.add("Brad")
    tree_set.add("Collin")

    # 打印 TreeSet 的内容
    print("Initial TreeSet:", end=" ")
    tree_set.print()  # 输出: ['Alice', 'Brad', 'Collin']

    # 检查元素是否存在
    print("Is 'Alice' in TreeSet?", tree_set.contains("Alice"))  # 输出: True
    print("Is 'David' in TreeSet?", tree_set.contains("David"))  # 输出: False

    # 删除元素
    tree_set.remove("Brad")

    # 打印 TreeSet 的内容
    print("TreeSet after removing 'Brad':", end=" ")
    tree_set.print()  # 输出: ['Alice', 'Collin']
