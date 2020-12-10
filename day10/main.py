import math
import FileRead

FILENAME = "input.txt"

def solution1():
    f = FileRead.ReadInput(FILENAME, True)
    f.sort()
    laptopJolts = f[-1] + 3
    f.append(laptopJolts)
    joltage = 0
    diff1 = 0
    diff3 = 0
    for i in f:
        if i - joltage == 3:
            diff3 += 1
        elif i - joltage == 2:
            continue
        elif i - joltage == 1:
            diff1 += 1
        else:
            raise ValueError("After {} joltage there is no good adapter".format(joltage))
        joltage = i
    return diff3, diff1, diff1 * diff3

def solution2old():
    def calculateChargers(joltage, joltageDiff, file):
        f = [x for x in file if x > joltage]
        adapters = []
        for x in range(0,len(f)):
            newJoltage = f[x]
            diff = newJoltage - joltage
            if diff == joltageDiff:
                return f[x]
            elif diff < joltageDiff:
                adapters.append(f[x])
            elif diff > joltageDiff:
                if len(adapters) > 0:
                    return adapters[-1]
                else:
                    return f[x]

    f = FileRead.ReadInput(FILENAME, True)
    f.sort()
    laptopJolts = f[-1] + 3
    f.append(laptopJolts)
    print(f)
    chargers3 = [0]
    while chargers3[-1] != 22:
        chargers3.append(calculateChargers(chargers3[-1], 3, f))
    chargers2 = [0]
    while chargers2[-1] != 22:
        chargers2.append(calculateChargers(chargers2[-1], 2, f))
    chargers1 = [0]
    while chargers1[-1] != 22:
        chargers1.append(calculateChargers(chargers1[-1], 1, f))
    return [chargers1, chargers2, chargers3]

def solution2():
    def checkChargerSequence(seq, laptopJolts):
        if seq[-1] != laptopJolts:
            return False
        for i in range(0, len(seq) - 1):
            if seq[i + 1] - seq[i] > 3:
                return False
        return True

    def countWays(jolts):
        ways = {}
        ways[0] = 1
        for i in range(1,len(jolts)):
            way1 = ways.get(jolts[i] - 1, 0)
            way2 = ways.get(jolts[i] - 2, 0)
            way3 = ways.get(jolts[i] - 3, 0)
            ways[jolts[i]] = way1 + way2 + way3
        return ways[jolts[-1]]

    f = FileRead.ReadInput(FILENAME, True)
    f.append(0)
    f.sort()
    laptopJolts = f[-1] + 3
    f.append(laptopJolts)
    return [countWays(f)]


def timeIt(func):
    import time
    t1 =time.perf_counter()
    answer = func()
    t1 = time.perf_counter() - t1
    print("Time taken by {}: {:.5f}s".format(func.__name__, t1))
    print(*answer)
    print("\n")
    return t1

t1 = timeIt(solution1)
t2 = timeIt(solution2)
print("Total time: {:.5f}".format(t1+t2))
