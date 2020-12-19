file = "test-input"
file = "input"

with open("/Users/amieeverett/Sites/advent-of-code-2020/day11/"+file+".txt") as f:
    rows = [(i.strip()) for i in f.readlines()]

def getAdjacentCoords(row, column):
    coords = []
    for r in range(row-1, row+2):
        for c in range(column-1, column+2):
            if r >= 0 and c >= 0 and r < len(rows) and c < len(rows[r]):
                if (not (r == row and c == column)) and (rows[r][c] != '.'):
                    coords.append((r, c))
    if len(coords) >= 4:
        return coords
    return False

def getNumOccupied(coordinates):
    neighbourCount = 0
    for coordinate in coordinates:
        neighbour = rows[coordinate[0]][coordinate[1]]
        if neighbour == '#':
            neighbourCount += 1
    return neighbourCount

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
countIterations = 1

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
            elif seatValue == '#' and numOccupied >= 4:
                changesMade = True
                newSingleRow[seatCol] = 'L'
        newRows.append("".join(newSingleRow))
    rows = newRows
    countIterations += 1

# print(countIterations)
# print(rows)
occupiedCount = 0
for r in rows:
    for x in r:
        if x == '#':
            occupiedCount += 1

print(occupiedCount)

# --- Part Two ---
