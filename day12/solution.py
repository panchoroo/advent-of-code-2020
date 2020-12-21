file = "test-input"
file = "input"

with open("/Users/amieeverett/Sites/advent-of-code-2020/day12/"+file+".txt") as f:
    rows = [(i.strip()) for i in f.readlines()]

dirs = ['N', 'E', 'S', 'W']
currentDir = 1
# These now refer to the waypoint
xVal = 10
yVal = 1
xShipVal = 0
yShipVal = 0

for row in rows:
    instruction = row[:1]
    value = int(row[1:])

    if instruction == 'F':
        xShipVal += value*xVal
        yShipVal += value*yVal

    elif instruction == 'N':
        yVal += value
    elif instruction == 'E':
        xVal += value
    elif instruction == 'S':
        yVal -= value
    elif instruction == 'W':
        xVal -= value
    else:
        if value == 180:
            xVal *= -1
            yVal *= -1
        elif row == 'R90' or row == 'L270':
            # b, -a
            newX = yVal
            yVal = -xVal
            xVal = newX
        elif row == 'R270' or row == 'L90':
            # -b, a
            newY = xVal
            xVal = -yVal
            yVal = newY
        else:
            print('Eeerror', row)

if xShipVal < 0:
    xShipVal *= -1
if yShipVal < 0:
    yShipVal *= -1
print('Manhattan distance of the ship = ', xShipVal + yShipVal)
