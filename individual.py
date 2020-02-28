import random
import numpy as np
import pyrosim
import math
from snakeservo import ROBOT
import matplotlib.pyplot as plt
import csv

class INDIVIDUAL:

      def __init__(self, i):
        self.ID = i

        self.genomeh = np.random.random((14, 14)) * 2 - 1

        self.genomeop = np.random.random((14, 8)) * 2 - 1


        # print self.genome
          # print(self.genome)
        self.fitness = 0
       

      # def Evaluate(self, pb):
      #     sim = pyrosim.Simulator(xyz=[50,60,0], use_textures=True, eval_time= 1000, play_paused=False, play_blind=pb)
      #     snakeservo = ROBOT(sim, self.genome)
      #     sim.start()
      #     sim.wait_to_finish()
      #     sensorData = sim.get_sensor_data( sensor_id = snakeservo.Pos1, svi=0 )
      #     self.fitness = sensorData[-1]
      #   #   print(sim.get_sensor_data(snakeservo.Ray0)/400)
      #   #   print(sim.get_sensor_data(snakeservo.Pyh))
      #   #   print(sim.get_sensor_data(snakeservo.Pxh))
     
      def Start_Evaluation(self, pb):
        # seconds = 150
        # dt = 0.05
        # eval_time = int(seconds/dt)
        # self.sim = pyrosim.Simulator(xyz=[50,60,0], use_textures=True, eval_time= eval_time, dt = dt ,play_paused=False, play_blind=pb)
        seconds = 120.0
        dt = 0.2
        eval_time = int(seconds/dt)
        # print(eval_time)
        gravity = -1.0

        self.sim = pyrosim.Simulator(eval_time=eval_time, debug=False,
                                   play_paused=False,
                                   gravity=gravity,
                                   play_blind=pb,
                                   use_textures=True,
                                   capture=False,
                                   dt=dt)

        self.snakeservo= ROBOT(self.sim, self.genomeh, self.genomeop)
        self.sim.start()
       
      def Compute_Fitness(self):
        self.sim.wait_to_finish()
        # sensorData = self.sim.get_sensor_data( sensor_id = self.robot.Ray2 )
        # print(sensorData)
        x1 = self.sim.get_sensor_data( sensor_id =  self.snakeservo.Pos1, svi = 0 )
        y1 = self.sim.get_sensor_data( sensor_id = self.snakeservo.Pos1 , svi = 1 )
        x2 = self.sim.get_sensor_data( sensor_id =  self.snakeservo.Pos2, svi = 0 )
        y2 = self.sim.get_sensor_data( sensor_id = self.snakeservo.Pos2 , svi = 1 )
        xc0 = self.sim.get_sensor_data( sensor_id = self.snakeservo.Poscyl[0] , svi = 1 )
        xc1 = self.sim.get_sensor_data( sensor_id = self.snakeservo.Poscyl[1] , svi = 1 )
        xc2 = self.sim.get_sensor_data( sensor_id = self.snakeservo.Poscyl[2] , svi = 1 )
        xc3 = self.sim.get_sensor_data( sensor_id = self.snakeservo.Poscyl[3] , svi = 1 )

        # prop_sensor_results = self.sim.get_sensor_data(self.robot.Px[2])
        # print(prop_sensor_results)
        # self.fitness = x[-1]
        # max_item = max(y)
        # self.fitness = ( (1000-x1[-1]) + (1000-x2[-1] ) )/ 2
        # self.fitness = (x1[-1]+x2[-1])/2
        # print x1[-1], x2[-1]

        self.fitness = (xc0[-1] + (xc1[-1]-xc1[0]) + (xc2[-1]-xc2[0]) + (xc3[-1]-xc3[0]))   / 4



        del self.sim

      def Mutate(self):
        for j in range (0, 13):
          for i in range (0, 13):
            mutgen = random.randint(0, 1000)
            if mutgen < 130 :
              self.genomeh[j][i] = random.gauss( self.genomeh[j][i] , math.fabs(self.genomeh[j][i]))

        for j in range (0, 13):
          for i in range (0, 7):
            mutgen = random.randint(0, 1000)
            if mutgen < 130 :
              self.genomeop[j][i] = random.gauss( self.genomeop[j][i] , math.fabs(self.genomeop[j][i]))          

          # generomutate = random.randint(0, 7)
          # self.genome[0][generomutate] = random.gauss( self.genome[0][generomutate] , math.fabs(self.genome[0][generomutate]))


# inf de cada individuo de la poblacion print, plot fitness, save csv* 
      def Print(self, i, popsize, fitvector, fitprom, genomevector, gen, g):
        # print(self.genome)
        # print(self.fitness),
        print ("["),
        # print "ID]",
        print(self.ID),
        print(self.fitness),
        # print(self.genome),
        print("]"),
        # print i, gen
        fitvector[gen][i] = self.fitness
        # print genoma
        # best = [[0] for f in range (gen)]
        # print max(fitvector)
        
        # genomevector[gen][i] = genoma
        # print genomevector

    

        if  g == gen+1 and i==popsize-1:

          # E N C O N T R A R   MEJOR INDIVIDUO
          best = 0
          self.gbest = 0
          self.ibest = 0
          for g in range (0, gen+1):
            for i in range (0, popsize):
              fitness = fitvector[g][i]
              if fitness > best :
                best = fitness
                self.gbest = g
                self.ibest = i


            

          # P R O M E D I O    FITNESS X GENERACION
          for x in range (0, gen+1):   
          #   print fitprom
            fitprom[x][0] = sum(fitvector[x])/popsize
            # print fitprom

          # G U A R D A R     EN CSV X GENERACION
          for x in range (0, gen+1):
            name = "Gen"+str(x)+".csv"
            with open (name, mode='w') as csv_file:
              fieldnames = ['gen', 'ind', 'genome', 'fitness']
              writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
# falta guardar genoma
              writer.writeheader()
              for i in range (0, popsize):
                writer.writerow({'gen': x, 'ind': i, 'genome': 0, 'fitness': fitvector[x][i]})
         
          #  P L O T 
          f = plt.figure()
          panel = f.add_subplot(111)
          plt.plot(fitprom)
          plt.show()
 
      def PrintBest(self):
        # print(self.genome)
        # print(self.fitness),
        print(self.genomeh),
        print(self.genomeop),
        print ("["),
        print( self.ID),
        print(self.fitness),
        print("]"),
        f= open("bestind.txt", "a")
        np.savetxt("bestind.txt", self.genomeh, self.genomeop )
        f.close()

        with open ('Best.csv', mode='w') as csv_file:
          fieldnames = ['genomeh', 'genomeop', 'fitness']
          writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

          writer.writeheader()
          writer.writerow({'genome': self.genomeh, 'genomeop': self.genomeop, 'fitness': self.fitness})
        



          


