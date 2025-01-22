这道题很简单，但是要思考一个问题：DFS VS BFS

BFS Pseudocode
```
def dfs(node, depth):
    if not node:
        return
    if depth == len(output):  # 首次到达该层
        output.append(node.val)
    dfs(node.right, depth + 1)  # 优先右子树
    dfs(node.left, depth + 1)   # 然后左子树
```

DFS Pseudocode
```
while queue:
    level_size = len(queue)
    for i in range(level_size):
        node = queue.pop(0)
        if i == level_size - 1:  # 每层最后一个节点
            output.append(node.val)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
```

时间复杂度：都是O(n)

空间复杂度：
* DFS (O(h)，h 为树的深度)
* BFS (O(w), w 为树的宽度)

完全二叉树：DFS 更优，因为深度较小，递归简单高效，空间复杂度低。

一般二叉树：BFS 更合适，因为层次遍历能更好地处理不规则结构，逻辑更直观。

整体来看，还是更适合用BFS，更直观。