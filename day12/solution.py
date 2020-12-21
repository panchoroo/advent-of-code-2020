file = "test-input"
file = "input"

with open("/Users/amieeverett/Sites/advent-of-code-2020/day12/"+file+".txt") as f:
    rows = [(i.strip()) for i in f.readlines()]


dirs = ['N', 'E', 'S', 'W']
currentDir = 1
xVal = 0
yVal = 0

for row in rows:
    instruction = row[:1]
    value = int(row[1:])

    if instruction == 'F':
        instruction = dirs[currentDir]

    if instruction == 'N':
        yVal += value
    elif instruction == 'E':
        xVal += value
    elif instruction == 'S':
        yVal -= value
    elif instruction == 'W':
        xVal -= value
    elif instruction == 'R':
        currentDir += int(value/90)
        print(currentDir)
    elif instruction == 'L':
        currentDir -= int(value/90)

    if currentDir not in range(0, 4):
        if currentDir < 4:
            currentDir += 4
        else:
            currentDir -= 4

if xVal < 0:
    xVal *= -1
if yVal < 0:
    yVal *= -1
print('Manhattan distance = ', xVal + yVal)
