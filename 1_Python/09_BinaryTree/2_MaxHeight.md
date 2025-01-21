DFS (Recursive, Inner Function)
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def maxH(node):
            if not node:
                return 0
            return 1 + max(maxH(node.left),maxH(node.right))
        return maxH(root)
```

DFS (Recursive)
```python
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
```

DFS (Stack)
```python
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        stack = [[root, 1]]
        res = 0

        while stack:
            node, depth = stack.pop()

            if node:
                res = max(res, depth)
                stack.append([node.left, depth + 1])
                stack.append([node.right, depth + 1])
        return res
```

BFS
```python
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # to find height
        if not root:
            return 0
        queue = [root]
        h = 0
        while queue:
            level_size = len(queue)
            for _ in range(level_size):
                cur_node = queue.pop(0)
                if cur_node.left:
                    queue.append(cur_node.left)
                if cur_node.right:
                    queue.append(cur_node.right)
            h += 1
        return h
```












        