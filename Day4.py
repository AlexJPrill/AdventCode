import sys
class Card:

    def __init__(self, id, winning, numbers):
        self.id = id
        self.winning = winning
        self.numbers = numbers
        self.score = 0
        self.coppies = 1
    
    def getScore(self):
        for num in self.winning:
            if num in self.numbers:
                if self.score == 0:
                    self.score = 1
                else:
                    self.score *= 2
        return self.score

    def getMatches(self):
        matches = 0
        for num in self.winning:
            if num in self.numbers:
                matches += 1
        return matches


def parseInput(string):
    winning =[]
    string = string.split(":")[1]
    string = string.split("|")
    winning = string[0].strip()
    winning = winning.split(" ")
    numbers = string[1].strip()
    numbers = numbers.split(" ")
    for num in numbers:
        if not num.isnumeric():
            numbers.remove(num)
    return (winning, numbers)
    
    

file = open("input.txt", "r")
cards = []
for id, line in enumerate(file):
    winning, numbers = parseInput(line)
    cards.append(Card(id+1, winning, numbers))






numCards = 0
for card in cards:
    numCards += card.coppies
print(numCards)
