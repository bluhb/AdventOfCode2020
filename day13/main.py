import FileRead
import re
import time

FILENAME = "input.txt"

def parseInput():
    f = FileRead.ReadInput(FILENAME)
    regex = "(\d+)"
    arriveTime = f[0]
    busses = [*re.findall(regex, f[1])]
    busses = [int(x) for x in busses]
    return int(arriveTime), busses

def parseInput2():
    f = FileRead.ReadInput(FILENAME)
    regex = "(\d+)"
    arriveTime = f[0]
    busses = f[1].split(",")
    return int(arriveTime), busses

def solution1():
    arriveTime, busses = parseInput()
    i = arriveTime
    while True:
        for bus in busses:
            if i % bus == 0:
                break
        else:
            i += 1
            continue
        break
    return bus * (i - arriveTime)

def solution2():
    _, busses = parseInput2()
    busNumbers = [(i, int(x)) for i,x in enumerate(busses) if x!= "x"]
    print(busNumbers)
    step = busNumbers[0][1]
    t = 0
    for delta, bus in busNumbers:
        while (t + delta) % bus != 0:
            t += step
        step *= bus
    return t

print(solution1())
print(solution2())
