常规思路：
1. 从root开始往下找，找到p和q
2. 找到p和q后开始回退，直到发现共同祖先节点

上述思路针对任何类型的tree寻找ancestor，但是对于BST，根据其特性，left总是比root小，right总是比root大，因此当p和q的值分别小于和大于root的时候，就说明root是ancestor了。

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        while root:
            if p.val < root.val and q.val < root.val:
                root = root.left
            elif p.val > root.val and q.val > root.val:
                root = root.right
            else:
                return root
```