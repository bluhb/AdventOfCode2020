import FileRead
import math

F = FileRead.ReadInput("input.txt")


def isTree(Char):
    return True if Char == "#" else False

def traverse(Slope): #[X, Y] slope
    X = 0
    Y = 0
    Trees = 0
    for i in range(0, len(F), Slope[1]):
        Line = F[i]
        if X >= len(Line):
            X = X % len(Line)
        if isTree(Line[X]):
            Trees += 1
        Y += Slope[1]
        X += Slope[0]
    return Trees

def solution1():
    Answer = traverse([3, 1])
    print("Trees for slope 3,1 is: {}".format(Answer))

def solution2():
    Slopes = [
                [1,1],
                [3,1],
                [5,1],
                [7,1],
                [1,2]
            ]
    Answers = []
    for Slope in Slopes:
        Answers.append(traverse(Slope))

    print("Product of all slopes is: {}".format(math.prod(Answers)))


solution1()
solution2()
