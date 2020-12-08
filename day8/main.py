import FileRead
import re

f = FileRead.ReadInput(input("Filename:\n"))

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
            return accumulator, None
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
    return _, accumulator

def solution2(codes):
    jmp_nop_indexes = [codes.index(i) for i in codes if i[0] == "nop" or i[0] == "jmp"]
    i = 0
    accumulator = None
    instructions_copy = [x[:] for x in codes]
    _, accumulator = solution1(instructions_copy)
    while accumulator is None:
        instructions_copy = [x[:] for x in codes]
        opcode = instructions_copy[jmp_nop_indexes[i]]
        instructions_copy[jmp_nop_indexes[i]][0] = "jpm" if opcode[0] == "nop" else "nop"
        _, accumulator = solution1(instructions_copy)
        i += 1
    return accumulator




opcodes = parseInput(f)
accumulator, _ = solution1(opcodes)
print("solution1: {}".format(accumulator))

opcodes = parseInput(f)
accumulator = solution2(opcodes)
print("solution2: {}".format(accumulator))
