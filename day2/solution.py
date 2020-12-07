# select lines and hit Shift + Enter to run them
# use exit() if python terminal breaks in vscode:
# https: // stackoverflow.com/questions/51540391/invalid-syntax-error-when-running-python-from-inside-visual-studio-code

with open('/Users/amieeverett/Sites/advent-of-code-2020/day2/input.txt') as f:
    passwords = [i.strip() for i in f.readlines()]

# How many passwords are valid according to their policies?
# min/max and letter to test for
validPasswords = 0
for passwordInfo in passwords:
    info, password = str(passwordInfo).split(':')
    numberRange, letter = info.split(' ')
    minRange, maxRange = str(numberRange).split('-')
    if int(minRange) <= password.count(letter) <= int(maxRange):
        validPasswords += 1

print('number of valid passwords is:', validPasswords)
