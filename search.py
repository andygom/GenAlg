from snakeservo import ROBOT
import numpy as np 
import math 
import pip
import pyrosim
import random
import copy
import pickle
from individual import INDIVIDUAL
from population import POPULATION

popsize = 101
gen = 500

fitvector = [ [0 for c in range(popsize)] for f in range (gen)]
fitprom = [ [0] for f in range (gen)]


parents = POPULATION(popsize, 0, fitvector, fitprom, gen)
parents.Initialize()
parents.Evaluate(True)
print(0),
parents.Print()

for g in range(1, gen):
    children = POPULATION(popsize, g, fitvector, fitprom, gen)
    children.Fill_From(parents)
    children.Evaluate(True)
    print(g),
    children.Print()
    parents.p = children.p
#     children = copy.deepcopy(parents)
#     children.Mutate()
#     children.Evaluate(True)
#     parents.ReplaceWith(children)
#     print(g),s
#     parents.Print()

f= open('robot.p', 'w')
pickle.dump (parents.p[0], f)
f.close()
