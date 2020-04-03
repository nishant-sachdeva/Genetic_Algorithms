import client_moodle
import random
import statistics
import math
import numpy as np
import json

import colorama
from colorama import Fore, Style
import notify

def generate_data_for_comparison(validation_data,  train_data):
    validation_data = np.asarray(validation_data)
    
    train_data = np.asarray(train_data)

    # return_array = np.multiply( np.power(  np.subtract(validation_data , train_data)  , 2)  , validation_data ) 

    return_array = np.multiply ( np.power(validation_data , 5)  , np.power(train_data , 2)  )

    return return_array.tolist()



def naturalSelection(population, populationSize, private_key):
    thisGenFitnessTrain=[]
    thisGenFitnessValidation=[]
    for i in range(0, populationSize):
        temp = client_moodle.get_errors(private_key, population[i])
        
        # print(population[i])
        print( str(i) + " => train : validation " +str(int(temp[0]))+" "+str(int(temp[1])))
        # print(Style.RESET_ALL)
        
        thisGenFitnessTrain.append(temp[0])
        thisGenFitnessValidation.append(temp[1])
    # trainGuidelineUpper = 3625792
    # trainGuidelineLower = 79569
    # validationGuidelineUpper = 3625792

    #code to convert validation and train sets into numpy arrays and applying (y-x) ^3 * y onto them and returning a normal list into the requitsite function

    array_to_be_used_for_comparison = generate_data_for_comparison(thisGenFitnessValidation, thisGenFitnessTrain)

    population = [x for _, x in sorted(zip(array_to_be_used_for_comparison, population))]
    sortedFitnessValArray = sorted(array_to_be_used_for_comparison)
    sortedFitnessValA = sorted(thisGenFitnessValidation) 
    
    # sortedFitnessValArray = sorted(thisGenFitnessValidation) 
    
    fittestIndividualsForDirect = [i for i in range(0, int(populationSize/10))]
    fittestIndividualsForCrossing = [i for i in range(0, int(populationSize/2))]

    print("parents for crossing")
    for i in range(int(populationSize/2)):
        for j in population[i]:
            print(j, end=" ")
        print("\n\n")


    return population, fittestIndividualsForDirect, fittestIndividualsForCrossing, sortedFitnessValArray, sortedFitnessValA
    ####median method
    
    # medTrainVal = statistics.median(thisGenFitnessTrain)
    # medValidationVal = statistics.median(thisGenFitnessValidation)
    # indexTrain=[]
    # indexValidation=[]
    # for i in range(0, populationSize):
    #     if thisGenFitnessTrain[i]>medTrainVal:
    #         indexTrain.append(i)
    #     if thisGenFitnessValidation[i]<medValidationVal:
    #         indexValidation.append(i)
    # commonIndices = list(set(indexTrain).intersection(set(indexValidation)))
    # return commonIndices, indexTrain, indexValidation, thisGenFitnessTrain, thisGenFitnessValidation

def crossover(population, nextGenPopulation, populationSize, fittestIndividualsForDirect, fittestIndividualsForCrossing):
    print("individual(s) selected for elitism")
    for i in range(0, len(fittestIndividualsForDirect)):
        nextGenPopulation.append(population[fittestIndividualsForDirect[i]])
        for j in population[fittestIndividualsForDirect[i]]:
            print(j, end=" ")
        print("\n")
        
    for i in range(0, int((populationSize-len(fittestIndividualsForDirect))/2)):
        tempArray = mate(population, populationSize)
        nextGenPopulation.append(tempArray[0])
        nextGenPopulation.append(tempArray[1])
    if len(nextGenPopulation)!=populationSize:
        nextGenPopulation.append(population[fittestIndividualsForDirect[0]])
    return nextGenPopulation
    # if len(commonIndices)>0:
    #     for i in range(0, len(commonIndices)):
    #         nextGenPopulation.append(population[commonIndices[i]])
    #     symmetricDifferenceIndex=list(set(indexTrain).symmetric_difference(set(indexValidation)))
    #     for i in range(0, int((populationSize-len(commonIndices))/2)):
    #         tempArray = mate(population, symmetricDifferenceIndex)
    #         nextGenPopulation.append(tempArray[0])
    #         nextGenPopulation.append(tempArray[1])
    #     if len(nextGenPopulation)<populationSize:
    #         nextGenPopulation.append(mate(population, symmetricDifferenceIndex)[0])
    # else:
    #     unionIndex=list(set(indexTrain).union(set(indexValidation)))
    #     for i in range(0, int(populationSize/2)):
    #         tempArray = mate(population, unionIndex)
    #         nextGenPopulation.append(tempArray[0])
    #         nextGenPopulation.append(tempArray[1])
    # return nextGenPopulation


