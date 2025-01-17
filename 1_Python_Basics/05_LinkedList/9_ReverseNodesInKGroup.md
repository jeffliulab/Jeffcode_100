The most complicated one so far.

这道题是Python_Basics部分第一个在结构上变得复杂起来的例题。

这道题的逻辑并不难，每K个组成一个sub-linkedlist, 然后反转过来，然后连接起来，但是由于linkedlist本身的数据结构，导致该题在implement的时候较为复杂。

推荐模块化的写法，将reverse作为子函数写在里头，这样逻辑上更清晰一点：
```py
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # 辅助函数：反转链表
        def reverseLinkedList(head):
            prev = None
            cur = head
            while cur:
                cur_next = cur.next
                cur.next = prev
                prev = cur
                cur = cur_next
            return prev
        
        # 检查链表长度是否足够
        def hasEnoughNodes(start, k):
            count = 0
            while start and count < k:
                start = start.next
                count += 1
            return count == k

        dummy = ListNode(0)
        dummy.next = head
        prev_group_end = dummy
        cur = head

        while cur:
            # 检查是否有足够的节点反转
            if not hasEnoughNodes(cur, k):
                break

            # 记录当前部分的开始和结束
            group_start = cur
            group_end = cur
            for _ in range(k - 1):
                group_end = group_end.next

            # 记录下一个部分的开始
            next_group_start = group_end.next

            # 断开当前部分
            group_end.next = None

            # 反转当前部分
            reversed_group = reverseLinkedList(group_start)

            # 将反转的部分连接到前面和后面
            prev_group_end.next = reversed_group
            group_start.next = next_group_start

            # 更新指针
            prev_group_end = group_start
            cur = next_group_start

        return dummy.next
```


在Python中，如果不追求Os(1)，可以用更简洁的list来实现：
Ot(n), Os(n)
```py
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return []
        
        ls = []
        
        cur = head
        while cur:
            ls.append(cur.val)
            cur = cur.next
        
        for i in range(0,len(ls),k):
            if i + k <= len(ls):
                ls[i:i+k] = ls[i:i+k][::-1]


        dum = ListNode(-1)
        cur = dum
        for val in ls:
            cur.next = ListNode(val)
            cur = cur.next
        
        return dum.next
```