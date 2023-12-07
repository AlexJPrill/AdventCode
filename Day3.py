#Should probably use a multi dimensional array to solve these

# . are blank spaces and mean nothing
# anything else is a part and if a number is next to it that is its part number they can be diagonal

#Should probably solve this by parts and then find that parts part number of which it can have multiple


ignore = ['.', '\n']
parts = ['/','+','*','@','$','%','#','-','=','&',]
schematic = []

file = open("input.txt", "r")

schematic = []

with open("input.txt", "r") as file:
    for line in file:
        schematic.append(line.strip())

def getPartNumber(schematic, index, position):
    numbers = []
    if index - 1 >= 0:
        #Check all positions above the symbol
        number = ""
        if schematic[index - 1][position].isnumeric():
            begining = -1
            for i in range(position - 1, -1, -1):
                if not schematic[index-1][i].isnumeric():
                    begining = i + 1
                    break
                
            for i in range(begining, len(schematic[index])):
                
                if schematic[index-1][i].isnumeric():
                    number += schematic[index-1][i]
                else:
                    break
        numbers.append(number)
    #Bottom check
    if index + 1 <= len(schematic):
        pass

    return numbers

for line in schematic:
    for char in line:
        if char in parts:
            print(getPartNumber(schematic, schematic.index(line), line.index(char)))
            

    
#Uhh this still doesn't work 