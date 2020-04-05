'''
O(n*m) time and O(n*m) space
'''


def zigzagTraverse(array):
    # Declare boundaries
    width = len(array[0])
    height = len(array)

    # Initialize values
    goingDown = True
    row, col = 0, 0

    # The output
    zigzag = []

    # Don't stop if inbounds
    while row < height and col < width:
        zigzag.append(array[row][col])

        if goingDown:
            if col == 0 or row == height - 1:
                goingDown = False
                if row == height - 1:
                    col += 1
                else:
                    row += 1
            else:
                row += 1
                col -= 1
        else:  # goingUp!
            if row == 0 or col == width - 1:
                goingDown = True
                if col == width - 1:
                    row += 1
                else:
                    col += 1
            else:
                row -= 1
                col += 1

    return zigzag
