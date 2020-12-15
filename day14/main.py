import FileRead
import re

FILENAME = "input.txt"

def parseInput():
    f = FileRead.ReadInput(FILENAME)
    masks = {}
    mems = {}
    regFirstWord = "(\w+).+"
    regMask = ".+? = (.+)"
    regMem = "(\d+)"
    for i, x in enumerate(f):
        first = re.findall(regFirstWord, x)
        if first[0] == "mask":
            #parse mask
            mask = re.findall(regMask, x)
            masks[i] = mask[0]
        else:
            #parse mem
            locValue = re.findall(regMem, x)
            loc = locValue[0]
            value = locValue[1]
            mems[i] = {"loc":loc, "val":value}
    return masks, mems, i

def bitMask(v, m):
    v = '{0:036b}'.format(int(v))
    print(v)
    v = list(v)
    print(m)
    for i in range(0, len(m)):
        v[i] = v[i] if m[i] == "X" else m[i]
    v = ''.join(v)
    return v

def bitMask2(value, mask, currentBit, values):
    values.append(int( bitMask(value, mask) , 2 ))
    maskCopy = list(mask)
    maskCopy[currentBit] = "0" if maskCopy[currentBit] == "X" else "X"
    values.append(int( bitMask(value, ''.join(maskCopy)) , 2 ))
    maskCopy[currentBit] = "1"
    if currentBit + 1 == len(mask):
        return values
    else:
        currentBit = mask.index("X", currentBit + 1) if "X" in mask else len(mask) - 1
        return bitMask2(value, mask, currentBit, values)


def solution1():
    memory = {}
    masks, mems, maxProgramPointer = parseInput()
    currentMask = ""
    for p in range(0,maxProgramPointer + 1):
        if p in masks:
            currentMask = masks[p]
        elif p in mems:
            location = mems[p]["loc"]
            value = mems[p]["val"]
            value = bitMask(value, currentMask)
            memory[location] = int(value, 2)

    total = 0

    for _,x in memory.items():
        total += x
    return total
index = list("00000000000000000000000000000000X0XX").index("X")
print(bitMask2(26, "00000000000000000000000000000000X0XX", index, []))


# print(solution1())

