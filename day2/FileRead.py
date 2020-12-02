def readInput(FileName, convertInt=False):
    F = open(FileName)
    Input = []
    for Line in F:
        if convertInt:
            Input.append(int(Line.strip()))
        else:
            Input.append(Line.strip())
    return Input
