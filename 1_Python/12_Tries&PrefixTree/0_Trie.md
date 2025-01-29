Trie 的名字来自单词 "retrieval"（检索），因为它的设计目的是快速检索字符串。

Trie 的中文一般叫做 前缀树 或 字典树。

数据结构：
```
class TrieNode:
    def __init__(self):
        self.children = {}  # 存储子节点
        self.word = False   # 是否是单词结尾
```

root 本身并不代表任何字母，它只是一个空节点（虚拟根节点）。字母信息是存储在 children 字典的键 中，而不是节点本身。

具体用法：
```python
# Trie Implementation and Usage in Python

class TrieNode:
    def __init__(self):
        self.children = {}  # Dictionary to store child nodes
        self.word = False   # Indicates if a word ends at this node

class Trie:
    def __init__(self):
        self.root = TrieNode()  # Root node of the Trie

    def insert(self, word):
        """Insert a word into the Trie."""
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.word = True  # Mark the end of the word

    def search(self, word):
        """Search if a word exists in the Trie."""
        curr = self.root
        for c in word:
            if c not in curr.children:
                return False  # Character not found, word doesn't exist
            curr = curr.children[c]
        return curr.word  # Check if it's a complete word

    def starts_with(self, prefix):
        """Check if there is any word in the Trie that starts with the given prefix."""
        curr = self.root
        for c in prefix:
            if c not in curr.children:
                return False  # Character not found, prefix doesn't exist
            curr = curr.children[c]
        return True  # Prefix exists

# Example Usage
def main():
    trie = Trie()

    # Insert words into the Trie
    trie.insert("apple")
    trie.insert("app")
    trie.insert("banana")
    
    # Search for words
    print(trie.search("apple"))   # Output: True ("apple" exists)
    print(trie.search("app"))     # Output: True ("app" exists as a complete word)
    print(trie.search("appl"))    # Output: False ("appl" is a prefix, not a word)

    # Check prefixes
    print(trie.starts_with("app"))  # Output: True ("app" is a prefix)
    print(trie.starts_with("ban"))  # Output: True ("ban" is a prefix)
    print(trie.starts_with("cat"))  # Output: False ("cat" does not exist)

if __name__ == "__main__":
    main()
```
