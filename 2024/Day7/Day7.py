import os
import itertools

def evaluate(list):
    i = 1
    ans = 0
    expresion = ''
    expresion+=(list[0])
    while i <= len(list)-2:
        expresion+=(list[i])
        expresion+=(list[i+1])
        print(expresion)
        val = eval(expresion)
        expresion = val
        i+=2
        

    return ans

#This is my closest solution
#But it does not work with equations that contain odd number of values
#need to figure out how to fix it for those
def fixString(list):
    stack = []
    for s in reversed(list):
        stack.append(s)
    v2 = None
    while len(stack) != 1:
        v = stack.pop()
        match v:
            case '+':
                v = stack.pop()
                stack.append(str(eval(v+ '+' + v2)))
            case '*':
                v = stack.pop()
                stack.append(str(eval(v+ '*' + v2)))
            case '|':
                v = stack.pop()
                stack.append(v2+v)
            case _:
                v2 = v
    return int(stack.pop())

#I may have written most of this to be
def checkEquation(str, ans):
    sym = ['+', '*', '|']
    permutations = []
    numSym = len(str) - 1
    combos = [p for p in itertools.product(sym, repeat = numSym)]
    for c in combos:
        dog = (list(itertools.chain.from_iterable(zip(str, c))))
        dog.append(str[-1])
        permutations.append(dog)
    for p in permutations:
        if fixString(p) == ans:
            return 1
        
    return 0 

def main():
    file = fr'{os.path.dirname(os.path.abspath(__file__))}/input.txt'
    with open(file) as f:
        data = f.read().splitlines()
    val= [x.split(':') for x in data]
    equations = dict()
    for v in val:
        equations[int(v[0])] = [x for x in v[1].split()]
    #6
    #How do we go about brute forcing this problem
    ans = 0
    sym = ['+', '*', '|']
    for i, e in enumerate(equations):
        print(str(i) + '/' + str(len(equations)))
        permutations = []
        numSym = len(equations[e])-1
        combos = [p for p in itertools.product(sym, repeat = numSym)]
        for c in combos:
            dog = (list(itertools.chain.from_iterable(zip(equations[e], c))))
            dog.append(equations[e][-1])
            permutations.append(dog)
        for p in permutations:
            if e == fixString(p):
                ans += e
                break 
        

    print(ans)
if __name__=='__main__':
    main()
