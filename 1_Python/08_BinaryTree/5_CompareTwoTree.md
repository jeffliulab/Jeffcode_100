DFS
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
```

BFS (初见非优化版本)
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def bfs(node):
            queue = [node]
            res = []
            if not node:
                return [None]
            while queue:
                level_size = len(queue)
                cur_node = queue.pop(0)
                if cur_node:
                    res.append(cur_node.val)
                    queue.append(cur_node.left)
                    queue.append(cur_node.right)
                else:
                    res.append(None)
            return res
        return bfs(p) == bfs(q)
```