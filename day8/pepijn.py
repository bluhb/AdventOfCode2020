def readPuzzle(f):
    with open(f, 'r') as file:
        return [line.rstrip() for line in file]

def analyseData(data):
    for d in data:
        print(d)
    pass

def calculate_accumulator(data):
    idxArr = [*range(len(data))]
    idx = 0
    acc = 0
    operationChanged = True
    while True:
        idxArr.pop(idxArr.index(idx))
        operation = data[idx].split()[0]
        argument = int( data[idx].split()[-1] )
        if operation == 'acc':
            acc += argument
            idx +=1
        elif operation == 'jmp':
            idx += argument
        else:
            idx +=1
        if idx not in idxArr:
            break
    return acc, idx

def puzzle1(data):
    ans = calculate_accumulator(data)
    return ans[0]

def puzzle2(data):
    operators = [o.split()[0] for o in data]
    idxarr = [i for i, x in enumerate(operators) if x == 'nop']
    l = len(idxarr)
    idxarr.extend([i for i, x in enumerate(operators) if x == 'jmp'])
    newname = ['nop', 'jmp']
    i = 0
    while True:
        if i == l:
            newname = newname[::-1]
        data_new = data.copy()
        data_new[idxarr[i]] = data_new[idxarr[i]].replace(newname[0], newname[1])
        i += 1
        acc, idx  = calculate_accumulator(data_new)
        if idx == len(data):
            break
        if i == len(idxarr):
            print('ERROR')
            acc = None
            break
    return acc

if __name__ == "__main__":
    fname='./input.txt'
    data = readPuzzle(fname)
    print( "Puzzle 1, acc = {0}".format( puzzle1(data) ) )
    print( "Puzzle 2, acc = {0}".format( puzzle2(data) ) )
