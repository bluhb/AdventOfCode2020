import FileRead

FILENAME = "input.txt"

def solve(endNumber):
    f = FileRead.ReadInput(FILENAME)
    data = [int(x) for x in f[0].split(",")]
    lastNumber = data[-1]
    offset = 0
    mem = {v:k + 1 for k,v in enumerate(data[:-1])}
    print(mem)
    for i in range(len(data) + 1,endNumber + 1):
        nextNumber = mem.get(lastNumber, 0)
        if nextNumber:
            nextNumber = i - 1 - nextNumber
        mem[lastNumber] = i - 1
        lastNumber = nextNumber
    return lastNumber

def solution1():
    print(solve(2020))

def solution2():
    print(solve(30000000))

solution1()
solution2()
