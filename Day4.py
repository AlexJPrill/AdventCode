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


for card in cards:
    c = card.coppies
    n = card.getMatches()
    for i in range(n):
        if i+ 1 < len(cards):
            cards[(card.id)+i].coppies += c




sum = 0
for card in cards:
    #print(card.id, card.getMatches(), card.coppies)
    sum += card.coppies
print(sum)




