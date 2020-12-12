import FileRead
import re
import math as m

FILENAME = "input.txt"

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
    for c in data:
        print(position, direction, c, sep=" ")
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
    for c in data:
        print(position, waypoint, c, sep=" ")
        command = c[0]
        value = int(c[1])
        if command in ["L", "R"]:
            waypoint = rotatePoint(command, value, position, waypoint)
        elif command in ["N", "E", "S", "W"]:
            waypoint = waypointFunctions[compassToDegree[command]](value)
        elif command in ["F"]:
            position = forward(value)
    print(position, waypoint, c, sep=" ")
    manhattanDistance = abs(position[0]) + abs(position[1])
    print(manhattanDistance)

solution1()
solution2()



