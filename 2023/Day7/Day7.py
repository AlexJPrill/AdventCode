import os

class Hand:
    def __init__(self, cards, bid):
        self.bid = bid
        self.cards = self.processCards(cards)
        self.score = -1
        self.rank = -1
    
    

    def processCards(self, cards):
        c = list(cards)
        d = []
        for cd in c:
            match cd:
                case 'T':
                    d.append(10)
                case 'J':
                    d.append(11)
                case 'Q':
                    d.append(12)
                case 'K':
                    d.append(13)
                case 'A':
                    d.append(14)
                case _:
                    d.append(int(cd))
        return d
    
    def getRank(self):
        cards = self.cards.sort()
        something = []
        for c in cards:
            something.append(cards.count(c))
        something.sort()
        match something[4]:
            case 5:
                self.score = 6*sum(self.cards)
            case 4:
                self.score = 5*sum(self.cards)
            case 3:
                self.score = 4*sum(self.cards)
            case _:
                if something[4] == 3 and something[3] == 2:
                    self.score = 3*sum(self.cards)
                if something[4] == 2 and something[3] == 2:
                    self.score = 2*sum(self.cards)
                
            


def main():
    file = fr'{os.path.dirname(os.path.abspath(__file__))}/input.txt'
    with open(file) as f:
        data = f.read().splitlines()
        hands = [[x for x in line.split()] for line in data]
    
    h = Hand(hands[0][0], hands[0][1])


if __name__=='__main__':
    main()
