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

def solution2():
    f = file[:]
    needle = solution1()
    for i in range(0,len(f)):
        for y in range(i+2, len(f)):
            if sum(f[i:y]) == needle:
                break
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


print(solution1())
print(solution2())
