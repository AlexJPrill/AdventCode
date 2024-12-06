import re
with open('input.txt') as file:
    pairs = [[int(x) for x in re.findall(r'\d+', line)] for line in file.read().splitlines()]
    data = file.read().splitlines()

#Part 1
#answer = 0
#for p in pairs:
#    if set((range(p[0], p[1]+1))).issubset(range(p[2], p[3]+1)) or set((range(p[2], p[3]+1))).issubset(range(p[0], p[1]+1)):
#        answer += 1
#print(answer)

#Part 2
