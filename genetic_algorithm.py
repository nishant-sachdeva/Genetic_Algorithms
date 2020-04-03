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


# print(num)

population = []

try:
    with open('data.txt') as new_filename:
        population = json.load(new_filename)
        population=population[90:]
        # for i in range(0,90):
        #     person = []
        #     for j in range(0, 11):
        #         gene = random.uniform(-10, 10)
        #         person.append(gene)
        #     population.append(person)
    
except:
    print("the file did not load :/")
    for i in range(1):
        population.append(num)
    for i in range(0, populationSize-1):
        person = []
        for i in range(0, 11):
            gene = random.uniform(-10, 10)
            person.append(gene)
        population.append(person)



for i in range(0, 2):
    nextGenPopulation = []
    print("Generation: "+str(i+1))
    print("Population is")
    for i in population:
        for j in i:
            print(j, end=" ")
        print()
    population, fittestIndividualsForDirect, fittestIndividualsForCrossing, sortedFitnessValArray, sortedFitnessValA=geneticFunctions.naturalSelection(population, populationSize, private_key)
    nextGenPopulation=geneticFunctions.crossover(population, nextGenPopulation, populationSize, fittestIndividualsForDirect, fittestIndividualsForCrossing)
    print("nextGenPopulation after crossover is \n\n")
    for i in nextGenPopulation:
        for j in i:
            print(j, end=" ")
        print()
    nextGenPopulation=geneticFunctions.mutate(nextGenPopulation, populationSize)
    print("nextGenPopulation after mutation is \n\n")
    for i in nextGenPopulation:
        for j in i:
            print(j, end=" ")
        print()
    # geneticFunctions.storeBestGeneration(population, sortedFitnessValArray[0], sortedFitnessValA)
    population=nextGenPopulation
    # print(len(population))
    # print(len(nextGenPopulation))
    # try:
    #     with open('data.txt' , "w") as f:
    #         json.dump(population , f)
    #     print(len(population))
    #     print("All is well that ends well :)")

    # except:
    #     print("the file did not load :/")
    #     print(population)



# I have to find a way to make this population persistent
# try:
#     with open('data.txt' , "w") as f:
#         json.dump(population , f)
#         print(len(population))
print("All is well that ends well :)")

# except:
#     print("the file did not load :/")
#     print(population)

# this code should write my file into the j