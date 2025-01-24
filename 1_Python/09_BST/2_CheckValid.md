常规思路是直接用inorder traverse，然后生成一个list，确保list中没有非严格递增的情况就行。如果在用dfs的时候直接比较prev，还可以省去list的空间，达到和下面这个方法一样的最优效果。

但是结合BST的特性，一般推荐如下解法：
```python
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid(node, left, right):
            if not node:
                return True
            if not (left < node.val < right):  # 当前节点值必须在范围内
                return False
            # 左子树的上界是当前节点值，右子树的下界是当前节点值
            return valid(node.left, left, node.val) and valid(node.right, node.val, right)

        return valid(root, float("-inf"), float("inf"))
```

该解法和我一开始说的解法efficiency是一样的：
```python
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        prev = None

        def dfs(node):
            nonlocal prev
            if not node:
                return True
            if not dfs(node.left):
                return False
            if prev is not None and node.val <= prev:
                return False
            prev = node.val
            return dfs(node.right)

        return dfs(root)
```

我最开始写的最直观的解法如下：
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        ls = []
        def dfs(node):
            nonlocal ls
            if not node:
                return 
            dfs(node.left)
            ls.append(node.val)
            dfs(node.right)

        dfs(root)

        for i in range(len(ls)-1):
            if ls[i] >= ls[i+1]:
                return False
        return True
```