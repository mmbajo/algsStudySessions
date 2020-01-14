def subarraySort(array):
    minNotSorted = float('inf')
    maxNotSorted = float('-inf')
    for i in range(len(array)):
        currNum = array[i]
        if isNotSorted(i, currNum, array):
            minNotSorted = min(currNum, minNotSorted)
            maxNotSorted = max(currNum, maxNotSorted)

    if maxNotSorted == float('-inf'):
        return [-1, -1]

    lt = 0
    while array[lt] < minNotSorted:
        lt += 1
    gt = len(array) - 1
    while array[gt] > maxNotSorted:
        gt -= 1
    return [lt, gt]


def isNotSorted(i, currNum, array):
    if i == 0:
        return currNum > array[i + 1]
    if i == len(array) - 1:
        return currNum < array[i - 1]
    return (currNum > array[i + 1]) or (currNum < array[i - 1])
