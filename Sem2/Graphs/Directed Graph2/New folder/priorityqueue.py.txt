class PriorityQueue:
    def __init__(self):
        self._values = {}

    def empty(self):
        return len(self._values) == 0

    def push(self, obj, priority):
        self._values[obj] = priority

    def pop(self):
        topPriority = None
        topObject = None
        for obj in self._values.keys():
            objPriority = self._values[obj]
            if topPriority is None or topPriority > objPriority:
                topPriority = objPriority
                topObject = obj
        del self._values[topObject]
        return topObject