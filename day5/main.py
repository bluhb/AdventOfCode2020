import FileRead
import math
import pygame as pg
import time

FILENAME = "input.txt"
F = FileRead.ReadInput(FILENAME)
SCALEVERT = 15
SCALEHOR = 1
VISUALIZE = input("show simulation?") == "y"
DOTSIZE = 5

def initVisual(rows):
    pg.init()
    temp = FileRead.ReadInput(FILENAME)
    size = [rows * 8 * SCALEHOR + 30, (8 * SCALEVERT + 60)]
    screen = pg.display.set_mode(size)
    screen.fill((255,255,255))
    font = pg.font.Font('freesansbold.ttf', 32)
    return screen, font

def visualize(data, coordinate = None, init=False):
    global screen, font
    if init:
        for k, c in data.items():
            c = c[:]
            color = (0,255,0)
            if c[1] >= 4:
                c[1] += 1
            pg.draw.circle(screen, color, (c[0] * 8 * SCALEHOR, c[1] * SCALEVERT + 25), DOTSIZE)
    elif coordinate:
        color = (255,0,0)
        if coordinate[1] >= 4:
            coordinate[1] += 1
        pg.draw.circle(screen, color,
                (coordinate[0]* 8 * SCALEHOR, coordinate[1] * SCALEVERT + 25), DOTSIZE)

    # text = font.render(str(seated), True, (255,0,0), (255,255,255))
    # textRect = text.get_rect()
    # screen.blit(text, textRect)
    pg.display.flip()
    time.sleep(1/120)

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
    global screen, font
    IDs = []
    IDtoPlace = {}
    rowmax = 0
    for x in F:
        row, seat = parseSeat(x)
        rowmax = row if row > rowmax else rowmax
        IDs.append(row * 8 + seat)
        IDtoPlace[row * 8 + seat] = [row, seat]

    if VISUALIZE:
        print(rowmax)
        screen, font = initVisual(rowmax)

    # IDs.sort()
    AllIds = []
    for i in range(0,128):
        for x in range(0,8):
            ID = i*8+x
            if min(IDs) < ID < max(IDs):
                AllIds.append(ID)
                IDtoPlace[ID] = [i, x]
    if VISUALIZE:
        visualize(IDtoPlace, init = True)
        input("start")

    Free = [x for x in AllIds if (x not in IDs)]
    for i in range(0,len(IDs) - 1):
        # if IDs[i] + 1 != IDs[i+1]:

        visualize(AllIds, coordinate=IDtoPlace[IDs[i]])
    visualize(AllIds, coordinate=IDtoPlace[IDs[-1]])
    print(Free)
    result =  "your seat is {} + 1 = {}".format(Free[0] - 1, Free[0])
    return result

screen, font = None, None
print(solution1())
print(solution2())
input("exit")


