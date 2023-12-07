#This question already breaks my brain and I haven't even started it yet
import re

class Game:

    def __init__(self, id):
        self.id = id
        self.hands = []
    
    def addHand(self, hand):
        self.hands.append(hand)
    
    def getMinEachCube(self):
        red = 0
        green = 0
        blue = 0
        for hand in self.hands:
            if hand["red"] > red:
                red = hand["red"]
            if hand["green"] > green:
                green = hand["green"]
            if hand["blue"] > blue:
                blue = hand["blue"]
        return [red, green, blue]
    

    



def parseInput(line):
    line = line.replace(" ", "")
    line = line.replace("Game", "")
    line = re.split(":|;", line)
    game = Game(line[0])
    line.remove(line[0])
    hands = line
    hands2 = []
    for hand in hands:
        hands2.append(re.split(",", hand))

    for hand in hands2:
        grab = {"red": 0, "green": 0, "blue": 0}
        for cubes in hand:
            
            if cubes.find("red") != -1:
                grab["red"] = int(cubes[0:cubes.find("red")])
            elif cubes.find("green") != -1:
                grab["green"] = int(cubes[0:cubes.find("green")])
            elif cubes.find("blue") != -1:
                grab["blue"] = int(cubes[0:cubes.find("blue")])
        game.addHand(grab)
    return game


red = 12
green = 13
blue = 14

file = open("input.txt", "r")
games = []
for line in file:
    games.append(parseInput(line))


def checkGame(game, red, green, blue):
    for hand in game.hands:
        if hand["red"] > red or hand["green"] > green or hand["blue"] > blue:
            return False
    return True
        

powers = []
for game in games:
    p = game.getMinEachCube()
    s = 1
    for i in p:
        s = s*i
    powers.append(s)


print(sum(powers))

