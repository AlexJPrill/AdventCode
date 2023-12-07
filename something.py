import re
from collections import defaultdict

filename = r'input.txt'
numpattern = r'\d+'
sum = 0
index = 0
totaltickets = defaultdict(int)

with open(filename, 'r') as f:
    for line in f:
        totaltickets[index] += 1
        winning = set()
        have = set()

        data1 = line.split(':')
        data2 = data1[1].split('|')
        nummatches = re.finditer(numpattern, data2[0])
        for match in nummatches:
            winning.add(match.group())
        nummatches = re.finditer(numpattern, data2[1])
        for match in nummatches:
            have.add(match.group())
        n = len(winning & have)
        for i in range(n):
            totaltickets[index + i + 1] += totaltickets[index]
        sum += totaltickets[index]
        index += 1
print(sum)