BFS
```python
from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        # bfs
        queue = deque([root])
        output = []
        while queue:
            this_level_size = len(queue)
            this_level_vals = []
            for _ in range(this_level_size):
                cur_node = queue.popleft()
                this_level_vals.append(cur_node.val)
                if cur_node.left:
                    queue.append(cur_node.left)
                if cur_node.right:
                    queue.append(cur_node.right)
            output.append(this_level_vals)
        return output
```

由于BFS本身就是LevelOrderTraversal，所以这道题天然更适合用BFS解决，也推荐用BFS解决。如果非要用DFS的话，原理就是记录层数，然后在遇到一个node的时候，把他append到对应的那个队列元素（output[depth]）中。
```python
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []

        def dfs(node, depth):
            if not node:
                return None
            if len(res) == depth:
                res.append([])
            
            res[depth].append(node.val)
            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)
        
        dfs(root, 0)
        return res
```