def mate(population, populationSize):
    a=random.randint(0, populationSize/2-1)
    b=random.randint(0, populationSize/2-1)
    while b==a:
        b=random.randint(0, populationSize/2-1)
    offSpring0=[]
    offSpring1=[]
    # #####uniform crossover

    for i in range(0, 11):
        coin = random.uniform(0, 1)
        if coin > 0.5:
            offSpring0.append(population[a][i])
            offSpring1.append(population[b][i])
        else:
            offSpring0.append(population[b][i])
            offSpring1.append(population[a][i])
    
    print("parent0")
    for i in population[a]:
        print(i, end=" ")
    print("\n\n")
    print("parent1")
    for i in population[b]:
        print(i, end=" ")
    print("\n\n")
    print("offspring0")
    for i in offSpring0:
        print(i, end=" ")
    print("\n\n")
    print("offspring1")
    for i in offSpring1:
        print(i, end=" ")
    print("\n\n")


    #####single-point crossover

    # crossoverPoint=random.randint(0, 10)
    # for i in range(0, 11):
    #     if i < crossoverPoint:
    #         offSpring0.append(population[a][i])
    #         offSpring1.append(population[b][i])
    #     else:
    #         offSpring0.append(population[b][i])
    #         offSpring1.append(population[a][i])

    #####double-point crossover

    # crossoverPoint0 = random.randint(0, 5)
    # crossoverPoint1 = random.randint(crossoverPoint0+1, 10)
    # for i in range(0, 11):
    #     if i < crossoverPoint0:
    #         offSpring0.append(population[a][i])
    #         offSpring1.append(population[b][i])
    #     elif i >= crossoverPoint0 and i < crossoverPoint1:
    #         offSpring0.append(population[b][i])
    #         offSpring1.append(population[a][i])
    #     else:
    #         offSpring0.append(population[a][i])
    #         offSpring1.append(population[b][i])

    ###### procedure ends here

    offSprings = []
    offSprings.append(offSpring0)
    offSprings.append(offSpring1)
    return offSprings

def mutate(nextGenPopulation, populationSize):
    for i in range(0 , populationSize):
        coin = random.uniform(0,1)
        if coin > 0.7 :
            print(str(i), "individual selected") 
            for j in range(0 , 11):
                another_coin = random.uniform(0,1)
                if another_coin > 0.35:
                    print(str(j), "gene selected")
                    # now we form an new gene basically
                    temp = nextGenPopulation[i][j] * random.uniform(0.9 , 1.1) * random.choice([-1 , 1])

                    nextGenPopulation[i][j] +=temp

                    if math.fabs(nextGenPopulation[i][j]) > 10: 
                        nextGenPopulation[i][j] = float(nextGenPopulation[i][j]/10 )
                    # now we have to choose whether to add / subtract this thing from the 


    return nextGenPopulation

    # for i in range(0, populationSize):
    #     coin = random.uniform(0, 1)
    #     if coin > 0.6:
    #         for j in range(0, 11):
    #             coin1=random.uniform(0, 1)
    #             if coin1>0.35:
    #                 # print("value", nextGenPopulation[i][j])
    #                 # print(math.fabs(nextGenPopulation[i][j]))
    #                 if nextGenPopulation[i][j]!=0.0:
    #                     power = int(math.log(math.fabs(nextGenPopulation[i][j]), 10))
    #                     if power < -2:
    #                         orderOfMagnitude=random.randint(power-2,power+2)
    #                     else:
    #                         orderOfMagnitude=-2
    #                     nextGenPopulation[i][j]+=(random.uniform(-10, 10)*pow(10, orderOfMagnitude))
    #                     if abs(nextGenPopulation[i][j])>10:
    #                         while abs(nextGenPopulation[i][j])>10:
    #                             nextGenPopulation[i][j]/=10
    #                 else:
    #                     nextGenPopulation[i][j]+=(random.uniform(-10, 10)*pow(10, -2))
    # return nextGenPopulation


def storeBestGeneration(population, bestErrorValOfGeneration, printingVal):
    bestErrorVal=[]
    with open("bestErrorVal.txt", "r") as f0:
        bestErrorVal=json.load(f0)
    bestErrorVal = bestErrorVal[0]
    if bestErrorVal> bestErrorValOfGeneration:

        try:
            notify.send_notfication("IMPROVEMENT FOUND")
        except:
            print("IMPROVEMENT FOUND")

        bestErrorVal=[]
        bestErrorVal.append(bestErrorValOfGeneration)
        printVal=[]
        printVal.append(printingVal)
        with open("bestErrorVal.txt", "w") as f0:
            json.dump(bestErrorVal, f0)
        with open("bestPopulation.txt", "w") as f1:
            json.dump(population, f1)
        with open("ErrorVals.txt", "a") as f2:
            json.dump(printVal, f2)
    
    
    
    # f4 = open("ErrorVals.txt", "a+")
    # f2 = open("bestErrorVal.txt", "r+")
    # f3 = open("bestPopulation.txt", "w")
    # bestErrorVal=f2.read()
    # bestErrorVal = 9.222e38
    # temp=0
    # with open('bestErrorVal.txt', "r+") as f2:
    #     with open('bestPopulation.txt', "wt") as f3:
    #         with open('ErrorVals.txt', "w") as f4:
    #             bestErrorVal=f2.load(f2)
    #             if len(bestErrorVal)!=0:
    #                 bestErrorVal=float(bestErrorVal[0])
    #                 temp
    #                 if bestErrorVal>bestErrorValOfGeneration:
    #                     bestErrorVal=bestErrorValOfGeneration
    #                     # f2.write(str(bestErrorVal))
    #                     # f4.write(str(bestErrorVal))
    #                     # f3.write(str(population))
    #             else:
    #                 f2.write(str(bestErrorValOfGeneration))
    #                 f3.write(str(population))
    #                 f4.write(str(bestErrorValOfGeneration)+"\n")

    # f3.close()
    # f2.close()
    # f4.close()