"""
完全二叉树 Complete Binary Tree  通常使用 list/array 形式来存储。
因为完全二叉树有特殊的结构特性，可以用连续的数组高效地表示其节点位置，而不需要显式地使用指针链接节点。
"""

class CompleteBinaryTree:
    def __init__(self):
        """
        使用一个列表存储完全二叉树的节点。
        注意：第 0 位保留空，不使用，方便计算父子节点索引。
        """
        self.tree = [None]  # 第 0 位留空

    def insert(self, value):
        """
        在完全二叉树中插入一个新值。
        :param value: 要插入的值
        """
        self.tree.append(value)  # 新值总是插入到数组的末尾

    def __str__(self):
        """
        返回当前完全二叉树的层序遍历字符串。
        """
        return " -> ".join(map(str, self.tree[1:]))  # 忽略第 0 位

    def get_parent(self, index):
        """
        获取指定索引节点的父节点。
        :param index: 当前节点的索引
        :return: 父节点的值（如果存在），否则返回 None
        """
        if index <= 1 or index >= len(self.tree):
            return None  # 根节点或无效索引没有父节点
        parent_index = index // 2
        return self.tree[parent_index]

    def get_children(self, index):
        """
        获取指定索引节点的左右子节点。
        :param index: 当前节点的索引
        :return: 左右子节点的值（如果存在），否则返回 None
        """
        if index <= 0 or index >= len(self.tree):
            return None, None
        
        left_index = index * 2
        right_index = index * 2 + 1
        
        left = self.tree[left_index] if left_index < len(self.tree) else None
        right = self.tree[right_index] if right_index < len(self.tree) else None
        
        return left, right

    def print_tree(self):
        """
        按层次结构打印出树的形状。
        """
        if len(self.tree) <= 1:
            print("树为空")
            return

        level = 0  # 当前层级
        next_level = 1  # 下一层的节点数量
        for i in range(1, len(self.tree)):
            print(self.tree[i], end=" ")
            if i == next_level:
                print()  # 换行
                level += 1
                next_level = next_level + 2 ** level
        print()

# 测试代码
if __name__ == "__main__":
    cbt = CompleteBinaryTree()
    
    # 插入节点
    for value in [10, 20, 30, 40, 50, 60, 70]:
        cbt.insert(value)

    print("层序遍历:")
    print(cbt)

    print("按层次打印树:")
    cbt.print_tree()

    # 测试父节点和子节点
    index = 3  # 节点 30 的索引
    print(f"节点 {cbt.tree[index]} 的父节点是: {cbt.get_parent(index)}")
    print(f"节点 {cbt.tree[index]} 的左右子节点是: {cbt.get_children(index)}")
