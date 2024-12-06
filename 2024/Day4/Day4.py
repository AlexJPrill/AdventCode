import os

def checkPos(x, y, matrix, let):
    tot = 0
    directions = ['UR', 'UL', 'DR', 'DL', 'U', 'D', 'R', 'L']
    for dir in directions:
        tot += checkDiagonal(x, y, dir, matrix, let)
    return tot


def masCheck(x, y, matrix):
    ld = '' #UL, DR
    rd = '' #UR, DL
    #First need to check the for corners
    if not isValidCoord(x+1, y-1, matrix):
        return 0
    if not isValidCoord(x-1, y-1, matrix):
        return 0
    if not isValidCoord(x+1, y+1, matrix):
        return 0
    if not isValidCoord(x-1, y+1, matrix):
        return 0
    ld = matrix[y-1][x-1] + matrix[y][x] + matrix[y+1][x+1]
    rd = matrix[y-1][x+1] + matrix[y][x] + matrix[y+1][x-1]
    if (ld == 'MAS' or ld == 'SAM') and (rd == 'MAS' or rd == 'SAM'):
        return 1
    else:
        return 0
def checkDiagonal(x, y, direction, matrix, let):
    
    word = let
    match direction:
        case 'UR':
            for i in range(1, 4):
                if isValidCoord(x+i, y-i, matrix):
                    word += (matrix[y-i][x+i])
                else:
                    break
        case 'UL':
            for i in range(1,4):
                if isValidCoord(x-i, y-i, matrix):
                    word +=(matrix[y-i][x-i])
                else:
                    break
        case 'DR':
            for i in range(1,4):
                if isValidCoord(x+i, y+i, matrix):
                    word +=(matrix[y+i][x+i])
                else:
                    break
        case 'DL':
            for i in range(1,4):
                if isValidCoord(x-i, y+i, matrix):
                    word += (matrix[y+i][x-i])
                else:
                    break
        case 'L':
            for i in range(1,4):
                if isValidCoord(x-i, y, matrix):
                    word += matrix[y][x-i]
                else:
                    break
        case 'R':
            for i in range(1,4):
                if isValidCoord(x+i, y, matrix):
                    word += matrix[y][x+i]
                else:
                    break
        case 'U':
            for i in range(1,4):
                if isValidCoord(x, y-i, matrix):
                    word += matrix[y-i][x]
                else:
                    break
        case 'D':
            for i in range(1,4):
                if isValidCoord(x, y+i, matrix):
                    word += matrix[y+i][x]
                else:
                    break
    if word == 'XMAS':
        return 1
    else:
        return 0

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

    xmasCount = 0
    for y, yVal in enumerate(data):
        for x, xVal in enumerate(yVal):
            if xVal == 'A':
                xmasCount += masCheck(x, y, data)
                

    print(diagCount)
    print(xmasCount)
if __name__=='__main__':
    main()
