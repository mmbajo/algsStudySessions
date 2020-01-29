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


class MergeSort1:
    '''
    Best case: O(nlogn) time | O(nlogn) space
    Average case: O(nlogn) time | O(nlogn) space
    Worst case: O(nlogn) time | O(nlogn) space
    '''

    def sort(self, array: List[float]) -> List[float]:
        print("---------------------MergeSort--------------------------------")
        return self.mergeSort(array)

    def mergeSort(self, array: List[float]) -> List[float]:
        if len(array) <= 1:
            return array
        middleIdx = len(array) // 2
        leftSorted = self.mergeSort(array[:middleIdx])
        rightSorted = self.mergeSort(array[middleIdx:])
        sortedArray = self.mergeSortedArray(leftSorted, rightSorted)
        print('{} middleIdx -> {}'.format(sortedArray, middleIdx))
        return sortedArray

    def mergeSortedArray(self,
                         leftArray: List[float],
                         rightArray: List[float]) -> List[float]:
        sortedArray = [None] * (len(leftArray) + len(rightArray))
        i = j = k = 0
        while i < len(leftArray) and j < len(rightArray):
            if leftArray[i] <= rightArray[j]:
                sortedArray[k] = leftArray[i]
                i += 1
            elif leftArray[i] > rightArray[j]:
                sortedArray[k] = rightArray[j]
                j += 1
            k += 1

        while i < len(leftArray):
            sortedArray[k] = leftArray[i]
            i += 1
            k += 1

        while j < len(rightArray):
            sortedArray[k] = rightArray[j]
            j += 1
            k += 1
        return sortedArray


class MergeSort2:
    '''
    Best case: O(nlogn) time | O(n) space
    Average case: O(nlogn) time | O(n) space
    Worst case: O(nlogn) time | O(n) space
    In this version of merge sort we use an auxiliarry array to sort
    the main array in place.
    Damn! This is very difficult to grasp!!!
    '''

    def sort(self, array: List[float]) -> List[float]:
        print("---------------------MergeSortv2------------------------------")
        return self.mergeSort(array)

    def mergeSort(self, array: List[float]) -> List[float]:
        if len(array) <= 1:
            return array
        auxArray = array[:]
        self.mergeSortHelper(array, 0, len(array) - 1, auxArray)
        return array

    def mergeSortHelper(self,
                        mainArray: List[float],
                        startIdx: int,
                        endIdx: int,
                        auxArray: List[float]):
        if startIdx == endIdx:
            return
        middleIdx = (startIdx + endIdx) // 2
        self.mergeSortHelper(auxArray, startIdx, middleIdx, mainArray)
        self.mergeSortHelper(auxArray, middleIdx + 1, endIdx, mainArray)
        self.doMerge(mainArray, startIdx, middleIdx, endIdx, auxArray)
        print('{} middleIdx -> {}'.format(mainArray, middleIdx))

    def doMerge(self,
                mainArray: List[float],
                startIdx: int,
                middleIdx: int,
                endIdx: int,
                auxArray: List[float]):
        i = startIdx
        k = startIdx
        j = middleIdx + 1
        while i <= middleIdx and j <= endIdx:
            if auxArray[i] <= auxArray[j]:
                mainArray[k] = auxArray[i]
                i += 1
            elif auxArray[i] > auxArray[j]:
                mainArray[k] = auxArray[j]
                j += 1
            k += 1

        while i <= middleIdx:
            mainArray[k] = auxArray[i]
            i += 1
            k += 1

        while j <= endIdx:
            mainArray[k] = auxArray[j]
            j += 1
            k += 1


class SelectionSort:
    '''
    For every index of the array, finde the smallest from index to end
    Best case: O(n^2) time | O(1) space
    Average case: O(n^2) time | O(1) space
    Worst case: O(n^2) time | O(1) space
    '''

    def sort(self, array: List[float]) -> List[float]:
        print("---------------------SelectionSort----------------------------")
        lastIdx = len(array) - 1
        currIdx = 0
        while currIdx < lastIdx:
            print('{} middleIdx -> {}'.format(array, currIdx))
            smallestIdx = currIdx
            for i in range(currIdx + 1, lastIdx + 1):
                if array[i] < array[smallestIdx]:
                    smallestIdx = i
            self.swap(currIdx, smallestIdx, array)
            currIdx += 1
        return array

    def swap(self, i: int, j: int, array: List[float]):
        array[i], array[j] = array[j], array[i]
