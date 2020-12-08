with open('/Users/amieeverett/Sites/advent-of-code-2020/day3/input.txt') as f:
    rows = [i.strip() for i in f.readlines()]

def numberOfTreesFinder(mapOfRows, slopeX, slopeY):
    numberOfTrees=0
    index=0
    rowCount=0
    for row in mapOfRows:
        if(rowCount % slopeY == 0):
            if (row[index] == '#'):
                numberOfTrees += 1

            if index + slopeX > len(row) - 1:
                index -= len(row) - slopeX
            else:
                index += slopeX
        rowCount += 1
    return numberOfTrees

# Right 1, down 1.
# Right 3, down 1. (This is the slope you already checked.)
# Right 5, down 1.
# Right 7, down 1.
# Right 1, down 2.

# print(numberOfTreesFinder(rows, 1, 1))
# print(numberOfTreesFinder(rows, 3, 1))
# print(numberOfTreesFinder(rows, 5, 1))
# print(numberOfTreesFinder(rows, 7, 1))
# print(numberOfTreesFinder(rows, 1, 2))

print(numberOfTreesFinder(rows, 1, 1)*numberOfTreesFinder(rows, 3, 1)*numberOfTreesFinder(rows, 5, 1)*numberOfTreesFinder(rows, 7, 1)*numberOfTreesFinder(rows, 1, 2))
