在Python中，并没有内置Linked List，因为其经典使用场景（如队列、堆栈、快速插入和删除）在 Python 中已经被其他更高效的工具替代：
* 队列（Queue）：使用 collections.deque 可以更高效地完成队列操作，而无需自己实现链表。
* 堆栈（Stack）：使用 Python 的 list 可以实现堆栈的压入（append）和弹出（pop）。
* 快速插入与删除：在大多数情况下，链表的 O(1) 插入优势无法弥补其 O(n) 遍历的劣势。

## Singly LinkedList in Python

```py
# Definition of LinkedList Node
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val  # Value stored in the node
        self.next = next  # Reference to the next node in the linked list

# LinkedList Utilities
class LinkedListUtils:
    @staticmethod
    def create_linked_list(values):
        """
        Create a linked list from a list of values.
        :param values: List of values to initialize the linked list
        :return: Head node of the created linked list
        """
        if not values:
            return None  # Return None for an empty list

        head = ListNode(values[0])  # Create the head node
        current = head
        for value in values[1:]:
            current.next = ListNode(value)  # Link new node
            current = current.next  # Move to the next node
        return head

    @staticmethod
    def print_linked_list(head):
        """
        Print the values in a linked list.
        :param head: Head node of the linked list
        """
        current = head
        while current:
            print(current.val, end=" -> ")
            current = current.next
        print("None")

    @staticmethod
    def reverse_linked_list(head):
        """
        Reverse a linked list.
        :param head: Head node of the linked list
        :return: New head node of the reversed linked list
        """
        prev = None
        current = head
        while current:
            next_node = current.next  # Save the next node
            current.next = prev  # Reverse the current node's pointer
            prev = current  # Move prev forward
            current = next_node  # Move current forward
        return prev

    @staticmethod
    def find_middle(head):
        """
        Find the middle node of a linked list.
        :param head: Head node of the linked list
        :return: The middle node
        """
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next  # Move slow pointer by one step
            fast = fast.next.next  # Move fast pointer by two steps
        return slow

    @staticmethod
    def detect_cycle(head):
        """
        Detect if a linked list has a cycle.
        :param head: Head node of the linked list
        :return: True if there is a cycle, False otherwise
        """
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True  # Cycle detected
        return False

    @staticmethod
    def merge_two_sorted_lists(l1, l2):
        """
        Merge two sorted linked lists into one sorted linked list.
        :param l1: Head node of the first linked list
        :param l2: Head node of the second linked list
        :return: Head node of the merged linked list
        """
        dummy = ListNode()  # Dummy node to simplify edge cases
        current = dummy
        while l1 and l2:
            if l1.val < l2.val:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next
            current = current.next
        current.next = l1 or l2  # Attach the remaining nodes
        return dummy.next

# Example Usage
if __name__ == "__main__":
    # Create a linked list from a list of values
    head = LinkedListUtils.create_linked_list([1, 2, 3, 4, 5])

    # Print the linked list
    print("Original Linked List:")
    LinkedListUtils.print_linked_list(head)

    # Reverse the linked list
    head = LinkedListUtils.reverse_linked_list(head)
    print("Reversed Linked List:")
    LinkedListUtils.print_linked_list(head)

    # Find the middle of the linked list
    middle = LinkedListUtils.find_middle(head)
    print(f"Middle Node Value: {middle.val}")

    # Check if the linked list has a cycle
    print("Has Cycle:", LinkedListUtils.detect_cycle(head))

    # Merge two sorted linked lists
    l1 = LinkedListUtils.create_linked_list([1, 3, 5])
    l2 = LinkedListUtils.create_linked_list([2, 4, 6])
    merged_head = LinkedListUtils.merge_two_sorted_lists(l1, l2)
    print("Merged Sorted Linked List:")
    LinkedListUtils.print_linked_list(merged_head)

```

## Doubly LinkedList

```py
# Definition of Doubly Linked List Node
class DoublyListNode:
    def __init__(self, val=0, next=None, prev=None):
        self.val = val  # Value stored in the node
        self.next = next  # Reference to the next node in the linked list
        self.prev = prev  # Reference to the previous node in the linked list

# Doubly Linked List Utilities
class DoublyLinkedListUtils:
    @staticmethod
    def create_doubly_linked_list(values):
        """
        Create a doubly linked list from a list of values.
        :param values: List of values to initialize the doubly linked list
        :return: Head node of the created doubly linked list
        """
        if not values:
            return None  # Return None for an empty list

        head = DoublyListNode(values[0])  # Create the head node
        current = head
        for value in values[1:]:
            new_node = DoublyListNode(value)
            current.next = new_node  # Link new node to current's next
            new_node.prev = current  # Link current as new node's prev
            current = new_node  # Move to the next node
        return head

    @staticmethod
    def print_doubly_linked_list(head):
        """
        Print the values in a doubly linked list from head to tail.
        :param head: Head node of the doubly linked list
        """
        current = head
        while current:
            print(current.val, end=" <-> ")
            current = current.next
        print("None")

    @staticmethod
    def reverse_doubly_linked_list(head):
        """
        Reverse a doubly linked list.
        :param head: Head node of the doubly linked list
        :return: New head node of the reversed doubly linked list
        """
        current = head
        new_head = None
        while current:
            new_head = current  # Update new head
            current.next, current.prev = current.prev, current.next  # Swap next and prev
            current = current.prev  # Move to the next node (originally prev)
        return new_head

    @staticmethod
    def insert_after(node, value):
        """
        Insert a new node with a specified value after a given node in the doubly linked list.
        :param node: The node after which the new node will be inserted
        :param value: The value for the new node
        """
        new_node = DoublyListNode(value)
        new_node.next = node.next
        new_node.prev = node
        if node.next:
            node.next.prev = new_node
        node.next = new_node

    @staticmethod
    def delete_node(node):
        """
        Delete a specified node from the doubly linked list.
        :param node: The node to be deleted
        """
        if node.prev:
            node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev
        node.next = None
        node.prev = None

# Example Usage
if __name__ == "__main__":
    # Create a doubly linked list from a list of values
    head = DoublyLinkedListUtils.create_doubly_linked_list([1, 2, 3, 4, 5])

    # Print the doubly linked list
    print("Original Doubly Linked List:")
    DoublyLinkedListUtils.print_doubly_linked_list(head)

    # Reverse the doubly linked list
    head = DoublyLinkedListUtils.reverse_doubly_linked_list(head)
    print("Reversed Doubly Linked List:")
    DoublyLinkedListUtils.print_doubly_linked_list(head)

    # Insert a new node after the second node
    second_node = head.next  # Assuming the list has at least two nodes
    DoublyLinkedListUtils.insert_after(second_node, 6)
    print("After Inserting 6:")
    DoublyLinkedListUtils.print_doubly_linked_list(head)

    # Delete the second node
    DoublyLinkedListUtils.delete_node(second_node)
    print("After Deleting Second Node:")
    DoublyLinkedListUtils.print_doubly_linked_list(head)

```