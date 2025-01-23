PatternMatch不是刷题和面试的重点，但是对优化算法效率来说很重要。

在BinaryTree/IsSubTree这个问题中，如果用DFS解，需要Ot(m*n)的复杂度。而使用Z函数或者KMP，可以降低到Ot(m+n)。

Z函数：
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution: 
    def serialize(self, root: Optional[TreeNode]) -> str:
            if root == None:
                return "$#"
            
            return ("$" + str(root.val) + 
                    self.serialize(root.left) + self.serialize(root.right))  

    def z_function(self, s: str) -> list:
        z = [0] * len(s)
        l, r, n = 0, 0, len(s)
        for i in range(1, n):
            if i <= r:
                z[i] = min(r - i + 1, z[i - l])
            while i + z[i] < n and s[z[i]] == s[i + z[i]]:
                z[i] += 1
            if i + z[i] - 1 > r:
                l, r = i, i + z[i] - 1
        return z

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        serialized_root = self.serialize(root)
        serialized_subRoot = self.serialize(subRoot)
        combined = serialized_subRoot + "|" + serialized_root
        
        z_values = self.z_function(combined)
        sub_len = len(serialized_subRoot)
        
        for i in range(sub_len + 1, len(combined)):
            if z_values[i] == sub_len:
                return True
        return False
```

KMP：
```python
class Solution:
    def serialize(self, root: Optional[TreeNode]) -> str:
        if root is None:
            return "$#"
        return "$" + str(root.val) + self.serialize(root.left) + self.serialize(root.right)

    def build_prefix_table(self, pattern: str) -> list:
        """
        构造前缀表（Partial Match Table）
        """
        prefix_table = [0] * len(pattern)
        j = 0  # 前缀指针

        for i in range(1, len(pattern)):
            while j > 0 and pattern[i] != pattern[j]:
                j = prefix_table[j - 1]  # 回退到前一个匹配的位置

            if pattern[i] == pattern[j]:
                j += 1

            prefix_table[i] = j

        return prefix_table

    def kmp_search(self, text: str, pattern: str) -> bool:
        """
        使用前缀表进行字符串匹配
        """
        prefix_table = self.build_prefix_table(pattern)
        j = 0  # 模式串指针

        for i in range(len(text)):
            while j > 0 and text[i] != pattern[j]:
                j = prefix_table[j - 1]  # 回退到前一个匹配的位置

            if text[i] == pattern[j]:
                j += 1

            if j == len(pattern):  # 完整匹配
                return True

        return False

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        serialized_root = self.serialize(root)
        serialized_subRoot = self.serialize(subRoot)

        return self.kmp_search(serialized_root, serialized_subRoot)
```