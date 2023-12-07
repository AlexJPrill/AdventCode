


seedsToPlant = []

file = open("input.txt", "r")
l = file.readline()
l = l.split(":")[1].strip()
seedsToPlant = l.split(" ")
print(seedsToPlant)
#dog