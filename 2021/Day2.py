with open('i.txt') as file:
    data = file.readlines()
directions = []
for x in data:
    directions.append(x.strip().split(' '))


#Part 1
horizontal = 0
depth = 0
for d in directions:
    if d[0] == 'forward':
        horizontal += int(d[1])
    if d[0] == 'down':
        depth += int(d[1])
    if d[0] == 'up':
        depth -= int(d[1])

print(horizontal*depth)

#Part 2
horizontal = 0
depth = 0
aim = 0
for d in directions:
    if d[0] == 'forward':
        horizontal += int(d[1])
        depth += int(d[1])*aim
    if d[0] == 'down':
        aim += int(d[1])
    if d[0] == 'up':
        aim -= int(d[1])

print(horizontal*depth)