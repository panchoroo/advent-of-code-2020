file = "test-input"
file = "input"

with open("/Users/amieeverett/Sites/advent-of-code-2020/day11/"+file+".txt") as f:
    rows = [(i.strip()) for i in f.readlines()]

def getAdjacentCoords(row, column):
    if (rows[row][column] != '.'):
        # Top left, top, top right, right,
        TL = fanOut(row-1, column-1, -1, -1)
        T = fanOut(row-1, column, -1, 0)
        TR = fanOut(row-1, column+1, -1, 1)
        R = fanOut(row, column+1, 0, 1)
        # down right, down, down left, left
        DR = fanOut(row+1, column+1, 1, 1)
        D = fanOut(row+1, column, 1, 0)
        DL = fanOut(row+1, column-1, 1, -1)
        L = fanOut(row, column-1, 0, -1)
        
        possibleDirections = [TL, T, TR, R, DR, D, DL, L]
        coords = [(direction[0], direction[1]) for direction in possibleDirections if direction]
        # print('coords', coords)

        if len(coords) >= 5:
            return coords
    return False

def getNumOccupied(coordinates):
    neighbourCount = 0
    for coordinate in coordinates:
        neighbour = rows[coordinate[0]][coordinate[1]]
        if neighbour == '#':
            neighbourCount += 1
    return neighbourCount

def fanOut(startingR, startingC, rMod, cMod):
    r = startingR
    c = startingC
    while r in range(0, len(rows)) and c in range(0, len(rows[r])):
        if (rows[r][c] != '.'):
            return (r,c)
        else:
            r += rMod
            c += cMod
    return False

rowsAfterFirst= []
neighbours={}
for rowIndex, row in enumerate(rows):
    newSingleRow = list(rows[rowIndex])
    neighbours[rowIndex]= {}
    for colIndex, col in enumerate(row):
        seatVal = row[colIndex]
        if seatVal == 'L':
            newSingleRow[colIndex] = '#'
        adjecentCoordinates = getAdjacentCoords(rowIndex, colIndex)
        if adjecentCoordinates:
            neighbours[rowIndex][colIndex] = adjecentCoordinates
    rowsAfterFirst.append("".join(newSingleRow))

changesMade = True
rows = rowsAfterFirst

while changesMade == True:
    changesMade = False
    newRows = []
    for seatRow in neighbours:
        newSingleRow = list(rows[seatRow])
        for seatCol in neighbours[seatRow]:
            seatValue = rows[seatRow][seatCol]
            numOccupied = getNumOccupied(neighbours[seatRow][seatCol])
            if seatValue == 'L' and numOccupied == 0:
                changesMade = True
                newSingleRow[seatCol] = '#'
            elif seatValue == '#' and numOccupied >= 5:
                changesMade = True
                newSingleRow[seatCol] = 'L'
        newRows.append("".join(newSingleRow))
    rows = newRows

occupiedCount = 0
for r in rows:
    for x in r:
        if x == '#':
            occupiedCount += 1

print(occupiedCount)
