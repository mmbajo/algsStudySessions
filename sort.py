from typing import List


class HeapSort:
    '''
    Best case: O(nlogn) time | O(1) space
    Average case: O(nlogn) time | O(1) space
    Worst case: O(nlogn) time | O(1) space
    '''

    def sort(self, array: List[float]) -> List[float]:
        print("---------------------HeapSort--------------------------------")
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

    Note: Worst case happens if the partitioner is the min or max of the array!
    '''

    def sort(self, array: List[float]) -> List[float]:
        print("---------------------QuickSort--------------------------------")
        self.quickSortHelper(0, len(array) - 1, array)
        return array

    def quickSortHelper(self, startIdx: int, endIdx: int, array: List[float]):
        if startIdx >= endIdx:
            return
        leftIdx, rightIdx = self.threeWayPartition(startIdx, endIdx, array)
        self.quickSortHelper(startIdx, leftIdx - 1, array)
        self.quickSortHelper(rightIdx + 1, endIdx, array)

    def threeWayPartition(self, startIdx: int, endIdx: int, array: List[float]):
        partitioner = array[startIdx]
        lessIdx = startIdx
        equalIdx = startIdx
        greaterIdx = endIdx

        while equalIdx <= greaterIdx:
            if array[equalIdx] == partitioner:
                equalIdx += 1
                print('{} Increment equalIdx -> {}'.format(array, equalIdx))
            elif array[equalIdx] < partitioner:
                self.swap(equalIdx, lessIdx, array)
                equalIdx += 1
                lessIdx += 1
                print('{} Swap vals equalIdx and lessIdx! Increment equalIdx -> {} and lessIdx -> {}'
                      .format(array, equalIdx, lessIdx))
            elif array[equalIdx] > partitioner:
                self.swap(equalIdx, greaterIdx, array)
                greaterIdx -= 1
                print('{} Swap vals equalIdx and greaterIdx! Decrement greaterIdx -> {}'
                      .format(array, greaterIdx))
        return lessIdx, greaterIdx

    def swap(self, i: int, j: int, array: List[float]):
        array[i], array[j] = array[j], array[i]


class MergeSort:
    '''
    Best case: O(nlogn) time | O(nlogn) space
    Average case: O(nlogn) time | O(nlogn) space
    Worst case: O(nlogn) time | O(nlogn) space
    '''

    pass
