# file = "test-input"
# currentPreamble=5
file = "input"
currentPreamble=25

with open("/Users/amieeverett/Sites/advent-of-code-2020/day9/"+file+".txt") as f:
    rows = [int(i.strip()) for i in f.readlines()]

def isValidSum(preamble, potentialSum, subset):
    for potentialAddend1 in subset:
        potentialAddend2 = potentialSum - potentialAddend1
        if potentialAddend2 != potentialAddend1 and potentialAddend2 in subset:
            return False
    return potentialSum

def sol1(rows):
    for rowIndex, testNumber in enumerate(rows):
        if rowIndex >= currentPreamble:
            solution = isValidSum(currentPreamble, testNumber, rows[rowIndex-currentPreamble:rowIndex])
            if solution:
                return solution

# The first step of attacking the weakness in the XMAS data is to find the first number in the list(after the preamble) which is not the sum of two of the 25 numbers before it. What is the first number that does not have this property?

print('solution 1 = ', sol1(rows))

# --- Part Two ---
# The final step in breaking the XMAS encryption relies on the invalid number you just found: you must find a contiguous set of at least two numbers in your list which sum to the invalid number from step 1.

# In this list, adding up all of the numbers from 15 through 40 produces the invalid number from step 1, 127. (Of course, the contiguous set of numbers in your actual list might be much longer.)

# To find the encryption weakness, add together the smallest and largest number in this contiguous range
# in this example, these are 15 and 47, producing 62.

# What is the encryption weakness in your XMAS-encrypted list of numbers?

def findContiguousSum(part1Sol, startIndex, rows):
    sumList = []
    currentIndex = startIndex
    while currentIndex in range(1, len(rows)):
        if sum(sumList) == part1Sol and len(sumList) > 1:
            return sumList
        elif sum(sumList) >= part1Sol:
            return False
        else:
            sumList.append(rows[currentIndex])
            currentIndex += 1
    return False

for rowIndex, testNumber in enumerate(rows):
    sol2 = findContiguousSum(sol1(rows), rowIndex, rows)
    if sol2:
        print('solution 2 = ', min(sol2) + max(sol2))
