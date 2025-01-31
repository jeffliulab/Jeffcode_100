```python
class TreeNode:
    def __init__(self):
        self.child = {}
        self.word = False

class PrefixTree:

    def __init__(self):
        self.root = TreeNode()
        

    def insert(self, word: str) -> None:
        cur_node = self.root
        for c in word:
            if c not in cur_node.child:
                cur_node.child[c] = TreeNode()
            cur_node = cur_node.child[c]
        cur_node.word = True


    def search(self, word: str) -> bool:
        cur_node = self.root
        for c in word:
            if c not in cur_node.child:
                return False
            cur_node = cur_node.child[c]
        return cur_node.word

    def startsWith(self, prefix: str) -> bool:
        cur_node = self.root
        for c in prefix:
            if c not in cur_node.child:
                return False
            cur_node = cur_node.child[c]
        return True
```