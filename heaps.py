'''
Heap Implementation
Must think about the invariants!!!!!!
Especially on while loops!!!!
'''


class MinHeap:
    def __init__(self, array):
        self.heap = self.buildHeap(array)

    def buildHeap(self, array):
        lastIdx = len(array) - 1
        lastParent = (lastIdx - 1) // 2
        for parent in reversed(range(lastParent + 1)):
            self.siftDown(parent, lastIdx, array)
        return array

    def siftDown(self, currIdx, endIdx, heap):
        childOneIdx = 2 * currIdx + 1
        while childOneIdx <= endIdx:
            tempChildTwoIdx = 2 * currIdx + 2
            childTwoIdx = tempChildTwoIdx if tempChildTwoIdx <= endIdx else -1
            if childTwoIdx != -1 and heap[childTwoIdx] < heap[childOneIdx]:
                idxToSwap = childTwoIdx
            else:
                idxToSwap = childOneIdx
            if heap[idxToSwap] < heap[currIdx]:
                self.swap(idxToSwap, currIdx, heap)
            else:
                break

    def siftUp(self, currIdx, heap):
        parentIdx = (currIdx - 1) // 2
        while currIdx > 0 and heap[parentIdx] < heap[currIdx]:
            self.swap(currIdx, parentIdx, heap)
            currIdx = parentIdx
            parentIdx = (currIdx - 1) // 2

    def peek(self):
        return self.heap[0]

    def remove(self):
        self.swap(0, len(self.heap) - 1, self.heap)
        toRemove = self.heap.pop()
        self.siftDown(0, len(self.heap) - 1, self.heap)
        return toRemove

    def insert(self, toInsert):
        self.heap.append(toInsert)
        self.siftUp(len(self.heap) - 1, self.heap)

    def swap(self, i, j, heap):
        heap[i], heap[j] = heap[j], heap[i]
