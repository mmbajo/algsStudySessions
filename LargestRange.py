'''O(n) time | O(n) space'''


def largestRange(array):
    bestRange = []
    longestRange = 0
    hashTable = {}

    # Initialize hashTable
    for i in array:
        hashTable[i] = True

    # Iterate on every element in array
    for i in array:
        # Check if i is already visited
        if not hashTable[i]:
            continue
        hashTable[i] = False
        currRange = 1

        # Check lefts of current i
        left = i - 1
        while left in hashTable:
            hashTable[left] = False
            currRange += 1
            left -= 1

        # Check rights of current i
        right = i + 1
        while right in hashTable:
            hashTable[right] = False
            currRange += 1
            right += 1

        if currRange > longestRange:
            longestRange = currRange
            bestRange = [left + 1, right - 1]

    return bestRange
