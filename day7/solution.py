with open("/Users/amieeverett/Sites/advent-of-code-2020/day7/input.txt") as f:
    rows = [i.strip() for i in f.readlines()]
# with open("/Users/amieeverett/Sites/advent-of-code-2020/day7/input2.txt") as f:
#     rows2 = [i.strip() for i in f.readlines()]

# You have a shiny gold bag. If you wanted to carry it in at least one other bag, how many different bag colors would be valid for the outermost bag? (In other words: how many colors can, eventually, contain at least one shiny gold bag?)
# How many bag colors can eventually contain at least one shiny gold bag? (The list of rules is quite long; make sure you get all of it.)

def goldDigger(bagsToCheck, innerBagColour):
    bagsWithGold=[]
    for entry in bagsToCheck:
        if innerBagColour in bagsToCheck[entry]:
            print('entry', entry)
            bagsWithGold.append(entry)
    return bagsWithGold

nestedBags={}
solutionBags=[]
for row in rows:
# for row in rows2:
    outerBag, innerBags = row.split(' bags contain ')
    for item in innerBags[:-1].split(', '):
        item = ' '.join(item.split(' ')[1: -1])
        if outerBag not in nestedBags.keys():
            if item != 'other':
                nestedBags[outerBag] = [item] 
        elif outerBag != 'shiny gold':
            nestedBags[outerBag].append(item)

solutionBags = goldDigger(nestedBags, 'shiny gold')
for solution in solutionBags:
    solutionBags += goldDigger(nestedBags, solution)
    
print('solutionBags', solutionBags)
print (len(set(solutionBags)))
