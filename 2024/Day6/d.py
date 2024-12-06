import os
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

def runMaze(guard, objects, map):
    visited = set()
    while isValidCoord(guard.pos[0], guard.pos[1], map):
        visited.add((guard.pos[0], guard.pos[1], guard.direction))
        if guard.checkAhead() in objects:
            guard.rotate()
        guard.move()
        if (guard.pos[0], guard.pos[1], guard.direction) in visited:
            return True
    return False

def main():
    file = fr'{os.path.dirname(os.path.abspath(__file__))}/input.txt'
    with open(file) as f:
        map = f.read().splitlines()
        map = [list(line) for line in map]

    objects = []
    guard = None
    for y, line in enumerate(map):
        for x, space in enumerate(line):
            if space == '#':
                objects.append((x, y))
            elif space == '^':
                guard = Guard([x, y])

    if guard is not None:
        if runMaze(guard, objects, map):
            print("Guard revisited a position with the same direction.")
        else:
            print("Guard did not revisit any position with the same direction.")

if __name__ == '__main__':
    main()