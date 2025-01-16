The special skill here：

（1） Use two fast and slow pointers, and let two pointers keep a distance of n.

（2）Another point is to determine which position is the place that slow point should stop.

（3） Use dum, 这样就算第一个就要删掉也不会出问题。

```py
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dum = ListNode(-1, head)

        slow, fast = dum, dum
        for _ in range(n+1):
            fast = fast.next

        while(fast):
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next

        return dum.next
```