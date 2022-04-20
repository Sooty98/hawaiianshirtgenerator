import csv
import random

plants=[]
animals=[]
colours=[]

with open('plants.csv', newline='') as plantfile:
    plantreader = csv.reader(plantfile,delimiter=',',quotechar='|')
    for row in plantreader:
        plants.append(row)


with open('animals.csv', newline='') as animalfile:
    animalreader = csv.reader(animalfile,delimiter=',',quotechar='|')
    for row in animalreader:
        animals.append(row)

with open('colours.csv', newline='') as colourfile:
    colourreader = csv.reader(colourfile,delimiter=',',quotechar='|')
    for row in colourreader:
        colours.append(row)

randplant = random.choice(plants)
randanimal = random.choice(animals)
randcolour = random.choice(colours)

print(randplant, ' ', randanimal, ' ', randcolour)