class ArrayBST:
    """
    用Array存储实现的二叉搜索树 BST。
    """
    def __init__(self):
        self.array = []  # 用数组存储 BST 的节点

    def insert(self, val):
        """
        插入值到顺序存储的 BST。
        :param val: 要插入的值
        """
        if not self.array:
            self.array.append(val)  # 如果数组为空，直接插入根节点
        else:
            idx = 0  # 从根节点开始
            while idx < len(self.array):
                if val < self.array[idx]:
                    # 左子节点位置
                    next_idx = 2 * idx + 1
                else:
                    # 右子节点位置
                    next_idx = 2 * idx + 2

                # 如果子节点不存在，插入值
                if next_idx >= len(self.array):
                    self.array.extend([None] * (next_idx - len(self.array) + 1))
                if self.array[next_idx] is None:
                    self.array[next_idx] = val
                    break
                idx = next_idx

    def preorder(self, idx=0):
        """
        前序遍历：根 → 左 → 右。
        :param idx: 当前节点的索引
        """
        if idx < len(self.array) and self.array[idx] is not None:
            print(self.array[idx], end=" ")
            self.preorder(2 * idx + 1)  # 遍历左子节点
            self.preorder(2 * idx + 2)  # 遍历右子节点

    def inorder(self, idx=0):
        """
        中序遍历：左 → 根 → 右。
        :param idx: 当前节点的索引
        """
        if idx < len(self.array) and self.array[idx] is not None:
            self.inorder(2 * idx + 1)  # 遍历左子节点
            print(self.array[idx], end=" ")
            self.inorder(2 * idx + 2)  # 遍历右子节点

    def postorder(self, idx=0):
        """
        后序遍历：左 → 右 → 根。
        :param idx: 当前节点的索引
        """
        if idx < len(self.array) and self.array[idx] is not None:
            self.postorder(2 * idx + 1)  # 遍历左子节点
            self.postorder(2 * idx + 2)  # 遍历右子节点
            print(self.array[idx], end=" ")




# 示例：Array存储的 BST
array_bst = ArrayBST()
for v in values:
    array_bst.insert(v)

print("\n顺序存储 BST 的遍历结果:")
print("前序遍历:", end=" ")
array_bst.preorder()  # 输出：10 5 3 7 15 12 18
print("\n中序遍历:", end=" ")
array_bst.inorder()   # 输出：3 5 7 10 12 15 18
print("\n后序遍历:", end=" ")
array_bst.postorder() # 输出：3 7 5 12 18 15 10
