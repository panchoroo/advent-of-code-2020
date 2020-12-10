with open("/Users/amieeverett/Sites/advent-of-code-2020/day6/input.txt") as f:
    rows = [i.strip() for i in f.readlines()]

allAnswers = []
rowCount = 0
totalCount = 0

for row in rows:
    if(row == ""):
        # totalCount += len(set(allAnswers))
        for answer in set(allAnswers):
            if allAnswers.count(answer) == rowCount:
                totalCount += 1
        rowCount = 0
        allAnswers = []
    else:
        rowCount += 1
        for question in row:
            allAnswers.append(question)

print('totalCount', totalCount)
