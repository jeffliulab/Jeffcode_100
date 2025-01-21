class TreeNode:
    def __init__(self, value=0):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    # 插入操作
    def insert(self, value):
        if not self.root:  # 如果树为空，设置根节点
            self.root = TreeNode(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        if value < node.value:  # 插入左子树
            if not node.left:
                node.left = TreeNode(value)
            else:
                self._insert_recursive(node.left, value)
        elif value > node.value:  # 插入右子树
            if not node.right:
                node.right = TreeNode(value)
            else:
                self._insert_recursive(node.right, value)

    # 查找操作
    def search(self, value):
        return self._search_recursive(self.root, value)

    def _search_recursive(self, node, value):
        if not node:  # 节点为空，未找到
            return False
        if value == node.value:  # 找到目标值
            return True
        elif value < node.value:  # 在左子树查找
            return self._search_recursive(node.left, value)
        else:  # 在右子树查找
            return self._search_recursive(node.right, value)

    # 删除操作
    def delete(self, value):
        self.root = self._delete_recursive(self.root, value)

    def _delete_recursive(self, node, value):
        if not node:
            return None
        if value < node.value:  # 在左子树中删除
            node.left = self._delete_recursive(node.left, value)
        elif value > node.value:  # 在右子树中删除
            node.right = self._delete_recursive(node.right, value)
        else:  # 找到节点
            if not node.left:  # 无左子树
                return node.right
            if not node.right:  # 无右子树
                return node.left
            # 有两个子节点，找到右子树最小值替代
            min_larger_node = self._find_min(node.right)
            node.value = min_larger_node.value
            node.right = self._delete_recursive(node.right, min_larger_node.value)
        return node

    def _find_min(self, node):
        while node.left:
            node = node.left
        return node

    # 中序遍历（升序排列）
    def inorder_traversal(self, node):
        if node:
            self.inorder_traversal(node.left)
            print(node.value, end=" ")
            self.inorder_traversal(node.right)

# 测试代码
if __name__ == "__main__":
    bst = BinarySearchTree()

    # 插入节点
    bst.insert(8)
    bst.insert(3)
    bst.insert(10)
    bst.insert(1)
    bst.insert(6)
    bst.insert(4)
    bst.insert(7)
    bst.insert(14)
    bst.insert(13)

    # 查找节点
    print("Search 6:", bst.search(6))  # 输出: True
    print("Search 15:", bst.search(15))  # 输出: False

    # 中序遍历
    print("Inorder Traversal:", end=" ")
    bst.inorder_traversal(bst.root)  # 输出: 1 3 4 6 7 8 10 13 14

    # 删除节点
    bst.delete(10)
    print("\nInorder Traversal after deleting 10:", end=" ")
    bst.inorder_traversal(bst.root)  # 输出: 1 3 4 6 7 8 13 14
