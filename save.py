import numpy as np 
import math 
import pip
import pyrosim
import random
import copy
import pickle
from snakeservo import ROBOT
from individual import INDIVIDUAL
from population import POPULATION

genvector = np.genfromtxt('bestind.txt', dtype='float')
print genvector

indbest = INDIVIDUAL(0)
indbest.genome = genvector
print indbest.genome
indbest.Start_Evaluation(False)


