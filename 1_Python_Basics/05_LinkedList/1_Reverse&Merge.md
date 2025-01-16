这是两个练习LinkedList使用方法的题。

重要用法：

1、虚拟头节点dummy，不能设置为None，一般设置为-1

2、设置一个游标cur，不断用游标cur去延长linked list

## Reverse a linked list

用一个list存储，然后反转，Ot(n)但占用空间较高

占用空间优化：让linked list的1～5按顺序的箭头们全都变成反过来的，也就是原地反转

```py
# prev：记录当前节点的“前一个节点”（初始为 None，因为 1 的前面没有节点）。
# current：记录当前正在操作的节点（初始为链表的第一个节点 1）。
# next_node：暂存当前节点的 next，防止链表断开。
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        prev = None
        cur = head
        
        while(cur):
            cur_next = cur.next # store the remaining part 2-3-4
            cur.next = prev # reverse the arrow, cur = 1-None
            prev = cur # prev= 1-None
            cur = cur_next

        return prev
```


## Merge two sorted linked list

```py
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dum = ListNode(-1)
        cur = dum
        while list1 and list2:
            if list1.val > list2.val:
                cur.next = list2
                list2 = list2.next
            else:
                cur.next = list1
                list1 = list1.next
            cur = cur.next
        
        if list1:
            cur.next = list1
        if list2:
            cur.next = list2
        
        return dum.next
```