class TreeNode:
    """
    节点类: 表示二叉搜索树 BST 中的一个节点。
    """
    def __init__(self, val=0):
        self.val = val  # 节点值
        self.left = None  # 左子节点
        self.right = None  # 右子节点


class BST:
    """
    二叉搜索树BST类: 实现插入、搜索以及三种遍历方式。
    """
    def __init__(self):
        self.root = None

    def insert(self, root, val):
        """
        插入节点。
        :param root: 当前子树的根节点
        :param val: 要插入的值
        :return: 更新后的根节点
        """
        if root is None:
            return TreeNode(val)  # 找到插入位置，返回新节点

        if val < root.val:
            root.left = self.insert(root.left, val)  # 插入左子树
        elif val > root.val:
            root.right = self.insert(root.right, val)  # 插入右子树

        return root

    def search(self, root, val):
        """
        搜索节点。
        :param root: 当前子树的根节点
        :param val: 要查找的值
        :return: 如果找到返回 True，否则返回 False
        """
        if root is None:
            return False  # 到达叶节点，未找到
        if root.val == val:
            return True  # 找到目标
        elif val < root.val:
            return self.search(root.left, val)  # 搜索左子树
        else:
            return self.search(root.right, val)  # 搜索右子树

    def preorder(self, root):
        """
        前序遍历：根 → 左 → 右。
        :param root: 当前子树的根节点
        """
        if root is not None:
            print(root.val, end=" ")  # 访问根节点
            self.preorder(root.left)  # 遍历左子树
            self.preorder(root.right)  # 遍历右子树

    def inorder(self, root):
        """
        中序遍历：左 → 根 → 右。
        :param root: 当前子树的根节点
        """
        if root is not None:
            self.inorder(root.left)  # 遍历左子树
            print(root.val, end=" ")  # 访问根节点
            self.inorder(root.right)  # 遍历右子树

    def postorder(self, root):
        """
        后序遍历：左 → 右 → 根。
        :param root: 当前子树的根节点
        """
        if root is not None:
            self.postorder(root.left)  # 遍历左子树
            self.postorder(root.right)  # 遍历右子树
            print(root.val, end=" ")  # 访问根节点

# 示例：链式存储的 BST
bst = BST()
root = None
values = [10, 5, 15, 3, 7, 12, 18]
for v in values:
    root = bst.insert(root, v)

print("链式存储 BST 的遍历结果:")
print("前序遍历:", end=" ")
bst.preorder(root)  # 输出：10 5 3 7 15 12 18
print("\n中序遍历:", end=" ")
bst.inorder(root)   # 输出：3 5 7 10 12 15 18
print("\n后序遍历:", end=" ")
bst.postorder(root) # 输出：3 7 5 12 18 15 10
















