with open("/Users/amieeverett/Sites/advent-of-code-2020/day4/input.txt") as f:
    rows = [i.strip() for i in f.readlines()]

# Count the number of valid passports - those that have all required fields. 
# Treat cid as optional. 
# In your batch file, how many passports are valid?

# byr(Birth Year)
# iyr(Issue Year)
# eyr(Expiration Year)
# hgt(Height)
# hcl(Hair Color)
# ecl(Eye Color)
# pid(Passport ID)
# cid(Country ID)

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

numberOfValidPassports = 0
passPortData = setBlankPassport()
for row in rows:
    print(row)
    if(row == ""):
        if(checkPassport(passPortData)):
            numberOfValidPassports += 1
        else:
            print("passPortData", passPortData)
            print("✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨")
        passPortData = setBlankPassport()
        print("------------------------------------------------------------")
    else:
        items = str(row).split(" ")
        for item in items:
            index = item.split(":")[0]
            if(index in passPortData.keys()):
                passPortData[index] = True
            # elif(index == 'cid'):
            #     passPortData['pid'] = True
                # treat CID and PID as interchangeable, this gave 218 as the answer

print("numberOfValidPassports", numberOfValidPassports)
# 215 is too low
# 218 is too high
# 216 is the answer, but why?
