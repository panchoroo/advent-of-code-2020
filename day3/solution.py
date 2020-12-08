# select lines and hit Shift + Enter to run them
# use exit() if python terminal breaks in vscode:
# https: // stackoverflow.com/questions/51540391/invalid-syntax-error-when-running-python-from-inside-visual-studio-code

with open('/Users/amieeverett/Sites/advent-of-code-2020/day3/input.txt') as f:
    rows = [i.strip() for i in f.readlines()]

numberOfTrees=0
index=0
for row in rows:
    if (row[index] == '#'):
        numberOfTrees += 1

    if index + 3 > len(row) - 1:
        index -= len(row) - 3
    else:
        index += 3

print('numberOfTrees', numberOfTrees)
