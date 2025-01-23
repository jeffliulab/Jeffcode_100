我的思路是在reconstruct的基础上进行：
1. 将tree分别用preorder和inorder DFS遍历，然后存储到一个字符串中，可以用P... I...区分
2. 将字符串以P和I进行区分，然后提取preorder和inorder的部分，进行tree reconstruct

该方法在实际使用中遇到了重复值不好处理的问题，比如对于[3,4,1,3]这样的有多个3的序列，就不好弄了。

对于有可能有重复值的情况，更直观的方法就是对空值也进行记录，比如记录为N，然后用DFS或者BFS进行遍历及恢复。

DFS
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        string = ""
        def dfs(node):
            nonlocal string
            if not node:
                string += "N,"
                return
            string += str(node.val) + ","
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return string
     

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        ls = data.split(",")
        i = 0

        def dfs():
            nonlocal i

            if i >= len(ls): # 用 >= 是防御性编程。虽然正常情况不会大于，但这样更安全。可以只用 ==。
                return None
            if ls[i] == "N":
                i += 1
                return None
            
            root = TreeNode(int(ls[i]))

            # 顺序必须固定，因为序列化时用的是前序遍历(根-左-右)，
            # 反序列化也必须按相同顺序。先读当前节点值并+1，再递归处理左右子树。
            i += 1 
            root.left = dfs()
            root.right = dfs()
            return root
        
        return dfs()
```

BFS稍微要想一下，其实也很简单。首先traverse成一个BFS序列很好理解，然后对于一个序列，其i=0的元素一定是root，以此类推，第1个是root的left node，第2个是root的right node，第三个是left node的left node，整体保持一个i*2+1是left node，i*2+2是right node的顺序。

BFS
```python
class Codec:    
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""
        queue = [root]
        result = []  # 改用列表存储结果，最后用逗号连接
        
        while queue:
            node = queue.pop(0)
            if node:  
                result.append(str(node.val))  # 添加节点值
                queue.extend([node.left, node.right])  # 左右子节点入队
            else:  
                result.append("N")  # 空节点标记
                
        return ",".join(result)  # 用逗号连接所有值
    
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data:
            return None
            
        ls = data.split(",")  # 分割字符串得到节点值列表
        root = TreeNode(int(ls[0]))
        queue = [root]
        i = 1
        
        while queue and i < len(ls):
            node = queue.pop(0)
            # 处理左子节点
            if i < len(ls) and ls[i] != 'N':
                node.left = TreeNode(int(ls[i]))
                queue.append(node.left)
            i += 1
            # 处理右子节点
            if i < len(ls) and ls[i] != 'N':
                node.right = TreeNode(int(ls[i]))
                queue.append(node.right)
            i += 1
        
        return root
```