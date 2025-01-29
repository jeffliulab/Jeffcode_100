class MinHeap:
    def __init__(self):
        self.heap = []

    def push(self, val):
        """Insert an element into the heap"""
        self.heap.append(val)
        self._sift_up(len(self.heap) - 1)

    def pop(self):
        """Remove and return the top element of the heap"""
        if len(self.heap) == 0:
            raise IndexError("Heap is empty!")
        root = self.heap[0]
        # Move the last element to the root and remove the last element
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        self._sift_down(0)
        return root

    def peek(self):
        """Get the top element of the heap"""
        if len(self.heap) == 0:
            raise IndexError("Heap is empty!")
        return self.heap[0]

    def _sift_up(self, idx):
        """Adjust the heap upwards"""
        parent = (idx - 1) // 2
        while idx > 0 and self.heap[idx] < self.heap[parent]:
            # Swap the current node with its parent
            self.heap[idx], self.heap[parent] = self.heap[parent], self.heap[idx]
            idx = parent
            parent = (idx - 1) // 2

    def _sift_down(self, idx):
        """Adjust the heap downwards"""
        n = len(self.heap)
        while True:
            left = 2 * idx + 1
            right = 2 * idx + 2
            smallest = idx
            if left < n and self.heap[left] < self.heap[smallest]:
                smallest = left
            if right < n and self.heap[right] < self.heap[smallest]:
                smallest = right
            if smallest == idx:
                break
            # Swap the current node with its child node
            self.heap[idx], self.heap[smallest] = self.heap[smallest], self.heap[idx]
            idx = smallest

# Test MinHeap
heap = MinHeap()
heap.push(3)
heap.push(1)
heap.push(5)
heap.push(7)
heap.push(9)
heap.push(2)

print("Top element of the heap:", heap.peek())  # Output: 1
print("Pop the top element of the heap:", heap.pop())  # Output: 1
print("Heap after popping the top element:", heap.heap)  # Output: [2, 3, 5, 7, 9]
