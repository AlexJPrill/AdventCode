import os
import copy
import time
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
        while gaurd.checkAhead() in objects:
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
    
    objects = set()
    gaurd = None
    xStart, yStart = 0, 0
    for y, line in enumerate(map):
        for x, space in enumerate(line):
            if space == '#':
                objects.add((x, y))
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
    loops = 0
    count = 0
    visited.remove((xStart, yStart))
    for v in visited:
        newObjects = copy.copy(objects)
    
        newObjects.add((v[0], v[1]))
        if runMaze(Gaurd([xStart,yStart]), newObjects, map):
            loops += 1
        count += 1
    print(loops)

def measure_execution_time():
    start_time = time.time()
    main()
    end_time = time.time()
    print(f"Execution time: {end_time - start_time} seconds")

if __name__=='__main__':
    measure_execution_time()
