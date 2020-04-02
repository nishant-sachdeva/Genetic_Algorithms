import json
import random
import math

population = []

with open('data.txt') as new_filename:
	population = json.load(new_filename)

	print(len(population))


# with open('data.txt') as new_filename:
# 	new_pop = json.load(new_filename)


# new_pop = new_pop[:90]


for i in range(0 , len(population)):
	coin = random.uniform(0,1)
	if coin > 0.0 : 
		for j in range(0 , 11):
			another_coin = random.uniform(0,1)
			if another_coin > 0.35:
				population[i][j]  = population[i][j] * random.uniform(0.9 , 1.1)
				if math.fabs(population[i][j]) > 10: 
					population[i][j] = float(population[i][j]/10 )


# for pop in new_pop:
# 	population.append(pop)



print("appending complete")
print(len(population))



with open('data.txt' , "w") as f:
	json.dump(population , f)


print("the data has been dumped into the new population")