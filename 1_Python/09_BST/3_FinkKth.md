可以用DFS来INORDER TRAVERSE BST，这样第k个元素一定就是要找的第K小的元素。

用一个counter，在普通DFS中计数，当counter==k的时候，记录这个值，然后最后return这个值，就可以了。

但是直接DFS会导致多余的traverse，所以在此基础上，增加提前终止的思路，在找到符合要求的情况下就return：
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # 中序遍历（In-order Traversal）： BST的中序遍历会按从小到大的顺序访问节点的值。
        # 因此，第k个访问到的节点就是第k小的值。
        # 这里要注意：
        # 确实，当 num == k 的时候可以直接 return，
        # 但在递归函数中直接 return 只会退出当前的递归调用，而不会终止整个递归过程。
        num = 0
        def dfs(node):
            nonlocal num
            if not node:
                return
            left = dfs(node.left)
            if left is not None:
                return left

            num += 1
            if num == k:
                return node.val
            # 在 def dfs(node): 函数中，只有一种情况会真正返回一个值：
            # 当 num == k 的时候，这时返回的值就是目标结果（第 k 小的节点值）。

            return dfs(node.right)

        return dfs(root)
```