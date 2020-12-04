import FileRead

F = FileRead.ReadInput("input.txt")


def splitInPassPorts(F):
    PassportStrings = []
    Passports = []
    NewPart = ""
    for Part in F:
        if Part != "":
            NewPart += " " + Part
        else:
            PassportStrings.append(NewPart.strip())
            NewPart = ""
    if NewPart != "":
        PassportStrings.append(NewPart.strip())

    for String in PassportStrings:
        KeyValues = String.split(" ")
        PassPort = {}
        for Pair in KeyValues:
            KeyValue = Pair.split(":")
            PassPort[KeyValue[0]] = KeyValue[1]
        Passports.append(PassPort)

    return Passports

def checkKeysArePresent(Passport, KeysToCheck, solution = 1):
    Keys = list(Passport.keys())
    for Key in KeysToCheck:
        if Key not in Keys:
            return False
        if not checkValue(Passport, Key) and solution == 2:
            return False
    return True

def checkValue(Passport, Key):
    if Key == "byr":
        Result = True if 1920 <= int(Passport[Key]) <= 2002 else False
    elif Key == "iyr":
        Result = True if 2010 <= int(Passport[Key]) <= 2020 else False
    elif Key == "eyr":
        Result = True if 2020 <= int(Passport[Key]) <= 2030 else False
    elif Key == "hgt":
        Unit = Passport[Key][-2:]
        if Unit == "cm":
            Result = True if 150 <= int(Passport[Key][:-2]) <= 193 else False
        elif Unit == "in":
            Result = True if 59 <= int(Passport[Key][:-2]) <= 76 else False
        else:
            Result = False
    elif Key == "hcl":
        if Passport[Key][0] == "#" and len(Passport[Key]) == 7:
            try:
                int(Passport[Key][1:], 16)
                Result = True
            except ValueError:
                Result = False
        else:
            Result = False
    elif Key == "ecl":
        Result = True if Passport[Key] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"] else False
    elif Key == "pid":
        Result = True if len(Passport[Key]) == 9 and Passport[Key].isnumeric else False
    else:
        raise ValueError("Unexpected Key")
        Result = None
    return Result

def solution1():
    KeysToCheck = ["ecl", "pid", "eyr", "hcl", "byr", "iyr", "hgt"]
    Passports = splitInPassPorts(F)
    Amount = 0
    for Passport in Passports:
        if checkKeysArePresent(Passport, KeysToCheck):
            Amount += 1
    print(Amount)

def solution2():
    KeysToCheck = ["ecl", "pid", "eyr", "hcl", "byr", "iyr", "hgt"]
    Passports = splitInPassPorts(F)
    Amount = 0
    for Passport in Passports:
        if checkKeysArePresent(Passport, KeysToCheck, 2):
            Amount += 1
    print(Amount)
solution1()
solution2()
