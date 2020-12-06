with open('/Users/amieeverett/Sites/advent-of-code-2020/challenge1/input.txt') as f:
    expenses = [int(i.strip()) for i in f.readlines()]
print(expenses)

def findAddendsForSum(listOfAddends, summationAmount):
    while len(listOfAddends) > 0:
        potentialAddend1 = listOfAddends.pop()
        for potentialAddend2 in listOfAddends:
            if potentialAddend1 + potentialAddend2 == summationAmount:
                print('Addend 1, Addend 2:')
                print(potentialAddend1, potentialAddend2)
                print('Product of Addend 1 * Addend 2:')
                print(potentialAddend1*potentialAddend2)
                break


findAddendsForSum(expenses, 2020)
