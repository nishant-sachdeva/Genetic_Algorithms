import client_moodle
import random
import statistics
import math

def naturalSelection(population, populationSize, private_key):
    thisGenFitnessTrain=[]
    thisGenFitnessValidation=[]
    for i in range(0, populationSize):
        temp=client_moodle.get_errors(private_key, population[i])
        print(str(i)+"th element's error for train and validation are " +str(temp[0])+" "+str(temp[1]))
        thisGenFitnessTrain.append(temp[0])
        thisGenFitnessValidation.append(temp[1])
    # trainGuidelineUpper = 3625792
    # trainGuidelineLower = 79569
    # validationGuidelineUpper = 3625792

    population = [x for _, x in sorted(zip(thisGenFitnessValidation, population))]
    sortedFitnessValArray = sorted(thisGenFitnessValidation) 
    
    fittestIndividualsForDirect = [i for i in range(0, int(populationSize/10))]
    fittestIndividualsForCrossing = [i for i in range(0, int(populationSize/5))]

    return population, fittestIndividualsForDirect, fittestIndividualsForCrossing, sortedFitnessValArray
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
    for i in range(0, len(fittestIndividualsForDirect)):
        nextGenPopulation.append(population[fittestIndividualsForDirect[i]])
        
    for i in range(0, int((populationSize-len(fittestIndividualsForDirect))/2)):
        tempArray = mate(population, fittestIndividualsForCrossing)
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


def mate(population, symmetricDifferenceIndex):
    a=random.randint(0, len(symmetricDifferenceIndex)-1)
    b=random.randint(0, len(symmetricDifferenceIndex)-1)
    while b==a:
        b=random.randint(0, len(symmetricDifferenceIndex)-1)
    offSpring0=[]
    offSpring1=[]
    #####uniform crossover

    # for i in range(0, 11):
    #     coin = random.uniform(0, 1)
    #     if coin > 0.5:
    #         offSpring0.append(population[a][i])
    #         offSpring1.append(population[b][i])
    #     else:
    #         offSpring0.append(population[b][i])
    #         offSpring1.append(population[a][i])
    
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

    crossoverPoint0 = random.randint(0, 5)
    crossoverPoint1 = random.randint(crossoverPoint0+1, 10)
    for i in range(0, 11):
        if i < crossoverPoint0:
            offSpring0.append(population[a][i])
            offSpring1.append(population[b][i])
        elif i >= crossoverPoint0 and i < crossoverPoint1:
            offSpring0.append(population[b][i])
            offSpring1.append(population[a][i])
        else:
            offSpring0.append(population[a][i])
            offSpring1.append(population[b][i])
    offSprings = []
    offSprings.append(offSpring0)
    offSprings.append(offSpring1)
    return offSprings

def mutate(nextGenPopulation, populationSize):
    for i in range(0, populationSize):
        coin = random.uniform(0, 1)
        if coin > 0.8:
            for j in range(0, 11):
                coin1=random.uniform(0, 1)
                if coin1>0.35:
                    # print("value", nextGenPopulation[i][j])
                    # print(math.fabs(nextGenPopulation[i][j]))
                    if nextGenPopulation[i][j]!=0.0:
                        power = int(math.log(math.fabs(nextGenPopulation[i][j]), 10))
                        if power < -2:
                            orderOfMagnitude=random.randint(power-2,power+2)
                        else:
                            orderOfMagnitude=-2
                        nextGenPopulation[i][j]+=(random.uniform(-10, 10)*pow(10, orderOfMagnitude))
                        if abs(nextGenPopulation[i][j])>10:
                            while abs(nextGenPopulation[i][j])>10:
                                nextGenPopulation[i][j]/=10
                    else:
                        nextGenPopulation[i][j]+=(random.uniform(-10, 10)*pow(10, -2))
    return nextGenPopulation


def storeBestGeneration(population, bestErrorValOfGeneration):
    f2 = open("bestErrorVal.txt", "w+")
    f3 = open("bestPopulation.txt", "w")
    bestErrorVal=f2.read()
    if len(bestErrorVal)!=0:
        bestErrorVal=int(bestErrorVal)
        if bestErrorVal>bestErrorValOfGeneration:
            bestErrorVal=bestErrorValOfGeneration
            f2.write(str(bestErrorVal))
            f3.write(str(population))
    else:
        bestErrorVal = bestErrorValOfGeneration
        f2.write(str(bestErrorVal))
        f3.write(str(population))
    f3.close()
    f2.close()
