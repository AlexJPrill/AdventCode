import os

def pair(iterable):
    a = iter(iterable)
    b = iter(iterable)
    next(b)
    return [p for p in zip(a,b)]


def check(line):
    #Check if all decreasing or increasing
    signs = [y-x for (x, y) in pair(line)]
    if not( all([True if s > 0 else False for s in signs]) or all([True if s < 0 else False for s in signs]) ):
        return False
    absigns = [abs(x) for x in signs]
    if not all([True if s <= 3 and s >= 1 else False for s in absigns]):
        return False
    return True
def main():
    file = fr'{os.path.dirname(os.path.abspath(__file__))}/input.txt'
    with open(file) as f:
        data = f.read().splitlines()
        data = [[int(x) for x in line.split()] for line in data]
        ans = 0
        for line in data:
            if check(line):
                ans += 1
            else:
                for index, i in enumerate(line):
                    n = line.copy()
                    del n[index]
                    if check(n):
                        ans += 1
                        break


    print(ans)

if __name__=='__main__':
    main()