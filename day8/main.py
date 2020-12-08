import FileRead
import re

f = FileRead.ReadInput("input.txt")

def parseInput(f):
    opcodes = []
    search = re.compile("^(.+) (.+)")
    for l in f:
        instruct = re.findall(search, l) # find instruction + argument number
        instruct = [y for x in instruct for y in x] #convert the nested tuple to a list
        instruct[1] = int(instruct[1]) #convert the argument to int
        instruct.append(0) #add run counter
        opcodes.append(instruct)
    return opcodes

def solution1(instructions):
    i = 0
    prevI = 0
    accumulator = 0
    while i < len(instructions):
        opcode = instructions[i][0]
        if instructions[i][2] > 0: #if the instruction was run before, terminate
            break
        instructions[i][2] += 1
        if opcode == "nop":
            prevI = i
            i += 1
        elif opcode == "acc":
            accumulator += instructions[i][1]
            prevI = i
            i += 1
        elif opcode == "jmp":
            prevI = i
            i += instructions[i][1]
    return prevI, accumulator

def solution2(codes):
    instructions_copy = [x[:] for x in codes]
    i_to_change, _ = solution1(instructions_copy)
    opcode = codes[i_to_change]
    codes[i_to_change][0] = "nop" if opcode[0] == "jmp" else "jmp"

    _, accumulator = solution1(codes) #run the code again with the changed instructions
    return accumulator

opcodes = parseInput(f)
_, accumulator = solution1(opcodes)
print("solution1: {}".format(accumulator))

opcodes = parseInput(f)
accumulator = solution2(opcodes)
print("solution2: {}".format(accumulator))
