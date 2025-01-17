本页面展示基于Merge2的最基本版本的解，更优的解在后面分治和最小堆那里还会再次提到。

Merge K = Merge 2 one by one

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

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:  # 如果列表为空，返回 None
            return None
        
        # 初始链表为第一个链表
        ll = lists[0]
        
        for i in range(1, len(lists)):
            ll = self.mergeTwoLists(ll, lists[i])
        
        return ll
```