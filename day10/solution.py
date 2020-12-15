file = "test-input"
file = "test-input2"
file = "input"

with open("/Users/amieeverett/Sites/advent-of-code-2020/day10/"+file+".txt") as f:
    rows = [int(i.strip()) for i in f.readlines()]

# Find a chain that uses all of your adapters to connect the charging outlet to your device's built-in adapter and count the joltage differences between the charging outlet, the adapters, and your device. What is the number of 1-jolt differences multiplied by the number of 3-jolt differences?

orderedJoltages=[0]
while len(rows) > 0:
    orderedJoltages.append(min(rows))
    rows.remove(min(rows))

# print(orderedJoltages)
joltDiff1=0
joltDiff3=1
for index in range(0,len(orderedJoltages)-1):
    difference = orderedJoltages[index+1]-orderedJoltages[index]
    # print('orderedJoltages[index+1]-orderedJoltages[index]', orderedJoltages[index+1], orderedJoltages[index])
    if difference == 1:
        joltDiff1 += 1
    elif difference == 3:
        joltDiff3 += 1
    else:
        print('ruh roh')

print('joltDiff1, joltDiff3', joltDiff1, joltDiff3)
print(joltDiff1*joltDiff3)

# --- Part Two ---
