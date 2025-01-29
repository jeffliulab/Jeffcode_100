Neetcode LinkedList/MergeK 最经典的解法，使用Heap

设置一个heap，让heap里永远只放着每个linkedlist的第一个值，这样就可以保证heap的第一个位子的那个值总是最小的，然后不停pop那个值，放到新的linkedlist里。

Ot(nlogk), Os(k)
```python
# 注：这个在neetcode里的答案有点麻烦，用下面这个方法可以巧妙避免list_node.val一样的时候，
# heap自动比较第二个list_node导致的list_node无法比较的问题
# 使用python的情况下，这种方法更符合python哲学，是更pythonic的解法

import heapq
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        for i, list_node in enumerate(lists):
            if list_node:
                heapq.heappush(heap, (list_node.val, i, list_node))

        dum = ListNode(-1)
        cur_node = dum
        while heap:
            val, index, heap_head_node = heapq.heappop(heap)
            if heap_head_node.next is not None:
                another = heap_head_node.next
                heapq.heappush(heap, (another.val, index, another))
            cur_node.next = heap_head_node
            cur_node = cur_node.next

        return dum.next            
```

不过从面向对象设计的角度来看，neetcode提供的方法也不错：
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class NodeWrapper:
    def __init__(self, node):
        self.node = node

    def __lt__(self, other):
        return self.node.val < other.node.val

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None

        res = ListNode(0)
        cur = res
        minHeap = []

        for lst in lists:
            if lst is not None:
                heapq.heappush(minHeap, NodeWrapper(lst))

        while minHeap:
            node_wrapper = heapq.heappop(minHeap)
            cur.next = node_wrapper.node
            cur = cur.next
            
            if node_wrapper.node.next:
                heapq.heappush(minHeap, NodeWrapper(node_wrapper.node.next))
        
        return res.next
```