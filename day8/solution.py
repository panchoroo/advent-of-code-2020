with open("/Users/amieeverett/Sites/advent-of-code-2020/day8/input.txt") as f:
    rows = [i.strip() for i in f.readlines()]
# with open("/Users/amieeverett/Sites/advent-of-code-2020/day8/test-input.txt") as f:
#     testRows = [i.strip() for i in f.readlines()]

def getInstruction(index, indices, accumulator, instructions):
    # print('index, indices, accumulator', index, indices, accumulator)
    if index in indices:
        return (accumulator)
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
        
        if index in range(0, len(instructions)):
            return getInstruction(index, indices, accumulator, instructions)
        elif index == len(instructions):
            print("🎯 Solution: ", accumulator)
            return (accumulator)
        else:
            return("Index Error")

# print('🎯',  getInstruction(0, [], 0, rows))

# ------------------------- Part 2 -------------------------

# Fix the program so that it terminates normally by changing exactly one jmp(to nop) or nop(to jmp). What is the value of the accumulator after the program terminates?
# when len(indices) = len(instructions) ?

# accum, length = getInstruction(0, [], 0, rows)
# print(accum, length)

def alterInstructions(instructions, oldRowIndex, newRow, oldRow):
    instructions[oldRowIndex] = newRow
    print(getInstruction(0, [], 0, instructions))
    instructions[oldRowIndex] = oldRow

for rowIndex, row in enumerate(rows):
    command, value = row.split(" ")
    if command == "nop":
        alterInstructions(rows, rowIndex, ' '.join(["jmp", value]), row)
    elif command == "jmp":
        alterInstructions(rows, rowIndex, ' '.join(["nop", value]), row)
    else:
        pass
