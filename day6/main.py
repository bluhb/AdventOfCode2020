import FileRead

f = FileRead.ReadInput("input.txt")

def parseIntoAnswerLists(l):
    total_answers= []
    answers = []
    for x in l:
        if x != "":
            answers.extend(x)
        elif x == "":
            total_answers.append(answers)
            answers = []
        else:
            raise ValueError("unexpected result")
    total_answers.append(answers)
    return total_answers

def parseIntoAnswerLists2(l):
    total_answers= []
    answers = []
    for x in l:
        if x != "":
            answers.append(list(x))
        elif x == "":
            total_answers.append(answers)
            answers = []
        else:
            raise ValueError("unexpected result")
    total_answers.append(answers)
    return total_answers

def solution1():
    answers = parseIntoAnswerLists(f)
    total_answers = 0
    for x in answers:
        total_answers += len(set(x))
    print(total_answers)

def solution2():
    answers = parseIntoAnswerLists2(f)
    total_answers = 0
    for x in answers:
        answer_increase = 0
        questioned_people = len(x)
        answers_combined = [answer for z in x for answer in z]
        for l in x[0]:
            if answers_combined.count(l) == questioned_people:
                answer_increase += 1
            else:
                continue
        total_answers += answer_increase
        answer_increase == 0
        continue
    print("total answers {}".format(total_answers))

solution1()
solution2()

