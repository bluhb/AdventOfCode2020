import FileRead
import math

F = FileRead.ReadInput("input.txt")

def parseSeat(s):
    row = [0,127]
    seat = [0, 7]
    for i in range(0,len(s)):
        direction = s[i]
        seathalf = (seat[1] - seat[0]) / 2
        half = (row[1] - row[0]) / 2
        if direction.upper() == "F":
            row = [row[0], math.floor(row[1] - half)]
        elif direction.upper() == "B":
            row = [math.ceil(row[0] + half), row[1]]
        elif direction.upper() == "L":
            seat = [seat[0], math.floor(seat[1] - seathalf)]
        elif direction.upper() == "R":
            seat = [math.ceil(seat[0] + seathalf), seat[1]]

    return row[0], seat[0]

def solution1():
    ID = 0
    for x in F:
        row, seat = parseSeat(x)
        IDSeat = row * 8 + seat
        if IDSeat > ID:
            ID = IDSeat
    return ID

def solution2():
    IDs = []
    for x in F:
        row, seat = parseSeat(x)
        IDs.append(row * 8 + seat)
    IDs.sort()
    AllIds = []
    for i in range(0,128):
        for x in range(0,8):
            ID = i*8+x
            if IDs[0] < ID < IDs[-1]:
                AllIds.append(ID)
    Free = [x for x in AllIds if (x not in IDs)]
    for i in range(0,len(IDs) - 2):
        if IDs[i] + 1 != IDs[i+1]:
            return "your seat is {} + 1 {} {}".format(IDs[i], IDs[i-1], IDs[i+1]), Free
    return IDs, Free, AllIds

print(solution1())
print(solution2())


