
```
You are given the head of a linked list of length n. Unlike a singly linked list, each node contains an additional pointer random, which may point to any node in the list, or null.

Create a deep copy of the list.

The deep copy should consist of exactly n new nodes, each including:

The original value val of the copied node
A next pointer to the new node corresponding to the next pointer of the original node
A random pointer to the new node corresponding to the random pointer of the original node
```

Shallow Copy: 仅复制对象的引用，而不是复制对象本身。如果原始对象发生变化，浅拷贝对象也会受到影响。

Deep Copy: 会创建一个新的对象，并递归复制所有内容，确保新对象和原始对象完全独立，互不影响。

难点总结：
```
节点独立性： 直接赋值复制的只是指针，新链表节点必须完全独立于原链表节点。
random 指针处理： random 指针的目标节点需要找到新链表中的对应节点，而不是直接指向原链表节点。
链表结构维护： 在构建新链表时，需同时维护 next 和 random 指针的正确关系。
链表拆分： 构建新链表后，需要从混合链表中正确拆分出原链表和新链表，确保两者结构独立且完整。
```