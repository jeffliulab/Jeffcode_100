```python
class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left  # 左子树
        self.right = right  # 右子树
```

Height
```python
# Height: 从某个节点到其最远叶子节点的路径长度
def get_height(node):
    if not node:  # 空节点高度为 -1（或根据需求设置为 0）
        return -1
    left_height = get_height(node.left)
    right_height = get_height(node.right)
    return max(left_height, right_height) + 1
```

Depth
```python
# Depth: 从根节点到某个节点的路径长度
def get_depth(node, target, depth=0):
    if not node:  # 节点为空，返回 -1 表示未找到
        return -1
    if node == target:  # 找到目标节点
        return depth
    # 在左子树或右子树中递归查找
    left_depth = get_depth(node.left, target, depth + 1)
    if left_depth != -1:  # 如果在左子树找到了
        return left_depth
    return get_depth(node.right, target, depth + 1)  # 否则继续在右子树找
```

Practice
```py
# 创建树
root = TreeNode("A")
root.left = TreeNode("B")
root.right = TreeNode("C")
root.left.left = TreeNode("D")
root.left.right = TreeNode("E")
root.right.right = TreeNode("F")

# 计算树的高度（以根节点为例）
print("Tree Height:", get_height(root))  # 输出: Tree Height: 2

# 查询某个节点的深度（以节点 "E" 为例）
print("Depth of Node E:", get_depth(root, root.left.right))  # 输出: Depth of Node E: 2
```

Traverse - DFS
```python
# Preorder Traversal 前序遍历
# 顺序：根节点 → 左子树 → 右子树
def preorder_traversal(node):
    if not node:
        return
    print(node.value, end=" ")  # 访问当前节点
    preorder_traversal(node.left)  # 遍历左子树
    preorder_traversal(node.right)  # 遍历右子树

# Inorder Traversal 中序遍历
# 顺序：左子树 → 根节点 → 右子树
def inorder_traversal(node):
    if not node:
        return
    inorder_traversal(node.left)  # 遍历左子树
    print(node.value, end=" ")  # 访问当前节点
    inorder_traversal(node.right)  # 遍历右子树

# Postorder Traversal 后序遍历
# 顺序：左子树 → 右子树 → 根节点
def postorder_traversal(node):
    if not node:
        return
    postorder_traversal(node.left)  # 遍历左子树
    postorder_traversal(node.right)  # 遍历右子树
    print(node.value, end=" ")  # 访问当前节点

```

Traverse - BFS
```python
# 广度优先遍历按照树的层次从上到下，从左到右逐层遍历。
# 顺序：逐层从左到右访问节点
from collections import deque

def level_order_traversal(node):
    if not node:
        return
    queue = deque([node])  # 使用队列存储当前层的节点
    while queue:
        current = queue.popleft()  # 从队列中取出一个节点
        print(current.value, end=" ")  # 访问当前节点
        if current.left:  # 将左子节点加入队列
            queue.append(current.left)
        if current.right:  # 将右子节点加入队列
            queue.append(current.right)
```