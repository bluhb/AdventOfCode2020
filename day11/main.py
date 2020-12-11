import FileRead
import time
import pygame as pg

FILENAME = "input.txt"
VISUALIZE = input("Want to see an animation? y/n: ").upper() == "y".upper()
SCALE = 10

def initVisual():
    pg.init()
    temp = FileRead.ReadInput(FILENAME)
    size = [len(temp) * SCALE + 15, (len(temp[0]) * SCALE + 60)]
    screen = pg.display.set_mode(size)
    screen.fill((255,255,255))
    font = pg.font.Font('freesansbold.ttf', 32)
    return screen, font

def visualize(data):
    global screen, font
    for xi, x in enumerate(data):
        for yi, y in enumerate(x):
            if y == "#":
                color = (255,0,0)
            elif y == "L":
                color = (0,255,0)
            elif y == ".":
                color = (255,255,255)
            pg.draw.circle(screen, color, (xi*SCALE + 10,yi*SCALE + 50), SCALE / 2)
    seated = sum([x.count("#") for x in data])
    text = font.render(str(seated), True, (255,0,0), (255,255,255))
    textRect = text.get_rect()
    screen.blit(text, textRect)
    pg.display.flip()

    time.sleep(1/60)

def checkSeat1(data, row, column): #check neighbours
    current = data[row][column]
    change = True
    rowLength = len(data) #save lengths as speed improvement, faster than running len() in the loop
    columnLength = len(data[0])
    if current == "L":
        for checkRow in range(-1, 2): #2 to include 1
            for checkColumn in range(-1, 2): #2 to include 1
                if not checkRow and not checkColumn: #don't inlcude 0,0'
                    pass
                elif 0 <= row + checkRow < rowLength and 0 <= column + checkColumn < columnLength:
                    change &= data[row + checkRow][column + checkColumn] != "#"
                else:
                    pass
                if not change:
                    return change
        return change

    elif current == "#":
        count = 0
        for checkRow in range(-1, 2): #2 to include 1
            for checkColumn in range(-1, 2): #2 to include 1
                if not checkRow and not checkColumn: #don't inlcude 0,0'
                    pass
                elif 0 <= row + checkRow < rowLength and 0 <= column + checkColumn < columnLength:
                    count += 1 if data[row + checkRow][column + checkColumn] == "#" else 0
                else:
                    pass
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
    symbol = data[current[0]][current[1]] #speed improvement, only get the element 1 time
    if  symbol == "#": #if occupied return 1
        return 1
    elif symbol == "L": #if empty seat, return 0
        return 0
    elif symbol == ".": #if no seat, call function again to check next position
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
    i = 0
    while working != seats:
        if VISUALIZE and i%2 == 0:
            visualize(seats)
        working = [x[:] for x in seats]
        for row in range(0,len(seats)):
            for column in range(0,len(seats[row])):
                current = working[row][column]
                if current != ".":
                    change = checkSeat1(working, row, column)
                    if change:
                        seats[row][column] = switch[current]
        i+=1
    count = sum([x.count("#") for x in seats])
    return [count]

def solution2():
    f = FileRead.ReadInput(FILENAME)
    directions = ["u", "ru", "r", "rd", "d", "ld", "l", "lu"]
    data = [list(x) for x in f]
    working = []
    i = 0
    while working != data:
        if VISUALIZE and i%2 == 0:
            visualize(data)
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
        i += 1
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

if VISUALIZE:
    screen, font = initVisual()

t1 = timeIt(solution1)
input("continue")
t2 = timeIt(solution2)
print("Total time is {:.2f}s".format(t1 + t2))
input("continue")
