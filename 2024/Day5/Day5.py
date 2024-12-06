import os
import numpy as np

def findMiddle(input_list):
    middle = float(len(input_list))/2
    if middle % 2 != 0:
        return input_list[int(middle - .5)]
    else:
        return (input_list[int(middle)], input_list[int(middle-1)])
    
def updateCorrect(num, update, rules):
    if update[0] == num:
        after = update.copy()
        after.remove(num)
        for n in after:
            for rule in rules:
                if rule[0] == num and rule[1] == n:
                    return True
            return False
    elif update[len(update)-1] == num:
        before = update[0:update.index(num)]
        for n in before:
            for rule in rules:
                if rule[0] == n and rule[1] == num:
                    return True
            return False
    #Number is somewhere in the middle of the update and we need to check both sides
    else:
        before = update[0:update.index(num)]
        after = update[update.index(num)+1:len(update)+1]
        afterB = False
        beforeB = False
        for n in after:
            for rule in rules:
                if rule[0] == num and rule[1] == n:
                    afterB = True
        for n in before:
            for rule in rules:
                if rule[0] == n and rule[1] == num:
                    beforeB = True
        if afterB == True and beforeB == True:
            return True
        else:
            return False
    
def swap_elements(lst, index1, index2):
    lst[index1], lst[index2] = lst[index2], lst[index1]
    return lst

def fix_update(update, rules):
    cUpdate = update
    correct = False
    while correct == False:
        for num in cUpdate:
            if updateCorrect(num, cUpdate, rules) == False:
                break
            elif cUpdate[-1] == num:
                correct = True
        for num in update:
            for rule in rules:
                if num in rule and rule[abs(rule.index(num)-1)] in update:
                    if rule.index(num) == 0 and (cUpdate.index(num) > cUpdate.index(rule[1])):
                        cUpdate = swap_elements(cUpdate, cUpdate.index(num), cUpdate.index(rule[1]))
                    elif rule.index(num) == 1 and (cUpdate.index(num) < cUpdate.index(rule[0])):
                        cUpdate = swap_elements(cUpdate, cUpdate.index(num), cUpdate.index(rule[0]))
    return findMiddle(cUpdate)

def main():
    file = fr'{os.path.dirname(os.path.abspath(__file__))}/input.txt'
    updates = []
    rules = []
    with open(file) as f:
        data = f.read()
        rules, updates = data.split('\n\n')
        updates = [x.split(',') for x in updates.splitlines()]
        rules = [x.split('|') for x in rules.splitlines()]
    middle_update = 0
    incorrect_middle = 0
    incorrect = []
    for update in updates:
        for num in update:
            s = updateCorrect(num, update, rules)
            if s == False:
                incorrect.append(update)
                break
            if update[-1] == num and s == True:
                middle_update += int(findMiddle(update))
    for n in incorrect:
        incorrect_middle += int(fix_update(n, rules))
    print(incorrect_middle)
    print(middle_update)
if __name__=='__main__':
    main()
