from fibheap import *


class PriorityQueue:
    def __init__(self):
        self._heap = makefheap()

    def empty(self):
        return self._heap.num_nodes == 0

    def push(self, obj, priority):
        # Complexity: Theta(1)
        fheappush(self._heap, (priority, obj))

    def pop(self):
        # Complexity: O(logn)
        return fheappop(self._heap)[1]
