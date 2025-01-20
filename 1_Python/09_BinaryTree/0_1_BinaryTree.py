# 定义二叉树节点类
class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

# 主类，包含创建树、添加节点、计算高度和深度，以及遍历的方法
class BinaryTree:
    def __init__(self):
        self.root = None  # 初始化树根节点为空

    # 添加节点（递归添加到第一个可用位置）
    def add(self, value):
        if not self.root:  # 如果树为空，创建根节点
            self.root = TreeNode(value)
        else:
            self._add_recursive(self.root, value)

    def _add_recursive(self, node, value):
        if not node.left:  # 如果左子节点为空，添加到左子节点
            node.left = TreeNode(value)
        elif not node.right:  # 如果右子节点为空，添加到右子节点
            node.right = TreeNode(value)
        else:  # 如果左右子节点均不为空，递归添加到左子树
            self._add_recursive(node.left, value)

    # 计算树的高度
    def height(self, node):
        if not node:  # 空节点高度为 -1（可以改为 0）
            return -1
        left_height = self.height(node.left)
        right_height = self.height(node.right)
        return max(left_height, right_height) + 1

    # 计算节点深度
    def depth(self, node, target, current_depth=0):
        if not node:  # 如果节点为空，返回 -1 表示未找到
            return -1
        if node == target:  # 如果当前节点是目标节点，返回当前深度
            return current_depth
        # 在左子树递归查找深度
        left_depth = self.depth(node.left, target, current_depth + 1)
        if left_depth != -1:  # 如果左子树找到目标节点
            return left_depth
        # 否则在右子树递归查找
        return self.depth(node.right, target, current_depth + 1)

    # 前序遍历（根 → 左 → 右）
    def preorder_traversal(self, node):
        if node:
            print(node.value, end=" ")
            self.preorder_traversal(node.left)
            self.preorder_traversal(node.right)

    # 中序遍历（左 → 根 → 右）
    def inorder_traversal(self, node):
        if node:
            self.inorder_traversal(node.left)
            print(node.value, end=" ")
            self.inorder_traversal(node.right)

    # 后序遍历（左 → 右 → 根）
    def postorder_traversal(self, node):
        if node:
            self.postorder_traversal(node.left)
            self.postorder_traversal(node.right)
            print(node.value, end=" ")

    # 层次遍历（广度优先遍历）
    def level_order_traversal(self):
        if not self.root:
            return
        from collections import deque
        queue = deque([self.root])  # 使用队列
        while queue:
            current = queue.popleft()
            print(current.value, end=" ")
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)


# 测试代码
if __name__ == "__main__":
    # 创建二叉树
    tree = BinaryTree()
    
    # 添加节点
    tree.add("A")
    tree.add("B")
    tree.add("C")
    tree.add("D")
    tree.add("E")
    tree.add("F")

    # 打印树的高度
    print("Tree Height:", tree.height(tree.root))  # 输出: Tree Height: 2

    # 计算某个节点的深度
    print("Depth of Node D:", tree.depth(tree.root, tree.root.left.left))  # 输出: Depth of Node D: 2

    # 遍历并打印节点
    print("\nPreorder Traversal:", end=" ")
    tree.preorder_traversal(tree.root)  # 输出: A B D E C F

    print("\nInorder Traversal:", end=" ")
    tree.inorder_traversal(tree.root)  # 输出: D B E A C F

    print("\nPostorder Traversal:", end=" ")
    tree.postorder_traversal(tree.root)  # 输出: D E B F C A

    print("\nLevel Order Traversal:", end=" ")
    tree.level_order_traversal()  # 输出: A B C D E F
