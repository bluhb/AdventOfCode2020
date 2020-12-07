import FileRead
import re
f = FileRead.ReadInput("input.txt")

re_search = re.compile("(?:(.+) bags contain)? (?:(?:(\d+) (.+?) bags?)|no other bags)")

def parseToRuleDict(r):
    groups = re.findall(re_search, r)
    groups = [y for tuples in groups for y in tuples if y != ""]
    if len(groups) > 0:
        rule_dict = {groups[0]: groups[1:]}
        return rule_dict
    return {}

def searchLuggageBag(bags, my_bag, current_bag):
    if current_bag == my_bag: #returns when my_bag is found in another bag
        return 1
    elif bags.get(current_bag) is None or len(bags.get(current_bag)) == 0: #if there are no bags inside this bag
        return 0
    else:
        counts = []
        for k in bags[current_bag]: #check for every bag in the current bag
            counts.append(searchLuggageBag(bags, my_bag, k))
        return (max(counts)) #return 0 or 1 depending on if my bag is found

def countNeededBags(rules, my_bag):
    if my_bag is None or len(rules[my_bag]) == 0:
        return 1 #only one bag is in here
    contents = rules[my_bag]
    total = []
    for i in range(0, len(contents), 2):
        total.append(int(contents[i]) * countNeededBags(rules, contents[i+1]))
    return sum(total) + 1 #plus one for the bag that you are checking


def solution1():
    my_bag = "shiny gold"
    rules = {}
    amount = 0
    for i in f:
        rules.update(parseToRuleDict(i))
    for k,v in rules.items():
        if k != my_bag: #don't count my own bag
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
