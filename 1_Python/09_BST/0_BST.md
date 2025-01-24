BST 结构示意图
```
Binary Search Tree（BST） 是一种特殊的二叉树，具有以下特性：
1. 左子树所有节点值 小于 根节点值。
2. 右子树所有节点值 大于 根节点值。
3. 每个子树也必须是一个 BST（递归定义）。

Example:

        8
       / \
      3   10
     / \    \
    1   6    14
       / \   /
      4   7 13


```

插入
```python
"""
功能：将一个值插入到二叉搜索树中，同时保持 BST 的性质（左 < 根 < 右）。

逻辑：
1. 从根节点开始，与当前节点比较：
      如果新值小于当前节点值，尝试插入到左子树；
      如果新值大于当前节点值，尝试插入到右子树。
2. 如果当前节点为空（到达叶节点），则创建一个新节点并插入。
3. 如果新值等于当前节点值，通常不插入（BST 不允许重复值）。
"""
class TreeNode:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    # 插入方法
    def insert(self, root, val):
        if root is None:
            return TreeNode(val)  # 找到插入位置，返回新节点

        if val < root.val:
            root.left = self.insert(root.left, val)  # 插入左子树
        elif val > root.val:
            root.right = self.insert(root.right, val)  # 插入右子树

        return root  # 返回根节点，保持树结构
```

搜索
```python
"""
功能：检查某个值是否存在于 BST 中。

逻辑：
1. 从根节点开始，与当前节点值比较：
      如果值等于当前节点值，则找到目标，返回 True。
      如果值小于当前节点值，继续搜索左子树。
      如果值大于当前节点值，继续搜索右子树。
2. 如果到达空节点（None），则目标值不存在，返回 False。
"""
class BST:
    # 搜索方法
    def search(self, root, val):
        if root is None:  # 到达叶节点，未找到
            return False
        if root.val == val:  # 找到目标
            return True
        elif val < root.val:
            return self.search(root.left, val)  # 搜索左子树
        else:
            return self.search(root.right, val)  # 搜索右子树

```