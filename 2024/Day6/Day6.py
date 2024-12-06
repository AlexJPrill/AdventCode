import os
import copy
def isValidCoord(x, y, matrix):
    return 0 <= x < len(matrix[0]) and 0 <= y < len(matrix)
class Gaurd:

    def __init__(self, pos):
        self.directions = ['^', '>', 'v', '<']
        self.direction = 0
        self.pos = pos
    
    def rotate(self):
        self.direction += 1
        if self.direction == 4:
            self.direction = 0
    
    def move(self):
        match self.directions[self.direction]:
            case '^':
                self.pos[1] -= 1
            case '>':
                self.pos[0] += 1
            case 'v': 
                self.pos[1] += 1
            case '<':
                self.pos[0] -= 1
    
    def checkAhead(self):
       match self.directions[self.direction]:
            case '^':
                return (self.pos[0], self.pos[1]-1)
            case '>':
                return (self.pos[0]+1, self.pos[1])
            case 'v': 
                return (self.pos[0], self.pos[1]+1)
            case '<':
                return(self.pos[0]-1, self.pos[1])

def runMaze(gaurd, objects, map):
    visited = set()
    while isValidCoord(gaurd.pos[0], gaurd.pos[1], map):
        visited.add((gaurd.pos[0], gaurd.pos[1], gaurd.directions[gaurd.direction]))
        if gaurd.checkAhead() in objects:
            gaurd.rotate()
        gaurd.move()
        if (gaurd.pos[0], gaurd.pos[1], gaurd.directions[gaurd.direction]) in visited:
            return True
    return False

def main():
    file = fr'{os.path.dirname(os.path.abspath(__file__))}/input.txt'
    with open(file) as f:
        map = f.read().splitlines()
        map = [list(line) for line in map]
    
    objects = []
    gaurd = None
    xStart, yStart = 0, 0
    for y, line in enumerate(map):
        for x, space in enumerate(line):
            if space == '#':
                objects.append((x, y))
            elif space == '^':
                gaurd = Gaurd([x, y])
                xStart = x
                yStart = y
    visited = set()
    while isValidCoord(gaurd.pos[0], gaurd.pos[1], map):
        visited.add((gaurd.pos[0], gaurd.pos[1]))

        #for object in objects:
        #    if int(object[0]) == int(gaurd.checkAhead()[0]) and int(object[1]) == int(gaurd.checkAhead()[1]):
        #        gaurd.rotate()
        #        break
        if gaurd.checkAhead() in objects:
            gaurd.rotate()
        gaurd.move()
    print(len(visited))
    visited.discard((xStart, yStart))
    loops = 0
    count = 0
    for v in visited:
        newObjects = copy.copy(objects)
    
        newObjects.append((v[0], v[1]))
        print('Starting maze ', count, '/', len(visited))
        if runMaze(Gaurd([xStart,yStart]), newObjects, map):
            loops += 1
        count += 1
    print(loops)



if __name__=='__main__':
    main()
