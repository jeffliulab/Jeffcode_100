Special Skill: Use slow and fast pointers to find the middle of the linked list

```py
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # use fast slow point to find the middle
        slow, fast = head, head
        while(fast and fast.next):
            slow = slow.next
            fast = fast.next.next

        # reverse the latter half part
        prev = None
        cur = slow.next
        while(cur):
            cur_next = cur.next
            cur.next = prev
            prev = cur
            cur = cur_next

        # cut the linkedlist
        slow.next = None

        # merge two linkedlists
        cur1, cur2 = head, prev
        while(cur2):
            cur1_next, cur2_next = cur1.next, cur2.next
            cur1.next = cur2
            cur2.next = cur1_next
            cur1, cur2 = cur1_next, cur2_next
```