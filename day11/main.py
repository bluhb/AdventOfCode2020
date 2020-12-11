import FileRead

FILENAME = "input.txt"

def checkSeat1(data, row, column):
    current = data[row][column]
    change = True
    if current == "L":
        for checkRow in range(-1, 2): #2 to include 1
            for checkColumn in range(-1, 2): #2 to include 1
                if not checkRow and not checkColumn: #don't inlcude 0,0'
                    continue
                elif not change:
                    return change
                elif 0 <= row + checkRow < len(data) and 0 <= column + checkColumn < len(data[row]):
                    change &= data[row + checkRow][column + checkColumn] != "#"
                else:
                    continue
        return change

    elif current == "#":
        count = 0
        for checkRow in range(-1, 2): #2 to include 1
            for checkColumn in range(-1, 2): #2 to include 1
                if not checkRow and not checkColumn: #don't inlcude 0,0'
                    continue
                elif 0 <= row + checkRow < len(data) and 0 <= column + checkColumn < len(data[row]):
                    count += 1 if data[row + checkRow][column + checkColumn] == "#" else 0
                else:
                    continue
                if count >= 4:
                    return True
        return False

def solution1():
    f = FileRead.ReadInput(FILENAME)
    for row in range(0,len(f)):
        f[row] = list(f[row])
    oldSeats = []
    seats = f.copy()
    switch = {"L":"#", "#":"L"} #dict to switch symbols around
    working = []
    while working != seats:
        working = [x[:] for x in seats]
        for row in range(0,len(seats)):
            for column in range(0,len(seats[row])):
                current = working[row][column]
                if current != ".":
                    change = checkSeat1(working, row, column)
                    if change:
                        seats[row][column] = switch[current]
    count = sum([x.count("#") for x in seats])
    return [count]


def timeIt(func):
    import time
    t1 =time.perf_counter()
    answer = func()
    t1 = time.perf_counter() - t1
    print("Time taken by {}: {:.5f}s".format(func.__name__, t1))
    print(*answer, sep="\n")
    return t1

timeIt(solution1)
