import pickle
from individual import INDIVIDUAL

# f = open ('robot.p' , 'r' )
# best = pickle.load(f)
# f.close()

# best = INDIVIDUAL(0)
# best.Star
# print(best.fitness)

f = open("robot.p","r")
best = pickle.load(f)
f.close()

best.PrintBest()
best.Start_Evaluation(False)