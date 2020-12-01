FileName = "input.txt"
Sum = 2020

def ReadInput():
    F = open(FileName)
    Input = []
    for Line in F:
        Input.append(int(Line.strip()))
    return Input

def FindSum(Input, Sum):
    for X in Input:
        for Y in Input:
            if (X + Y) == Sum:
                return X, Y, X * Y

def FindSum3(Input, Sum):
    for X in Input:
        for Y in Input:
            for Z in Input:
                if (X + Y + Z) == Sum:
                    return X, Y, Z, X*Y*Z

def Solution1():
    print(FindSum(ReadInput(), Sum))

def Solution2():
    print(FindSum3(ReadInput(), Sum))


Solution1()
Solution2()
