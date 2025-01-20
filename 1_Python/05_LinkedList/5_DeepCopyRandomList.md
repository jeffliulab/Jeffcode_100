Shallow Copy: 仅复制对象的引用，而不是复制对象本身。如果原始对象发生变化，浅拷贝对象也会受到影响。

Deep Copy: 会创建一个新的对象，并递归复制所有内容，确保新对象和原始对象完全独立，互不影响。

难点：
* 节点独立性： 直接赋值复制的只是指针，新链表节点必须完全独立于原链表节点。
* random 指针处理： random 指针的目标节点需要找到新链表中的对应节点，而不是直接指向原链表节点。
* 链表结构维护： 在构建新链表时，需同时维护 next 和 random 指针的正确关系。
* 链表拆分： 构建新链表后，需要从混合链表中正确拆分出原链表和新链表，确保两者结构独立且完整。


## Solution Use Dict

Ot(n), Os(n)

```py
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        dt = {}

        if not head:
            return None

        cur = head
        while cur:
            dt[cur] = Node(cur.val)
            cur = cur.next

        cur = head
        while cur:
            dt[cur].next = dt[cur.next] if cur.next else None
            dt[cur].random = dt[cur.random] if cur.random else None
            cur = cur.next
        
        return dt[head]
```

## Solution with Os(1) - 将新节点插在旧Linkedlist中，然后分离

```
1 -> 1' -> 2 -> 2' -> 3 -> 3' -> None
         |              |
         V              V
         2'             1'
```


```py 
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        cur = head
        while cur:
            cur_next = cur.next
            cur.next = Node(cur.val)
            cur.next.next = cur_next
            cur = cur_next

        cur = head
        while cur:
            if cur.random:
                cur.next.random = cur.random.next
            cur = cur.next.next
        
        cur = head
        dum = Node(-1)
        new_head = dum
        while cur:
            cur_real_next = cur.next.next
            dum_real_next = cur.next
            cur.next = cur_real_next
            dum.next = dum_real_next
            cur = cur.next
            dum = dum.next

        return new_head.next
```

优化版：（在最后断开的地方更优化一点，直接在原本的链接上断开）
```py
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        # Step 1: 在每个原节点后插入新节点
        cur = head
        while cur:
            cur_next = cur.next
            cur.next = Node(cur.val)
            cur.next.next = cur_next
            cur = cur_next

        # Step 2: 设置新节点的 random 指针
        cur = head
        while cur:
            if cur.random:
                cur.next.random = cur.random.next
            cur = cur.next.next

        # Step 3: 分离原链表和新链表
        cur = head
        new_head = head.next
        while cur:
            new_node = cur.next       # 当前新节点
            cur.next = new_node.next  # 恢复原链表
            if new_node.next:         # 如果还有下一个新节点
                new_node.next = new_node.next.next  # 更新新链表的 next
            cur = cur.next            # 移动到下一个原节点

        return new_head
```


## 还没看的方案：在random处存储新Node

和上面的方法一样是Os(1)，更加巧妙一点，这种方法的主要优势是避免了直接在链表中插入新节点（操作 next 指针）的复杂性，而是通过原链表的 random 指针暂存新节点，从而使逻辑更加简洁。

```NOT SEEN YET
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None

        l1 = head
        while l1:
            l2 = Node(l1.val)
            l2.next = l1.random
            l1.random = l2
            l1 = l1.next
        
        newHead = head.random
        
        l1 = head
        while l1:
            l2 = l1.random
            l2.random = l2.next.random if l2.next else None
            l1 = l1.next
            
        l1 = head
        while l1 is not None:
            l2 = l1.random
            l1.random = l2.next
            l2.next = l1.next.random if l1.next else None
            l1 = l1.next

        return newHead
```