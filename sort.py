from typing import List


class HeapSort:
    '''
    Best case: O(nlogn) time | O(1) space
    Average case: O(nlogn) time | O(1) space
    Worst case: O(nlogn) time | O(1) space
    '''

    def sort(self, array: List[float]) -> List[float]:
        self.buildMaxHeap(array)
        for endIdx in reversed(range(1, len(array))):
            self.swap(0, endIdx, array)
            print('{} Swap'.format(array))
            self.siftDown(0, endIdx - 1, array)  # Last elem is alrdy sorted!!
            print('{} SiftDown'.format(array))
        return array

    def buildMaxHeap(self, array: List[float]):
        lastIdx = len(array) - 1
        lastParentIdx = (lastIdx - 1) // 2
        for i in reversed(range(lastParentIdx + 1)):
            self.siftDown(i, lastIdx, array)

    def siftDown(self, currIdx: int, endIdx: int, array: List[float]):
        childOneIdx = 2 * currIdx + 1
        while childOneIdx <= endIdx:
            childTwoIdx = 2 * currIdx + 2 if 2 * currIdx + 2 <= endIdx else -1
            if childTwoIdx != -1 and array[childTwoIdx] > array[childOneIdx]:
                idxToSwap = childTwoIdx
            else:
                idxToSwap = childOneIdx
            if array[idxToSwap] > array[currIdx]:
                self.swap(idxToSwap, currIdx, array)
                currIdx = idxToSwap
                childOneIdx = 2 * currIdx + 1
            else:
                return

    def swap(self, i: int, j: int, array: List[float]):
        array[i], array[j] = array[j], array[i]


class QuickSort:
    '''
    Best case: O(nlogn) time | O(1) space
    Average case: O(nlogn) time | O(1) space
    Worst case: O(n^2) time | O(1) space
    '''
    pass
