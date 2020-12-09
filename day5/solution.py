with open("/Users/amieeverett/Sites/advent-of-code-2020/day5/input.txt") as f:
    rows = [i.strip() for i in f.readlines()]

# rows = ['BFFFBBFRRR', 'FFFBBBFRRR', 'BBFFBBFRLL']
# BFFFBBFRRR: row 70, column 7, seat ID 567.
# FFFBBBFRRR: row 14, column 7, seat ID 119. (it's binary, F is 0, B is 1)
# BBFFBBFRLL: row 102, column 4, seat ID 820.

def findRow(rowInfo):
    # it's binary, F is 0, B is 1)
    rowInfo = rowInfo.replace('F', '0')
    rowInfo = rowInfo.replace('B', '1')
    return int(rowInfo, 2)
    
def findColumn(columnInfo):
    columnInfo = columnInfo.replace('L', '0')
    columnInfo = columnInfo.replace('R', '1')
    return int(columnInfo, 2)

def findSeatID(rowNum, columnNum):
    # Every seat also has a unique seat ID: multiply the row by 8, then add the column. In this example, the seat has ID 44 * 8 + 5 = 357.
    return (rowNum*8) + columnNum

highestSeatID=0
for row in rows:
    rowNumber = findRow(row[:-3])
    columnNumber = findColumn(row[-3:])
    seatID = findSeatID(rowNumber, columnNumber)
    if seatID > highestSeatID:
        highestSeatID = seatID
    # print (findSeatID(rowNumber, columnNumber))
    # print ('------------------------')

# As a sanity check, look through your list of boarding passes. 
# What is the highest seat ID on a boarding pass?
print('highestSeatID = ', highestSeatID)
