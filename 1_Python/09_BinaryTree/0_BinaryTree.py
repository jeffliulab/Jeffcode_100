# 这个是自己写的，练习用

# 定义二叉树节点类
class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left 
        self.right = right

# 主类，包含创建树、添加节点、计算高度和深度，以及遍历的方法
class BinaryTree:
    def __init__(self):
        # initialize an empty tree
        # it is different from linkedlist
        self.root = None


    # 添加节点（递归添加到第一个可用位置）
    def add(self, value):
        # 先从root开始，如果root为空，创建root
        if not self.root:
            self.root = TreeNode(value)
            return # 这里写return是为了美观
        
        queue = [self.root]

        while queue:

            node = queue.pop(0)

            if not node.left:
                node.left = TreeNode(value)
                return 
            elif not node.right:
                node.right = TreeNode(value)
                return 
            else:
                queue.append(node.left)
                queue.append(node.right)



    # 计算树的高度
    def height(self, node):
        if not node:
            return 0
        
        queue = [node]
        height = 0
        
        while queue:
            level_size = len(queue)
            for _ in range(level_size):
                current_node = queue.pop(0)
                if current_node.left:
                    queue.append(current_node.left)
                if current_node.right:
                    queue.append(current_node.right)
            height += 1

        return height





    # 计算节点深度
    def depth(self, node, target, current_depth=0):
        # 这里必须用reference来比较，可以防止tree中有相同value的情况
        if not node:
            return -1
        
        if node is target: # use is to compare
            return current_depth

        # 接下来是recursive，先在left找
        left_depth = self.depth(node.left, target, current_depth+1)
        if left_depth != -1:
            return left_depth 
        
        right_depth = self.depth(node.right, target, current_depth + 1)
        return right_depth # 不管最后在右边找没找到，都return





    # 前序遍历（根 → 左 → 右）
    def preorder_traversal(self, node):
        result = []

        def dfs(node):
            if not node:
                return 
            result.append(node.value)
            dfs(node.left)
            dfs(node.right)
        
        dfs(node)
        return result


    # 中序遍历（左 → 根 → 右）
    def inorder_traversal(self, node):
        result = []

        def dfs(node):
            if not node:
                return 
            dfs(node.left)
            result.append(node.value)
            dfs(node.right)
        
        dfs(node)
        return result





    # 后序遍历（左 → 右 → 根）
    def postorder_traversal(self, node):
        result = []

        def dfs(node):
            if not node:
                return 
            dfs(node.left)
            dfs(node.right)
            result.append(node.value)

        dfs(node)
        return result



    # 层次遍历（广度优先遍历）
    def level_order_traversal(self):
        if not self.root:
            return []
        
        result = []
        queue = [self.root]

        while queue:
            level_size = len(queue)
            level = []

            for _ in range(level_size):
                node = queue.pop(0)
                level.append(node.value)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            result.append(level)

        return result




if __name__ == "__main__":
    try:
        # 创建二叉树
        tree = BinaryTree()
        
        # 添加节点
        tree.add("A")
        tree.add("B")
        tree.add("C")
        tree.add("D")
        tree.add("E")
        tree.add("F")

        # 测试树的高度
        height = tree.height(tree.root)
        assert height == 3, f"Height test failed! Expected: 3, Got: {height}"

        # 测试某个节点的深度
        depth_d = tree.depth(tree.root, tree.root.left.left)
        assert depth_d == 2, f"Depth test failed! Expected: 2, Got: {depth_d}"

        # 测试遍历
        # 前序遍历 - 直接使用返回的结果数组
        preorder_result = tree.preorder_traversal(tree.root)
        assert preorder_result == ["A", "B", "D", "E", "C", "F"], \
            f"Preorder traversal test failed! Got: {preorder_result}"

        # 中序遍历
        inorder_result = tree.inorder_traversal(tree.root)
        assert inorder_result == ["D", "B", "E", "A", "F", "C"], \
            f"Inorder traversal test failed! Got: {inorder_result}"

        # 后序遍历
        postorder_result = tree.postorder_traversal(tree.root)
        assert postorder_result == ["D", "E", "B", "F", "C", "A"], \
            f"Postorder traversal test failed! Got: {postorder_result}"

        # 层次遍历
        level_order_result = tree.level_order_traversal()
        assert level_order_result == [["A"], ["B", "C"], ["D", "E", "F"]], \
            f"Level order traversal test failed! Got: {level_order_result}"

        print("All tests passed successfully!")

    except AssertionError as e:
        print(e)