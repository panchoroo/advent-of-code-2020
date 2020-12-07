with open('/Users/amieeverett/Sites/advent-of-code-2020/challenge1/input.txt') as f:
    expenses = [int(i.strip()) for i in f.readlines()]
print(expenses)

def findAddendsForSum(listOfAddends, summationAmount):
    while len(listOfAddends) > 0:
        potentialAddend1 = listOfAddends.pop()
        for potentialAddend2 in listOfAddends:
            if potentialAddend1 + potentialAddend2 == summationAmount:
                print('Addend 1, Addend 2:', potentialAddend1, potentialAddend2)
                return(potentialAddend1*potentialAddend2)

# Part One solution:
# findAddendsForSum(expenses, 2020)

# Part Two:
#  For each # in the list, pop it off, subtract from 2020, then see if two other numbers add up to that
while len(expenses) > 0:
    potentialAddend3 = expenses.pop()
    addendsForSum = findAddendsForSum(expenses.copy(), 2020 - potentialAddend3)
    if (addendsForSum):
        print('potentialAddend3 is:', potentialAddend3)
        print('addendsForSum returned:', addendsForSum)
        print('Product of all 3 is:', potentialAddend3*addendsForSum)
