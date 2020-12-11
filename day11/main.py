import FileRead

FILENAME = "input.txt"

def checkSeat1(data, row, column): #check neighbours
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

#check line of sight
def checkSeat2(current, direction, data):
    """
    current = [row, column] coordinates
    direction = lu(left up) u(up) ru(right up) l(left) r(right) ld(left down) d(down) rd(right down)
    data = the seats
    """
    directions = ["u", "ru", "r", "rd", "d", "ld", "l", "lu"]

    #add direction to current position
    current[0] += -1 if "u" in direction else 0
    current[0] += 1 if "d" in direction else 0
    current[1] += 1 if "r" in direction else 0
    current[1] += -1 if "l" in direction else 0

    #check if new current is still in the raster
    if not (0 <= current[0] < len(data) and 0 <= current[1] < len(data[0])):
        return 0
    elif  data[current[0]][current[1]] == "#": #if occupied return 1
        return 1
    elif data[current[0]][current[1]] == "L": #if empty seat, return 0
        return 0
    elif data[current[0]][current[1]] == ".": #if no seat, call function again to check next position
        if direction in directions:
            return checkSeat2(current, direction, data)
        else:
            ValueError("unknown direction")

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

def solution2():
    f = FileRead.ReadInput(FILENAME)
    directions = ["u", "ru", "r", "rd", "d", "ld", "l", "lu"]
    data = [list(x) for x in f]
    working = []

    while working != data:
        working = [x[:] for x in data]
        for row in range(0,len(data)):
            for column in range(0,len(data[0])):
                occupiedSeats = 0

                if working[row][column] == "#":
                    for direction in directions:
                        occupiedSeats += checkSeat2([row, column], direction, working)
                        if occupiedSeats >= 5:
                            data[row][column] = "L"
                            break

                elif working[row][column] == "L":
                    for direction in directions:
                        occupiedSeats += checkSeat2([row, column], direction, working)
                        if occupiedSeats > 0:
                            break
                    if occupiedSeats == 0:
                        data[row][column] = "#"

    return [sum([x.count("#") for x in data])]



def timeIt(func):
    import time
    print("Running {}".format(func.__name__))
    t1 =time.perf_counter()
    answer = func()
    t1 = time.perf_counter() - t1
    print("Time taken by {}: {:.5f}s".format(func.__name__, t1))
    print(*answer, sep="\n")
    print("")
    return t1

t1 = timeIt(solution1)
t2 = timeIt(solution2)
print("Total time is {}s".format(t1 + t2))
