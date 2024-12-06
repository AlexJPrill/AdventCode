import os

def checkPos(x, y, matrix, let):
    tot = 0
    directions = ['UR', 'UL', 'DR', 'DL', 'U', 'D', 'R', 'L']
    for direction in directions:
        tot += checkDiagonal(x, y, direction, matrix, let)
    return tot

def checkDiagonal(x, y, direction, matrix, let):
    word = let
    length = 4  # Length of the word "XMAS"
    for i in range(1, length):
        if direction == 'UR' and isValidCoord(x+i, y-i, matrix):
            word += matrix[y-i][x+i]
        elif direction == 'UL' and isValidCoord(x-i, y-i, matrix):
            word += matrix[y-i][x-i]
        elif direction == 'DR' and isValidCoord(x+i, y+i, matrix):
            word += matrix[y+i][x+i]
        elif direction == 'DL' and isValidCoord(x-i, y+i, matrix):
            word += matrix[y+i][x-i]
        elif direction == 'U' and isValidCoord(x, y-i, matrix):
            word += matrix[y-i][x]
        elif direction == 'D' and isValidCoord(x, y+i, matrix):
            word += matrix[y+i][x]
        elif direction == 'R' and isValidCoord(x+i, y, matrix):
            word += matrix[y][x+i]
        elif direction == 'L' and isValidCoord(x-i, y, matrix):
            word += matrix[y][x-i]
        else:
            break
    return 1 if word == "XMAS" else 0

def isValidCoord(x, y, matrix):
    return 0 <= x < len(matrix[0]) and 0 <= y < len(matrix)

def main():
    file = fr'{os.path.dirname(os.path.abspath(__file__))}/input.txt'
    with open(file) as f:
        data = f.read().splitlines()
    diagCount = 0
    for y, yVal in enumerate(data):
        for x, xVal in enumerate(yVal):
            if xVal == 'X':
                diagCount += checkPos(x, y, data, xVal)

    print(diagCount)

if __name__ == '__main__':
    main()