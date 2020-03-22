import client_moodle
import numpy as np
import random
import statistics
import geneticFunctions

populationSize=1000
# f=open("overfit.txt", "r+")
# num = f.read()
# num = num.replace("[", " ")
# num = num.replace("]", " ")
# num = num.strip()
# num = num.split(", ")
# for i in range(0, len(num)):
#     num[i]=float(num[i])
private_key="JVlzF9h4oeN3fyaOoSYgA1HiW82SlS1iptEqtB4lDQAeCK2k8C"
# ret_val=client_moodle.get_errors(private_key, num)
# ret_val2=client_moodle.submit(private_key, num)
population=[]
for i in range(0, populationSize):
    temp = []
    for i in range(0, 11):
        temp.append(random.uniform(-10, 10))
    population.append(temp)
nextGenPopulation=[]
print("Generation: 0", end=" ")

for i in range(1, 100):
    commonIndices, indexTrain, indexValidation, thisGenTrain, thisGenValidation=geneticFunctions.naturalSelection(population, populationSize, private_key)
    nextGenPopulation=geneticFunctions.crossover(population, nextGenPopulation, populationSize, commonIndices, indexTrain, indexValidation)
    nextGenPopulation=geneticFunctions.mutate(nextGenPopulation, populationSize)
    population=nextGenPopulation
    print(str(statistics.median(thisGenTrain))+" "+str(statistics.median(thisGenValidation)))
    print("Generation: "+str(i), end=" ")