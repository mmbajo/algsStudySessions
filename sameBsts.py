# O(n^2) time | O(n^2) space
# Where n is equal to the length of array
from typing import List


def sameBsts(arrayOne: List[float], arrayTwo: List[float]) -> bool:
    if len(arrayOne) == 0 and len(arrayTwo) == 0:
        return True

    if len(arrayOne) != len(arrayTwo):
        return False

    if arrayOne[0] != arrayTwo[0]:
        return False

    leftBstOne = getLeftBst(arrayOne)
    rightBstOne = getRightBst(arrayOne)
    leftBstTwo = getLeftBst(arrayTwo)
    rightBstTwo = getRightBst(arrayTwo)

    return sameBsts(leftBstOne, leftBstTwo) and sameBsts(rightBstOne, rightBstTwo)


def getLeftBst(array: List[float]):
    cache = []
    for i in range(1, len(array)):
        if array[i] < array[0]:
            cache.append(array[i])
    return cache


def getRightBst(array: List[float]):
    cache = []
    for i in range(1, len(array)):
        if array[0] <= array[i]:
            cache.append(array[i])
    return cache
