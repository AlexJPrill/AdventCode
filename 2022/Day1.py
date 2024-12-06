#Part 1

with open('input.txt') as file:
    data = file.read().split('\n\n')
#have elves be new list of data where we split on the new line charactar
elves = [x.split('\n') for x in data]
elves = [[int(y) for y in x] for x in elves]

#sums = []
#for e in elves:
#    sums.append(sum(e))
sums = [sum(e) for e in elves]

#Part 2
total = 0
for i in range(1, 4):
    total += max(sums)
    sums.remove(max(sums))
print(total)