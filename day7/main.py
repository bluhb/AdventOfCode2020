import FileRead
import re
f = FileRead.ReadInput("input.txt")
re_start = re.compile("^(.+) bags contain (?:(?:(\d) (.+) bag(?:s?|s?\.))|no other bags\.)")
re_rest = re.compile("(?:(\d) (.+) bag(?:s?))")

def parseToRuleDict(r):
    parts = r.split(",")
    contain = []
    startgroups = re.search(re_start, parts[0])
    contain.extend(startgroups.groups())
    for i in parts[1:]:
        groups = re.search(re_rest, i)
        if groups is None:
            print(i)
        else:
            contain.extend(groups.groups())
    rule_dict = {contain[0]: contain[1:]}
    return rule_dict

def searchLuggageBag(bags, my_bag, current_bag):
    if current_bag == my_bag:
        return 1
    elif bags.get(current_bag) is None or bags.get(current_bag)[0] is None:
        return 0
    else:
        counts = []
        for k in bags[current_bag]:
            counts.append(searchLuggageBag(bags, my_bag, k))
        return (max(counts))

def countNeededBags(rules, my_bag):
    if my_bag is None or rules[my_bag][0] is None:
        return 1
    contents = rules[my_bag]
    total = [1]
    for i in range(0, len(contents), 2):
        total.append(int(contents[i]) * countNeededBags(rules, contents[i+1]))
    return sum(total)


def solution1():
    my_bag = "shiny gold"
    rules = {}
    amount = 0
    for i in f:
        rules.update(parseToRuleDict(i))
    for k,v in rules.items():
        if k != my_bag:
            amount += (searchLuggageBag(rules, my_bag, k))
    print(amount)

def solution2():
    my_bag = "shiny gold"
    rules = {}
    amount = 0
    for i in f:
        rules.update(parseToRuleDict(i))
    print(countNeededBags(rules, my_bag) -1)

solution1()
solution2()
