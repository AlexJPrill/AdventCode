with open('i.txt') as file:
    data = file.read()

#read each line of the file into a list as an integer. Do this as a list comprehension
data = [int(x) for x in data.split('\n')]
#Part 1
#larger = 0
#
#for i, e in enumerate(data):
#    if i == 0:
#        continue
#    else:
#        if e > data[i-1]:
#            larger += 1
#
#print(larger)

#Part 2
larger = 0
chunks = []
i = 0
for i, e in enumerate(data):
    chunks.append(sum(data[i:i+3]))

for i, e in enumerate(chunks):
    if i == 0:
        continue
    else:
        if e > chunks[i-1]:
            larger += 1
print(larger)