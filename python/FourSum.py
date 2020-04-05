'''
Average Case: Time -> O(n^2) Space -> O(n^2)
Worst Case: Time -> O(n^3) Space -> O(n^2)
'''


def fourSum(array, targetSum):
    prevSums = {}
    quads = []
    for i in range(len(array) - 1):
        for j in range(i + 1, len(array)):
            potentialMatch = targetSum - (array[i] + array[j])
            if potentialMatch in prevSums:
                for pair in prevSums[potentialMatch]:
                    quads.append(pair + [array[i], array[j]])

        for k in range(0, i):
            currSum = array[i] + array[k]
            if currSum in prevSums:
                prevSums[currSum] += [[array[i], array[k]]]
            else:
                prevSums[currSum] = [[array[i], array[k]]]
    return quads
