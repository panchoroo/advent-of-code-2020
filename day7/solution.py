with open("/Users/amieeverett/Sites/advent-of-code-2020/day7/input.txt") as f:
    rows = [i.strip() for i in f.readlines()]
with open("/Users/amieeverett/Sites/advent-of-code-2020/day7/test-input.txt") as f:
    testRows = [i.strip() for i in f.readlines()]
with open("/Users/amieeverett/Sites/advent-of-code-2020/day7/test-input2.txt") as f:
    testRows2 = [i.strip() for i in f.readlines()]

# You have a shiny gold bag. If you wanted to carry it in at least one other bag, how many different bag colors would be valid for the outermost bag? (In other words: how many colors can, eventually, contain at least one shiny gold bag?)
# How many bag colors can eventually contain at least one shiny gold bag? (The list of rules is quite long; make sure you get all of it.)

def goldDigger(bagsToCheck, innerBagColour):
    bagsWithGold=[]
    for entry in bagsToCheck:
        if innerBagColour in bagsToCheck[entry]:
            bagsWithGold.append(entry)
    return bagsWithGold

def bagCounter(colour, multiplier, bagsList):
    bagCount = multiplier
    if colour in bagsList.keys():
        for item in bagsList[colour]:
            print('item/colour, new multiplier', item, bagsList[colour][item])
            bagCount += multiplier * \
                bagCounter(item, bagsList[colour][item], bagsList)
            print('bagCount after else', bagCount)
    print('---------------------------')
    return bagCount

nestedBags={}
solutionBags=[]
for row in rows:
# for row in testRows:
# for row in testRows2:
    outerBag, innerBags = row.split(' bags contain ')
    for item in innerBags[:-1].split(', '):
        itemKey = ' '.join(item.split(' ')[1: -1])
        if itemKey != 'other':
            item = int(' '.join(item.split(' ')[:1]))
            if outerBag not in nestedBags.keys():
                nestedBags[outerBag] = {itemKey: item}
            else:
                nestedBags[outerBag][itemKey] = item

solutionBags = goldDigger(nestedBags, 'shiny gold')
for solution in solutionBags:
    solutionBags += goldDigger(nestedBags, solution)
    
# print('solutionBags', solutionBags)
# print (len(set(solutionBags)))

# ------------------------- Part 2 -------------------------
# How many individual bags are required inside your single shiny gold bag?

colour = 'shiny gold'
for item in nestedBags[colour]:
    print('🎯', bagCounter(item, nestedBags[colour][item], nestedBags))
