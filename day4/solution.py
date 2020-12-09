import re

with open("/Users/amieeverett/Sites/advent-of-code-2020/day4/input.txt") as f:
    rows = [i.strip() for i in f.readlines()]

# Count the number of valid passports - those that have all required fields. 
# Treat cid as optional. 
# In your batch file, how many passports are valid?

def setBlankPassport():
    passPortData = {
        "byr": False, 
        "iyr": False, 
        "eyr": False, 
        "hgt": False, 
        "hcl": False, 
        "ecl": False, 
        "pid": False, 
    }
    return passPortData

def checkPassport(passport):
    for infoItem in passport:
        if(not passport[infoItem]):
            return False
    return True

def checkPassportItemValidity(passportIndex, passportItem):
    conditionsMet = False
    if passportIndex == 'byr':
        conditionsMet = (1920 <= int(passportItem) <= 2002)
    elif passportIndex == 'iyr':
        conditionsMet = (2010 <= int(passportItem) <= 2020)
    elif passportIndex == 'eyr':
        conditionsMet = (2020 <= int(passportItem) <= 2030)
    elif passportIndex == 'hgt':
        if 'cm' in passportItem:
            conditionsMet = (150 <= int(passportItem[:-2]) <= 193)
        elif 'in' in passportItem:
            conditionsMet = (59 <= int(passportItem[:-2]) <= 76)
    elif passportIndex == 'hcl':
        pattern = re.compile("^#{1}[a-f|0-9]{6}$")
        conditionsMet = pattern.match(passportItem)
    elif passportIndex == 'ecl':
        eyeColours = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
        conditionsMet = passportItem in eyeColours
    elif passportIndex == 'pid':
        pattern = re.compile("^\d{9}$")
        conditionsMet = pattern.match(passportItem)
    else:
        print('Error: invalid passportIndex', passportIndex)
    # if (conditionsMet):
    #     print('valid', passportIndex, passportItem)
    # else:
    #     print('invalid', passportIndex, passportItem)
    return conditionsMet

numberOfValidPassports = 0
passPortData = setBlankPassport()
for row in rows:
    # print(row)
    if(row == ""):
        if(checkPassport(passPortData)):
            numberOfValidPassports += 1
        passPortData = setBlankPassport()
        # print("------------------------------------------------------------")
    else:
        items = str(row).split(" ")
        for item in items:
            index, passportItem = item.split(":")
            if(index in passPortData.keys()):
                passPortData[index] = checkPassportItemValidity(index, passportItem)

print("numberOfValidPassports", numberOfValidPassports)

# 215 is too low
# 218 is too high
# 216 is the answer, but why?
# because the way this works it needs 2 blank lines after the last input or it won't fully process the last one

# -------------------- Part Two -----------------------------
# byr(Birth Year) - four digits
# at least 1920 and at most 2002.
# iyr(Issue Year) - four digits
# at least 2010 and at most 2020.
# eyr(Expiration Year) - four digits
# at least 2020 and at most 2030.
# hgt(Height) - a number followed by either cm or in:
# If cm, the number must be at least 150 and at most 193.
# If in, the number must be at least 59 and at most 76.
# hcl(Hair Color) - a  # followed by exactly six characters 0-9 or a-f.
# ecl(Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
# pid(Passport ID) - a nine-digit number, including leading zeroes.
# cid(Country ID) - ignored, missing or not.

# Your job is to count the passports where all required fields are both present and valid according to the above rules. Here are some example values:
