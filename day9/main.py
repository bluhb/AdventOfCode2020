import sys
import FileRead

if len(sys.argv) < 3:
    sys.exit(1)
file_name = sys.argv[1]
preamble = int(sys.argv[2])

file = FileRead.ReadInput(file_name, True)


def checkValue(value, lastNumbers):
    for i in lastNumbers:
        remainder = value - i
        if remainder != i and remainder in lastNumbers:
            return True
    return False

def solution1():
    lastNumbers = file[:preamble]
    f = file[preamble:]
    for i in range(0, len(f)):
        if not checkValue(f[i], lastNumbers):
            break
        lastNumbers = lastNumbers[1:]
        lastNumbers.append(f[i])
    else:
        return "No error found"
    return f[i]

def solution2(needle):
    f = [x for x in file if x < needle]
    i = 0
    while i < len(f):
        y = i + 2
        while y < len(f) and y != i:
            if sum(f[i:y]) == needle:
                break
            elif sum(f[i:y]) > needle:
                i += 1
            elif sum(f[i:y]) < needle:
                y += 1
        else:
            continue
        break
    else:
        return "no slice found that adds up to {}".format(needle)
    smallest = min(f[i:y])
    biggest = max(f[i:y])
    return "encryption weakness is {} + {} = {}\nSliced between {}:{}".format(
            smallest,
            biggest,
            smallest + biggest,
            i, y)

def timeIt():
    import time
    t1 =time.perf_counter()
    answer1 = solution1()
    t1 = time.perf_counter() - t1
    t2 = time.perf_counter()
    answer2 = solution2(answer1)
    t2 = time.perf_counter() - t2
    print("{} : {}".format(t1, answer1))
    print("{} : {}".format(t2, answer2))

timeIt()
