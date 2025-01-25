Binary Tree Maximum Path Sum
Given the root of a non-empty binary tree, return the maximum path sum of any non-empty path.

A path in a binary tree is a sequence of nodes where each pair of adjacent nodes has an edge connecting them. A node can not appear in the sequence more than once. The path does not necessarily need to include the root.

The path sum of a path is the sum of the node's values in the path.

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # 初始化全局最大路径和
        self.max_sum = float('-inf')
        
        # 递归函数，返回从当前节点出发的单侧最大路径和
        def dfs(node):
            if not node:
                return 0  # 空节点返回 0
            
            # 递归计算左子树和右子树的最大路径和
            # 如果某条路径的和为负数，则选择 0，不延伸该路径
            # 实现方式：逐层延展和传递单侧最大路径和
            left_max = max(dfs(node.left), 0)
            right_max = max(dfs(node.right), 0)
            
            # 更新全局最大路径和：当前节点值 + 左路径和 + 右路径和
            self.max_sum = max(self.max_sum, left_max+right_max+node.val)
            
            # 返回当前节点为起点的单侧最大路径和
            # 父节点调用递归时，只能从当前节点的某一侧（左或右）接收路径和，不能同时接收两侧。
            # 因为路径不能分叉，它是一个单向连续的路径。
            # 这里的的return值，不是为了最终的 max_sum，而是为了父节点能够正确计算路径和。
            # 用这个return value的地方在上面计算left_max和right_max的地方。
            return node.val + max(left_max, right_max)
        
        # 从根节点开始递归
        dfs(root)

        return int(self.max_sum)
```