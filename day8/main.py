import FileRead
import re

f = FileRead.ReadInput("input.txt")

def parseInput(f):
    instructions = []
    search = re.compile("^(.+) (.+)")
    for l in f:
        instruct = re.findall(search, l) # find instruction + argument number
        instruct = [y for x in instruct for y in x] #convert the nested tuple to a list
        instruct[1] = int(instruct[1]) #convert the argument to int
        instruct.append(0) #add run counter
        instructions.append(instruct)
    return instructions

def solution1():
    global instructions
    i = 0
    prevI = 0
    accumulator = 0

    while i < len(instructions):
        opcode = instructions[i][0]
        if instructions[i][2] > 0: #if the instruction was run before, terminate
            print("terminated at {} with instructions {}".format(i, instructions[i]))
            print("change instruction {} {}".format(prevI, instructions[prevI]))
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
    print("Accumulator is {}".format(accumulator))

def solution2():
    global instructions
    instructions[210][0] = "nop" #change the last jump instruction before terminating to nop
    solution1() #run the code again with the changed instructions


instructions = parseInput(f)
solution1()
instructions = parseInput(f)
solution2()
