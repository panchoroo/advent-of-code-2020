with open("/Users/amieeverett/Sites/advent-of-code-2020/day8/input.txt") as f:
    rows = [i.strip() for i in f.readlines()]
with open("/Users/amieeverett/Sites/advent-of-code-2020/day8/test-input.txt") as f:
    testRows = [i.strip() for i in f.readlines()]
with open("/Users/amieeverett/Sites/advent-of-code-2020/day8/test-input2.txt") as f:
    testRows2 = [i.strip() for i in f.readlines()]

# instructions = testRows
instructions = rows

def getInstruction(index, indices, accumulator):
    # print('index, indices, accumulator', index, indices, accumulator)
    if index in indices:
        return accumulator
    else: 
        indices.append(index)
        command, value = instructions[index].split(" ")
        if command == "acc":
            accumulator += int(value)
            index += 1
        elif command == "jmp":
            index += int(value)
        else:
            index += 1
        return getInstruction(index, indices, accumulator)
    return accumulator

print('🎯',  getInstruction(0, [], 0))

# ------------------------- Part 2 -------------------------

