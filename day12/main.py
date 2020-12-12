import FileRead
import re
import math as m
import pygame as pg
import time

FILENAME = "input.txt"
VISUALIZE = input("Want to see an animation?")
SCALE = 1

def initVisual():
    pg.init()
    temp = FileRead.ReadInput(FILENAME)
    size = [500,500]
    screen = pg.display.set_mode(size)
    screen.fill((0,0,0))
    font = pg.font.Font('freesansbold.ttf', 32)
    input("")
    return screen, font

def visualize(positions, minSize, maxSize):
    def moveOriginToMiddle(pos, minSize, maxSize, scale):
        return [(pos[0] + abs(minSize)) * scale, (pos[1] + abs(minSize)) * scale]

    global screen, font, SCALE
    tempScreen = pg.Surface([int((abs(minSize) + maxSize) * SCALE), 
        int((abs(minSize) + maxSize) * SCALE)])
    tempScreen.fill((0,0,0))
    color = (255,0,0)
    positions.append(positions[-1])
    rectScale = int((abs(minSize) + maxSize) / 500) #looks inverse, but this scales the rectangles up
    for i in range(0, len(positions) - 1):
        pos = moveOriginToMiddle(positions[i], minSize, maxSize, SCALE)
        nextPos = moveOriginToMiddle(positions[i + 1], minSize, maxSize, SCALE)
        if i > len(positions) - 10:
            color = (255,255,255)
        else:
            color = (125,0,0)
        pg.draw.rect(tempScreen,
                color,
                pg.Rect(pos[0], pos[1],
                    10 * rectScale, 10 * rectScale)
                )
        pg.draw.line(tempScreen, color, pos, nextPos, width=10*rectScale)
    pg.transform.scale(tempScreen, (500,500), screen)
    del(tempScreen)
    pg.display.flip()
    time.sleep(1/30)

def readInput():
    f = FileRead.ReadInput(FILENAME)
    search = re.compile("(.+?)(\d+)")
    data = []
    for line in f:
        i = re.finditer(search, line)
        data.append([y for x in i for y in x.groups()])
    return data

def solution1():
    position = [0,0]
    direction = 90 #east
    directionChange = {
            "L": lambda x : direction - x if direction -x >= 0 else direction - x + 360,
            "R": lambda x: direction + x if direction + x < 360 else direction + x - 360}
    forwardFunctions = {
            0 : lambda x : [position[0], position[1] - x],
            90 : lambda x : [position[0] + x, position[1]],
            180 : lambda x : [position[0], position[1] + x],
            270 : lambda x : [position[0] - x, position[1]]
            }
    compassToDegree = {
            "N": 0,
            "E": 90,
            "S": 180,
            "W": 270
            }
    data = readInput()
    if VISUALIZE:
        positions = []
        maxX = 250
        maxY = 250
        minX = -250
        minY = -250
    for c in data:
        print(position, direction, c, sep=" ")
        if VISUALIZE:
            maxY = position[1] if position[1] > maxY else maxY
            minY = position[1] if position[1] < minY else minY
            maxX = position[0] if position[0] > maxX else maxX
            minY = position[0] if position[0] < minX else minX
            minSize = min(minY, minX)
            maxSize = max(maxX, maxY)
            positions.append(position)
            visualize(positions, minSize, maxSize)
        command = c[0]
        value = int(c[1])
        if command == "F":
            position = forwardFunctions[direction](value)
        elif command in ["L", "R"]:
            direction = directionChange[command](value)
        elif command in ["N", "E", "S", "W"]:
            position = forwardFunctions[compassToDegree[command]](value)
        # print(c)
        # print(position)
    manhattanDistance = abs(position[0]) + abs(position[1])
    print(manhattanDistance)

def rotatePoint(direction, value, position, waypoint):
    tempWaypoint = waypoint[:]
    if direction == "L":
        value = -value
    else:
        value = value

    x = tempWaypoint[0] * m.cos(m.radians(value)) - tempWaypoint[1] * m.sin(m.radians(value))
    y = tempWaypoint[1] * m.cos(m.radians(value)) + tempWaypoint[0] * m.sin(m.radians(value))
    return [round(x), round(y)]


def solution2():
    position = [0,0]
    waypoint = [10, -1]
    forward = lambda x : [position[0] + waypoint[0] * x, position[1] + waypoint[1] * x]

    waypointFunctions = {
            0 : lambda x : [waypoint[0], waypoint[1] - x],
            90 : lambda x : [waypoint[0] + x, waypoint[1]],
            180 : lambda x : [waypoint[0], waypoint[1] + x],
            270 : lambda x : [waypoint[0] - x, waypoint[1]]
            }
    compassToDegree = {
            "N": 0,
            "E": 90,
            "S": 180,
            "W": 270
            }
    data = readInput()
    if VISUALIZE:
        positions = []
        maxX = 250
        maxY = 250
        minX = -250
        minY = -250
    for c in data:
        print(position, waypoint, c, sep=" ")
        if VISUALIZE:
            maxY = position[1] if position[1] > maxY else maxY
            minY = position[1] if position[1] < minY else minY
            maxX = position[0] if position[0] > maxX else maxX
            minY = position[0] if position[0] < minX else minX
            minSize = min(minY, minX)
            maxSize = max(maxX, maxY)
            positions.append(position)

        command = c[0]
        value = int(c[1])
        if command in ["L", "R"]:
            waypoint = rotatePoint(command, value, position, waypoint)
        elif command in ["N", "E", "S", "W"]:
            waypoint = waypointFunctions[compassToDegree[command]](value)
        elif command in ["F"]:
            position = forward(value)
    visualize(positions, minSize, maxSize)
    print(position, waypoint, c, sep=" ")
    manhattanDistance = abs(position[0]) + abs(position[1])
    print(manhattanDistance)

if VISUALIZE:
    screen, font = initVisual()
# solution1()
input("next")
solution2()
input("exit")



