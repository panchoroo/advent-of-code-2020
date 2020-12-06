with open('/Users/amieeverett/Sites/advent-of-code-2020/challenge1/input.txt') as f:
    expenses = [int(i.strip()) for i in f.readlines()]
print(expenses)

while len(expenses) > 0:
    potentialExpense = expenses.pop()
    for expense in expenses:
        if potentialExpense + expense == 2020:
            print('solution')
            print(potentialExpense, expense)
            print(potentialExpense*expense)
            break
