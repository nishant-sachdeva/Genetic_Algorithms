import client_moodle
import numpy as np
import random
import statistics
import geneticFunctions
import json

import pickle

populationSize = 10

f = open("overfit.txt", "r+")

num = f.read()

num = num.replace("[", " ")

num = num.replace("]", " ")

num = num.strip()

num = num.split(", ")

for i in range(0, len(num)):
    num[i]=float(num[i])

private_key="JVlzF9h4oeN3fyaOoSYgA1HiW82SlS1iptEqtB4lDQAeCK2k8C"


print(num)

population = []

# try:
with open("data_pickle.txt", "rb") as new_filename:
    pp = pickle.load(new_filename)
    # with open(data.txt) as f:
    #     population = json.load(f)

# except:
#     print("the file did not load :/")
#     for i in range(3):
#         population.append(num)

#     for i in range(0, populationSize-3):
#         person = []
#         for i in range(0, 11):
#             gene = random.uniform(-10, 10)
#             person.append(gene)
#         population.append(person)



# # nextGenPopulation = []

# # print("Generation: 0")

# for i in range(1, 4):
#     print("generation "+ str(i))
#     commonIndices, indexTrain, indexValidation, thisGenTrain, thisGenValidation = geneticFunctions.naturalSelection(population, populationSize, private_key)

#     nextGenPopulation = geneticFunctions.crossover(population, nextGenPopulation, populationSize, commonIndices, indexTrain, indexValidation)

#     nextGenPopulation = geneticFunctions.mutate(nextGenPopulation, populationSize)

#     population = nextGenPopulation



# # I have to find a way to make this population persistent
# try:
#     with open(data.txt , "w") as f:
#         json.dump(population , f)

# except:
#     print("the file did not load :/")
#     print(population)

# # this code should write my file into the j