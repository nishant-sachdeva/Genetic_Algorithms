import client_moodle
import numpy as np
import random
import statistics
import geneticFunctions

populationSize=10
f=open("overfit.txt", "r+")
num = f.read()
num = num.replace("[", " ")
num = num.replace("]", " ")
num = num.strip()
num = num.split(", ")
for i in range(0, len(num)):
    num[i]=float(num[i])
private_key="JVlzF9h4oeN3fyaOoSYgA1HiW82SlS1iptEqtB4lDQAeCK2k8C"
ret_val=client_moodle.get_errors(private_key, num)
ret_val2=client_moodle.submit(private_key, num)
print(ret_val, ret_val2)
population=[]
for i in range(0, populationSize):
    temp = []
    for i in range(0, 11):
        temp.append(random.uniform(-10, 10))
    population.append(temp)
nextGenPopulation=[]
print("Generation: 0", end=" ")

for i in range(1, 10):
    # for i in range(0, populationSize):
    #     print(type(population[i]))
    fittestIndividualsForDirect, fittestIndividualsForCrossing, sortedFitnessValArray=geneticFunctions.naturalSelection(population, populationSize, private_key)
    nextGenPopulation=geneticFunctions.crossover(population, nextGenPopulation, populationSize, fittestIndividualsForDirect, fittestIndividualsForCrossing)
    nextGenPopulation=geneticFunctions.mutate(nextGenPopulation, populationSize)
    print(population)
    population=nextGenPopulation
    geneticFunctions.storeBestGeneration(population, sortedFitnessValArray[0])
    # print(str(statistics.median(thisGenTrain))+" "+str(statistics.median(thisGenValidation)))
    print("Generation: "+str(i), end=" ")