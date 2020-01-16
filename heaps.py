'''
Heap Implementation
'''


class MinHeap:
    def __init__(self, array):
        self.heap = self.buildHeap(array)

    def buildHeap(self, array):
        pass

    def siftDown(self, currIdx, endIdx, heap):
        pass

    def siftUp(self, currIdx, heap):
        pass

    def peek(self):
        return self.heap[0]

    def remove(self):
        self.swap(0, len(self.heap) - 1, self.heap)
        toRemove = self.heap.pop()
        self.siftDown(0, len(self.heap) - 1, self.heap)
        return toRemove

    def insert(self, toInsert):
        pass

    def swap(self, i, j, heap):
        heap[i], heap[j] = heap[j], heap[i]
