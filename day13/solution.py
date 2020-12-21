file = "test-input"
file = "input"

with open("/Users/amieeverett/Sites/advent-of-code-2020/day13/"+file+".txt") as f:
    rows = [(i.strip()) for i in f.readlines()]

estimate = int(rows[0])
buses = [int(x) for x in rows[1].split(',') if x != 'x'] 
print(buses)
minutes = 0
busFound = False

while busFound == False:
    for bus in buses:
        if (estimate+minutes) % bus == 0:
            busFound = True
            print('This is your bus! ', minutes*bus)
    minutes += 1
