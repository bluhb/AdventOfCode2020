import FileRead

F = FileRead.readInput("input.txt")

def parseInput(F):
    ParsedF = []
    for X in F:
        Lowerbound = int(X[0:X.find("-")])
        Upperbound = int(X[X.find("-")+1:X.find(" ")])
        Letter = X[X.find(" ")+1:X.find(":")]
        Password = X[X.find(":")+2:]
        ParsedF.append([Lowerbound,
            Upperbound,
            Letter,
            Password])
    return ParsedF

def checkPassword(C):
    if C[0] <= C[3].count(C[2]) <= C[1]:
        return True
    else:
        return False

def checkPassword2(C):
    if C[3][C[0]-1] == C[2] or C[3][C[1]-1] == C[2]:
        if not (C[3][C[0]-1] == C[2] and C[3][C[1]-1] == C[2]):
            return True
        else:
            return False
    else:
        return False

def solution1():
    ParsedF = parseInput(F)
    Amount = 0
    for Pass in ParsedF:
        Check = checkPassword(Pass)
        if Check:
            Amount += 1
    print("Good passwords: {}".format(Amount))

def solution2():
    ParsedF = parseInput(F)
    Amount = 0
    for Pass in ParsedF:
        Check = checkPassword2(Pass)
        if Check:
            Amount += 1
    print("Good passwords: {}".format(Amount))

solution1()
solution2()
