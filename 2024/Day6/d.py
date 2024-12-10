import os
import copy
import time
from multiprocessing import Pool, cpu_count

class Guard:
    def __init__(self, pos):
        self.pos = pos
        self.directions = ['^', '>', 'v', '<']
        self.direction = 0  # Start facing up

    def rotate(self):
        self.direction = (self.direction + 1) % 4

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
                return (self.pos[0], self.pos[1] - 1)
            case '>':
                return (self.pos[0] + 1, self.pos[1])
            case 'v':
                return (self.pos[0], self.pos[1] + 1)
            case '<':
                return (self.pos[0] - 1, self.pos[1])

def isValidCoord(x, y, map):
    return 0 <= x < len(map[0]) and 0 <= y < len(map)

def runMaze(args):
    guard, objects, map = args
    visited = set()
    while isValidCoord(guard.pos[0], guard.pos[1], map):
        visited.add((guard.pos[0], guard.pos[1], guard.direction))
        while guard.checkAhead() in objects:
            guard.rotate()
        guard.move()
        if (guard.pos[0], guard.pos[1], guard.direction) in visited:
            return True
    return False

def run_maze_with_objects(v, objects, xStart, yStart, map):
    objects.add((v[0], v[1]))
    return runMaze((Guard([xStart, yStart]), objects, map))

def main():
    file = fr'{os.path.dirname(os.path.abspath(__file__))}/input.txt'
    with open(file) as f:
        map = f.read().splitlines()
        map = [list(line) for line in map]

    objects = set()
    guard = None
    xStart, yStart = 0, 0
    for y, line in enumerate(map):
        for x, space in enumerate(line):
            if space == '#':
                objects.add((x, y))
            elif space == '^':
                guard = Guard([x, y])
                xStart = x
                yStart = y

    visited = set()
    while isValidCoord(guard.pos[0], guard.pos[1], map):
        visited.add((guard.pos[0], guard.pos[1]))
        if guard.checkAhead() in objects:
            guard.rotate()
        guard.move()

    loops = 0
    visited.remove((xStart, yStart))
    newObjects = copy.copy(objects)
    with Pool(cpu_count()) as pool:
        results = pool.starmap(run_maze_with_objects, [(v, newObjects, xStart, yStart, map) for v in visited])
    print(cpu_count())
    loops = sum(results)
    print(loops)

def measure_execution_time():
    start_time = time.time()
    main()
    end_time = time.time()
    print(f"Execution time: {end_time - start_time} seconds")

if __name__ == '__main__':
    measure_execution_time()
