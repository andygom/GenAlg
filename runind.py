import csv
import numpy as np 
from snakeservo import ROBOT
from individual import INDIVIDUAL
from population import POPULATION

generation = 0
individual = 1

genfile = "Gen"+str(generation)+".csv"

with open(genfile, 'rb') as f:
    reader = csv.reader(f)

