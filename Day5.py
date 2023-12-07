
class Soil:

    def __init__(self):
        self.source = -1
        self.destination = -1
        self.range = -1


class Map:

    def __init__(self, name):
        self.name = name
        self.soils = []


seedsToPlant = []
maps = []

file = open("input.txt", "r")
l = file.readline()
l = l.split(":")[1].strip()
seedsToPlant = l.split(" ")


        
#dog