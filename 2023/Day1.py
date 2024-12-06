with open('input.txt') as file:
    data = file.read().splitlines()

l,r = list(zip(*[x.split() for x in data]))
ans = 0
d = []
for line in data:
    d.append(line.split())

left, right =  list(zip(*[x.split() for x in data]))
left, right = [int(x) for x in left], [int(x) for x in right]
#right = [int(x[0]) for x in d]
#left = [int(x[1]) for x in d]

right.sort()
left.sort()

for i, e in enumerate(right):
    ans += abs(left[i] - right[i])


ans = 0

for p in left:
    ans += right.count(p)*p

print(ans)