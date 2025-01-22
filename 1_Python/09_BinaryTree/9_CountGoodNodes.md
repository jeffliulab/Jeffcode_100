和上一道题不同，这道题天然适合DFS

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        count = 0

        def dfs(node, max_val):
            if not node:
                return 
            
            nonlocal count

            if node.val >= max_val:
                count += 1

            max_val = max (node.val, max_val)

            dfs(node.left, max_val)
            dfs(node.right, max_val)

        dfs(root, root.val)
        
        return count
```


代码优化版本（Neetcode提供的，稍微简化了代码，取消了nonlocal变量的使用）
```python
class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def dfs(node, maxVal):
            if not node:
                return 0

            res = 1 if node.val >= maxVal else 0
            maxVal = max(maxVal, node.val)
            res += dfs(node.left, maxVal)
            res += dfs(node.right, maxVal)
            return res

        return dfs(root, root.val)
```