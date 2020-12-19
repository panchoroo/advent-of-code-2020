import sys
file = "test-input"
file = "test-input2"
file = "input"

with open("/Users/amieeverett/Sites/advent-of-code-2020/day10/"+file+".txt") as f:
    rows = [int(i.strip()) for i in f.readlines()]

rows.append(0)
rows.sort()
orderedJoltages = rows
countRuns=[1]
def differenceCounter(orderedJoltages):
    joltDiff1=1
    joltDiff3=1
    countRuns=[]
    onesCounter=1
    for index in range(0,len(orderedJoltages)-1):
        difference = orderedJoltages[index+1]-orderedJoltages[index]
        if difference == 1:
            joltDiff1 += 1
            onesCounter += 1
            if onesCounter < 3:
                countRuns.append(orderedJoltages[index])
        elif difference == 3:
            joltDiff3 += 1
            onesCounter = 1
        else:
            print('Error')
    return (joltDiff1, joltDiff3, countRuns)

jolt1, jolt3, startsOfRuns = differenceCounter(rows)
# print('startsOfRuns', startsOfRuns)

# --- Part Two ---

# print('orderedJoltages', orderedJoltages)
graph = {}
for i in orderedJoltages:
    graph[i] = []

for i in orderedJoltages:
    for j in range(1,4):
        if i+j in orderedJoltages:
            graph[i].append(i+j)

def PathCounter(node):
    if len(graph[node]) <= 1:
        return 1
    return sum([PathCounter(child) for child in graph[node]])

newSum = 1
for g in startsOfRuns:
    if len(graph[g]) > 1:
        newSum *= PathCounter(g)

print('newSum', newSum)