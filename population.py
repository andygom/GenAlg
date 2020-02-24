from individual import INDIVIDUAL
import copy
import random
import numpy as np

class POPULATION: 

      def __init__(self, popsize, gen, fitvector, fitprom, g):
          self.p = {}
          self.gen = gen
          self.g = g 
          self.fitvector = fitvector
          self.genomevector = fitvector
          self.fitprom = fitprom
          # print self.fitvector
          # print self.genomevector
          # print gen
          self.popsize = popsize
          # self.fitvector= [ [0 for c in range(popsize)] for f in range (self.gen)]
          # print self.fitvector

      def Initialize(self):
        for i in range(0, self.popsize):
          self.p[i] = INDIVIDUAL(i)

      def Print(self):
        for i in self.p:
          if ( i in self.p ):
            self.p[i].Print(i, self.popsize, self.fitvector, self.fitprom, self.genomevector, self.gen, self.g)
        print ""

      def Evaluate(self, pb):
        for i in self.p:
          self.p[i].Start_Evaluation(pb)
        for i in self.p:
          self.p[i].Compute_Fitness()
      
      def Mutate(self):
        for i in self.p:
          self.p[i].Mutate()
      
      def ReplaceWith(self,other):
        for i in self.p:
          if ( self.p[i].fitness < other.p[i].fitness):
            self.p[i] = other.p[i]
        
      def Fill_From(self , other):
        self.Copy_Best_From(other)
        # self.Print()
        self.Collect_Children_From(other)
        # self.Print()

      def Copy_Best_From(self, other):
          self.bestfit = -100
          i = 0
          for j in other.p:
            if ( other.p[j].fitness > self.bestfit ):
              self.bestfit = other.p[j].fitness 
              i = j
            self.p[0] = copy.deepcopy(other.p[i]) 

      def Collect_Children_From(self, other):
          for i in range(1, self.popsize, 2):
         
              # winner = other.Winner_Of_Tournament_Selection(other)
              # self.p[i] = copy.deepcopy(winner) 
              # self.p[i].Mutate()
            winnergenome0, winnergenome1 = other.Winner_Of_Tournament_Selection(other, i)
            # self.p[i] = 
            self.p[i] = copy.deepcopy(winnergenome0) 
            self.p[i].Mutate()
            self.p[i+1] = copy.deepcopy(winnergenome1) 
            self.p[i+1].Mutate()
            # for j in range (1):
            #   winnergenome = other.Winner_Of_Tournament_Selection(other, i)
            #   self.p[i+1] = copy.deepcopy(winnergenome) 
            #   self.p[i+1].Mutate()


              # self.Print()
              # print(self.p[i])
          # self.Winner_Of_Tournament_Selection(other)

      def Winner_Of_Tournament_Selection(self, other, i):
        # p1 = random.randint(0, self.popsize-1)
        # p2 = random.randint(0, self.popsize-1)

        # while p1 == p2:
        #   p2 = random.randint(0, self.popsize-1) 
        # else: 
        #   if (other.p[p1].fitness > other.p[p2].fitness):
        #     return other.p[p1]
        #   else: 
        #     return other.p[p2]
        p0 = random.randint(0, self.popsize-1)
        p1 = random.randint(0, self.popsize-1)

        while p0 == p1:
          p0 = random.randint(0, self.popsize-1) 
        else: 
          if (other.p[p0].fitness > other.p[p1].fitness):
            newp0 = p0
          else: 
            newp0 = p1
          

        p2 = random.randint(0, self.popsize-1)
        p3 = random.randint(0, self.popsize-1)

        while p2 == p3:
          p2 = random.randint(0, self.popsize-1) 
        else: 
          if (other.p[p2].fitness > other.p[p3].fitness):
            newp1 = p2
          else: 
            newp1 = p3

        # print (newp0, newp1)
        a0 = other.p[newp0].genome[0:7,:]
        a1 = other.p[newp0].genome[7:14,:]
        b0 = other.p[newp1].genome[0:7,:]
        b1 = other.p[newp1].genome[7:14,:]
        newgenome1 =  np.concatenate((a0, b1), axis = 0)
        newgenome2 =  np.concatenate((b0, a1), axis = 0)

        genomewinner1 = copy.deepcopy(other.p[newp0])
        genomewinner2 = copy.deepcopy(other.p[newp1])
        genomewinner1.genome = newgenome1
        genomewinner2.genome = newgenome2

        # if (i%2 == 0):
        #   return genomewinner1
        # else:
        #  return genomewinner2
        # print newp0, newp1
        return genomewinner1, genomewinner2
        

    
        


        

