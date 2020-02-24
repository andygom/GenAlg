import sys
sys.path.insert(0, '../..')
import pyrosim 
import math

class ROBOT:

      def __init__(self,sim, wts):
          

          num_of_cyls =  4
          cyl = [0]*num_of_cyls

          num_of_mod = num_of_cyls-1
          mod = [0]*num_of_mod
          
          num_of_modhead = 2
          modhead = [0]*num_of_modhead

          num_of_xjoints = num_of_mod
          jointx = [0]*num_of_xjoints

          num_of_yjoints = num_of_mod
          jointy = [0]*num_of_yjoints

          num_of_headyjoint = 1
          jointheady = [0]*num_of_headyjoint

          num_of_headxjoint = 1
          jointheadx = [0]*num_of_headxjoint

          num_of_proprioceptivesensorx = num_of_xjoints
          self.Px = [0]*num_of_proprioceptivesensorx
          num_of_proprioceptivesensory = num_of_yjoints
          self.Py = [0]*num_of_proprioceptivesensory
          num_of_proprioceptivesensorxh = num_of_headxjoint
          self.Pxh = [0]*num_of_proprioceptivesensorxh
          num_of_proprioceptivesensoryh = num_of_headyjoint
          self.Pyh = [0]*num_of_proprioceptivesensoryh
          self.PNx=[0]*num_of_proprioceptivesensorx
          self.PNy=[0]*num_of_proprioceptivesensory
          self.PNxh=[0]*num_of_proprioceptivesensorxh
          self.PNyh=[0]*num_of_proprioceptivesensoryh
          num_of_motorsneuronx = num_of_xjoints
          num_of_motorsneurony = num_of_yjoints
          self.MNx=[0]*num_of_motorsneuronx
          self.MNy=[0]*num_of_motorsneurony
          num_of_motorsneuronxh = num_of_headxjoint
          num_of_motorsneuronyh = num_of_headyjoint
          self.MNxh=[0]*num_of_motorsneuronxh
          self.MNyh=[0]*num_of_motorsneuronyh
          # body
          sensorhead1 = sim.send_box(x=-8.85, y=3.7, z=7.5/2, mass=0.1, r1=0, r2=1, r3=0, length=3, width=2, height=.3, collision_group='robot', r=1, g=1, b=1)
          sensorhead2 = sim.send_box(x=-8.85, y=-3.7, z=7.5/2, mass=0.1, r1=0, r2=1, r3=0, length=3, width=2, height=.3, collision_group='robot', r=1, g=1, b=1)
          sensorhead4 = sim.send_box(x=65.25, y=3.7, z=7.5/2, mass=0.1, r1=0, r2=1, r3=0, length=3, width=2, height=.3, collision_group='robot', r=1, g=1, b=1)
          sensorhead5 = sim.send_box(x=65.25, y=-3.7, z=7.5/2, mass=0.1, r1=0, r2=1, r3=0, length=3, width=2, height=.3, collision_group='robot', r=1, g=1, b=1)         
          for i in range(num_of_cyls):
              cyl[i] = sim.send_box(x=(10.3+8.5)*i, y=0, z=6/2, mass=2.0, r1=1, r2=0, r3=0, length=3, width=3, height=10.3, collision_group='robot', r=.105, g=.105, b=.105)
          for i in range(num_of_mod):
              mod[i] = sim.send_cylinder(x=(8.5/2)+5.15+((8.5+10.3)*i), y=0, z=6/2, r1=1, r2=0, r3=0, length=8.5, radius=3, mass=1, collision_group='robot', r=1, g=1, b=1, capped=True)
          for i in range(num_of_modhead):
              modhead[i] = sim.send_cylinder(x=-5.15-3.7+(74.1*i), y=0, z=7.4/2, r1=1, r2=0, r3=0, length=8.5, radius=3.7, mass=2, collision_group='robot', r=1, g=1, b=1, capped=True)
          # joints
          for i in range(num_of_headyjoint): 
              jointheady[i] = sim.send_hinge_joint(first_body_id=cyl[0], second_body_id=modhead[0], x=-3.03, y=0, z=7.4/2, n1=0, n2=0, n3=1, lo=(-math.pi / 2.0), hi=(math.pi / 2.0), speed=1.0, torque=11.0, position_control=True)
          for i in range(num_of_headxjoint): 
              jointheadx[i] = sim.send_hinge_joint(first_body_id=cyl[-1], second_body_id=modhead[-1], x=59.43, y=0, z=7.4/2, n1=0, n2=1, n3=0, lo=(-math.pi / 2.0), hi=(math.pi / 2.0), speed=1.0, torque=11.0, position_control=True)
          for i in range(num_of_xjoints): 
              jointx[i] = sim.send_hinge_joint(first_body_id=cyl[i], second_body_id=mod[i], x=3.65+18.8*i, y=0, z=6/2, n1=0, n2=1, n3=0, lo=(-math.pi / 2.0), hi=(math.pi / 2.0), speed=1.0, torque=11.0, position_control=True)
          #3.65, 22.45, 41.25
          # 15.15, 33.95, 52.75
          for i in range(num_of_yjoints): 
              jointy[i] = sim.send_hinge_joint(first_body_id=cyl[i+1], second_body_id=mod[i], x=15.15+18.8*i, y=0, z=6/2, n1=0, n2=0, n3=1, lo=(-math.pi / 2.0), hi=(math.pi / 2.0), speed=1.0, torque=11.0, position_control=True)
          sim.send_fixed_joint(first_body_id=sensorhead1, second_body_id=modhead[0])
          sim.send_fixed_joint(first_body_id=sensorhead2, second_body_id=modhead[0])
          sim.send_fixed_joint(first_body_id=sensorhead4, second_body_id=modhead[1])
          sim.send_fixed_joint(first_body_id=sensorhead5, second_body_id=modhead[1])

          robot = sim.get_group_id('robot')
          sim.assign_collision('robot', 'robot')

           #  S E N S O R S 
          # proprioceptive sensor, in joints  
          for i in range(num_of_proprioceptivesensorx):
              self.Px[i]=sim.send_proprioceptive_sensor(joint_id = jointx[i]) 
          for i in range(num_of_proprioceptivesensory):
              self.Py[i]=sim.send_proprioceptive_sensor(joint_id = jointy[i])
          for i in range(num_of_proprioceptivesensorxh):
              self.Pxh[i]=sim.send_proprioceptive_sensor(joint_id = jointheadx[i]) 
          for i in range(num_of_proprioceptivesensoryh):
              self.Pyh[i]=sim.send_proprioceptive_sensor(joint_id = jointheady[i])
          self.Pos1 = sim.send_position_sensor(body_id=modhead[-1])
          self.Pos2 = sim.send_position_sensor(body_id=modhead[0])
          self.Ray0 = sim.send_ray_sensor(body_id=modhead[0], x =-16.8 , y = 0, z = 7/2, r1 = -1, r2 = 0, r3 = 0, max_distance=400)
          self.Ray1 = sim.send_ray_sensor(body_id=sensorhead1, x =-8.85, y = 3.7 , z = 7.5/2, r1 = 0, r2 =1, r3 = 0, max_distance=400)
          self.Ray2 = sim.send_ray_sensor(body_id=sensorhead2, x =-8.85 , y = -3.5, z = 7.5/2, r1 = 0, r2 = -1, r3 = 0, max_distance=400)
          self.Ray3 = sim.send_ray_sensor(body_id=modhead[1], x =73.2 , y = 0, z = 7/2, r1 = 1, r2 = 0, r3 = 0, max_distance=400)
          self.Ray4 = sim.send_ray_sensor(body_id=sensorhead4, x =65.25 , y = -3.5, z = 7.5/2, r1 = 0, r2 = -1, r3 = 0, max_distance=400)
          self.Ray5 = sim.send_ray_sensor(body_id=sensorhead5, x =65.25 , y = -3.5, z = 7.5/2, r1 = 0, r2 = 1, r3 = 0, max_distance=400)
          # N E U R O N S 
                  # send neurons to proprioceptive sensor
          for i in range(num_of_proprioceptivesensorx):
              self.PNx[i]= sim.send_sensor_neuron( sensor_id = self.Px[i])
          for i in range(num_of_proprioceptivesensory):
              self.PNy[i]= sim.send_sensor_neuron( sensor_id = self.Py[i])
          for i in range(num_of_proprioceptivesensorxh):
              self.PNxh[i]= sim.send_sensor_neuron( sensor_id =self.Pxh[i])
          for i in range(num_of_proprioceptivesensoryh):
              self.PNyh[i]= sim.send_sensor_neuron( sensor_id =self.Pyh[i])

                  # Motor neuron, in joints
          for i in range(num_of_motorsneuronx):
              self.MNx[i]=sim.send_motor_neuron( joint_id = jointx[i])
          for i in range(num_of_motorsneurony):
              self.MNy[i]=sim.send_motor_neuron( joint_id = jointy[i])
          for i in range(num_of_motorsneuronxh):
              self.MNxh[i]=sim.send_motor_neuron( joint_id = jointheadx[i])
          for i in range(num_of_motorsneuronyh):
              self.MNyh[i]=sim.send_motor_neuron( joint_id = jointheady[i])
          
          

          self.SRN0 = sim.send_user_input_neuron(self.Ray0/400)
          self.SRN1 = sim.send_user_input_neuron(self.Ray1/400)
          self.SRN2 = sim.send_user_input_neuron(self.Ray2/400)
          self.SRN3 = sim.send_user_input_neuron(self.Ray3/400)
          self.SRN4 = sim.send_user_input_neuron(self.Ray4/400)
          self.SRN5 = sim.send_user_input_neuron(self.Ray5/400)




          #SYNAPSE     

# R A Y  0
          for m in range(0, 3):
              sim.send_synapse(source_neuron_id=self.SRN0, target_neuron_id=self.MNx[m], weight=wts[0][m])
              sim.send_synapse(source_neuron_id=self.SRN0, target_neuron_id=self.MNy[m], weight=wts[0][m+3])
          sim.send_synapse(source_neuron_id=self.SRN0, target_neuron_id=self.MNxh[0], weight=wts[0][6])
          sim.send_synapse(source_neuron_id=self.SRN0, target_neuron_id=self.MNyh[0], weight=wts[0][7])
# R A Y  1
          for m in range(0, 3):
              sim.send_synapse(source_neuron_id=self.SRN1, target_neuron_id=self.MNx[m], weight=wts[1][m])
              sim.send_synapse(source_neuron_id=self.SRN1, target_neuron_id=self.MNy[m], weight=wts[1][m+3])
          sim.send_synapse(source_neuron_id=self.SRN1, target_neuron_id=self.MNxh[0], weight=wts[1][6])
          sim.send_synapse(source_neuron_id=self.SRN1, target_neuron_id=self.MNyh[0], weight=wts[1][7])
# R A Y  2
          for m in range(0, 3):
              sim.send_synapse(source_neuron_id=self.SRN2, target_neuron_id=self.MNx[m], weight=wts[2][m])
              sim.send_synapse(source_neuron_id=self.SRN2, target_neuron_id=self.MNy[m], weight=wts[2][m+3])
          sim.send_synapse(source_neuron_id=self.SRN2, target_neuron_id=self.MNxh[0], weight=wts[2][6])
          sim.send_synapse(source_neuron_id=self.SRN2, target_neuron_id=self.MNyh[0], weight=wts[2][7])
# R A Y  3
          for m in range(0, 3):
              sim.send_synapse(source_neuron_id=self.SRN3, target_neuron_id=self.MNx[m], weight=wts[3][m])
              sim.send_synapse(source_neuron_id=self.SRN3, target_neuron_id=self.MNy[m], weight=wts[3][m+3])
          sim.send_synapse(source_neuron_id=self.SRN3, target_neuron_id=self.MNxh[0], weight=wts[3][6])
          sim.send_synapse(source_neuron_id=self.SRN3, target_neuron_id=self.MNyh[0], weight=wts[3][7])
# R A Y  4
          for m in range(0, 3):
              sim.send_synapse(source_neuron_id=self.SRN4, target_neuron_id=self.MNx[m], weight=wts[4][m])
              sim.send_synapse(source_neuron_id=self.SRN4, target_neuron_id=self.MNy[m], weight=wts[4][m+3])
          sim.send_synapse(source_neuron_id=self.SRN4, target_neuron_id=self.MNxh[0], weight=wts[4][6])
          sim.send_synapse(source_neuron_id=self.SRN4, target_neuron_id=self.MNyh[0], weight=wts[4][7])
# R A Y  5
          for m in range(0, 3):
              sim.send_synapse(source_neuron_id=self.SRN5, target_neuron_id=self.MNx[m], weight=wts[5][m])
              sim.send_synapse(source_neuron_id=self.SRN5, target_neuron_id=self.MNy[m], weight=wts[5][m+3])
          sim.send_synapse(source_neuron_id=self.SRN5, target_neuron_id=self.MNxh[0], weight=wts[5][6])
          sim.send_synapse(source_neuron_id=self.SRN5, target_neuron_id=self.MNyh[0], weight=wts[5][7])
# P R O S x  0
          for m in range(0, 3):
              sim.send_synapse(source_neuron_id=self.PNx[0], target_neuron_id=self.MNx[m], weight=wts[6][m])
              sim.send_synapse(source_neuron_id=self.PNx[0], target_neuron_id=self.MNy[m], weight=wts[6][m+3])
          sim.send_synapse(source_neuron_id=self.PNx[0], target_neuron_id=self.MNxh[0], weight=wts[6][6])
          sim.send_synapse(source_neuron_id=self.PNx[0], target_neuron_id=self.MNyh[0], weight=wts[6][7])
# P R O S x  1
          for m in range(0, 3):
              sim.send_synapse(source_neuron_id=self.PNx[1], target_neuron_id=self.MNx[m], weight=wts[7][m])
              sim.send_synapse(source_neuron_id=self.PNx[1], target_neuron_id=self.MNy[m], weight=wts[7][m+3])
          sim.send_synapse(source_neuron_id=self.PNx[1], target_neuron_id=self.MNxh[0], weight=wts[7][6])
          sim.send_synapse(source_neuron_id=self.PNx[1], target_neuron_id=self.MNyh[0], weight=wts[7][7])
# P R O S x  2
          for m in range(0, 3):
              sim.send_synapse(source_neuron_id=self.PNx[2], target_neuron_id=self.MNx[m], weight=wts[8][m])
              sim.send_synapse(source_neuron_id=self.PNx[2], target_neuron_id=self.MNy[m], weight=wts[8][m+3])
          sim.send_synapse(source_neuron_id=self.PNx[2], target_neuron_id=self.MNxh[0], weight=wts[8][6])
          sim.send_synapse(source_neuron_id=self.PNx[2], target_neuron_id=self.MNyh[0], weight=wts[8][7])     
# P R O S y  0
          for m in range(0, 3):
              sim.send_synapse(source_neuron_id=self.PNy[0], target_neuron_id=self.MNx[m], weight=wts[9][m])
              sim.send_synapse(source_neuron_id=self.PNy[0], target_neuron_id=self.MNy[m], weight=wts[9][m+3])
          sim.send_synapse(source_neuron_id=self.PNy[0], target_neuron_id=self.MNxh[0], weight=wts[9][6])
          sim.send_synapse(source_neuron_id=self.PNy[0], target_neuron_id=self.MNyh[0], weight=wts[9][7])
# P R O S y  1
          for m in range(0, 3):
              sim.send_synapse(source_neuron_id=self.PNy[1], target_neuron_id=self.MNx[m], weight=wts[10][m])
              sim.send_synapse(source_neuron_id=self.PNy[1], target_neuron_id=self.MNy[m], weight=wts[10][m+3])
          sim.send_synapse(source_neuron_id=self.PNy[1], target_neuron_id=self.MNxh[0], weight=wts[10][6])
          sim.send_synapse(source_neuron_id=self.PNy[1], target_neuron_id=self.MNyh[0], weight=wts[10][7])
# P R O S y  2
          for m in range(0, 3):
              sim.send_synapse(source_neuron_id=self.PNy[2], target_neuron_id=self.MNx[m], weight=wts[11][m])
              sim.send_synapse(source_neuron_id=self.PNy[2], target_neuron_id=self.MNy[m], weight=wts[11][m+3])
          sim.send_synapse(source_neuron_id=self.PNy[2], target_neuron_id=self.MNxh[0], weight=wts[11][6])
          sim.send_synapse(source_neuron_id=self.PNy[2], target_neuron_id=self.MNyh[0], weight=wts[11][7])   
# P R O S head x  
          for m in range(0, 3):
              sim.send_synapse(source_neuron_id=self.PNxh[0], target_neuron_id=self.MNx[m], weight=wts[12][m])
              sim.send_synapse(source_neuron_id=self.PNxh[0], target_neuron_id=self.MNy[m], weight=wts[12][m+3])
          sim.send_synapse(source_neuron_id=self.PNxh[0], target_neuron_id=self.MNxh[0], weight=wts[12][6])
          sim.send_synapse(source_neuron_id=self.PNxh[0], target_neuron_id=self.MNyh[0], weight=wts[12][7])
# P R O S head y  
          for m in range(0, 3):
              sim.send_synapse(source_neuron_id=self.PNyh[0], target_neuron_id=self.MNx[m], weight=wts[13][m])
              sim.send_synapse(source_neuron_id=self.PNyh[0], target_neuron_id=self.MNy[m], weight=wts[13][m+3])
          sim.send_synapse(source_neuron_id=self.PNyh[0], target_neuron_id=self.MNxh[0], weight=wts[13][6])
          sim.send_synapse(source_neuron_id=self.PNyh[0], target_neuron_id=self.MNyh[0], weight=wts[13][7])              
        #       sim.send_synapse(source_neuron_id=self.SRN1, target_neuron_id='MotorNeuronx[m]', weight=wts[1][m])
        #       print(wts[1][m])
        #   for m in MotorNeurony:
        #       sim.send_synapse(source_neuron_id=self.SRN0, target_neuron_id='MotorNeurony[m]', weight=wts[0][m+4])
        #       print(wts[0][m+4])
        #       sim.send_synapse(source_neuron_id=self.SRN1, target_neuron_id='MotorNeurony[m]', weight=wts[1][m+4])
        #       print(wts[1][m+4])
   
  
        #   sim.send_synapse(source_neuron_id=self.PNx[0], target_neuron_id=self.MNx[1], weight=wts[0])      
        #   sim.send_synapse(source_neuron_id=self.Px[1], target_neuron_id=self.MNx[0], weight= wts[0])  
        # #   print(self.Px[1], self.MNx[0])
        # # #   print("peso", wt)  
        #   for i in range(num_of_proprioceptivesensorx):
        #       for myh in range(num_of_motorsneuronyh):
        #           sim.send_synapse(source_neuron_id = self.PNx[i] , target_neuron_id = MNyh[myh] , weight =wts[i]) 
        #       for mxh in range(num_of_motorsneuronxh):
        #           sim.send_synapse(source_neuron_id = self.PNx[i] , target_neuron_id = MNxh[mxh] , weight =wts[i])   
        #       for my in range(num_of_motorsneurony):
        #           sim.send_synapse(source_neuron_id = self.PNx[i] , target_neuron_id = MNy[my] , weight = wts[i])  
        #       for mx in range(num_of_motorsneuronx):
        #           sim.send_synapse(source_neuron_id = self.PNx[i] , target_neuron_id = self.MNx[mx] , weight = wts[i])
              
        #   for i in range(num_of_proprioceptivesensorxh):
        #       for myh in range(num_of_motorsneuronyh):
        #           sim.send_synapse(source_neuron_id = self.PNxh[i] , target_neuron_id = MNyh[myh] , weight =wts[i])  
        #       for mxh in range(num_of_motorsneuronxh):
        #           sim.send_synapse(source_neuron_id = self.PNxh[i] , target_neuron_id = MNxh[mxh] , weight =wts[i])   
        #       for my in range(num_of_motorsneurony):
        #           sim.send_synapse(source_neuron_id = self.PNxh[i] , target_neuron_id = MNy[my] , weight = wts[i])  
        #       for mx in range(num_of_motorsneuronx):
        #           sim.send_synapse(source_neuron_id = self.PNxh[i] , target_neuron_id = self.MNx[mx] , weight = wts[i])         
              
        #   for i in range(num_of_proprioceptivesensory):
        #       for myh in range(num_of_motorsneuronyh):
        #           sim.send_synapse(source_neuron_id = self.PNy[i] , target_neuron_id = MNyh[myh] , weight =wts[i])  
        #       for mxh in range(num_of_motorsneuronxh):
        #           sim.send_synapse(source_neuron_id = self.PNy[i] , target_neuron_id = MNxh[mxh] , weight =wts[i])   
        #       for my in range(num_of_motorsneurony):
        #           sim.send_synapse(source_neuron_id = self.PNy[i] , target_neuron_id = MNy[my] , weight = wts[i])  
        #       for mx in range(num_of_motorsneuronx):
        #           sim.send_synapse(source_neuron_id = self.PNy[i] , target_neuron_id = self.MNx[mx] , weight = wts[i])
              
        #   for i in range(num_of_proprioceptivesensoryh):
        #       for myh in range(num_of_motorsneuronyh):
        #           sim.send_synapse(source_neuron_id = self.PNyh[i] , target_neuron_id = MNyh[myh] , weight =wts[i])  
        #       for mxh in range(num_of_motorsneuronxh):
        #           sim.send_synapse(source_neuron_id = self.PNyh[i] , target_neuron_id = MNxh[mxh] , weight =wts[i])   
        #       for my in range(num_of_motorsneurony):
        #           sim.send_synapse(source_neuron_id = self.PNyh[i] , target_neuron_id = MNy[my] , weight = wts[i])  
        #       for mx in range(num_of_motorsneuronx):
        #           sim.send_synapse(source_neuron_id = self.PNyh[i] , target_neuron_id = self.MNx[mx] , weight = wts[i])   
    
    
        #   for m in range(num_of_motorsneuronx):
        #       sim.send_synapse(source_neuron_id = self.SRN0 , target_neuron_id = self.MNx[m] , weight = wts[i])
        #     #   print(wt)
        #   for m in range(num_of_motorsneurony):
        #       sim.send_synapse(source_neuron_id = self.SRN0 , target_neuron_id = MNy[m] , weight = wts[i]) 
        #   for m in range(num_of_motorsneuronxh):
        #       sim.send_synapse(source_neuron_id = self.SRN0 , target_neuron_id = MNxh[m] , weight =wts[i]) 
        #   for m in range(num_of_motorsneuronyh):
        #       sim.send_synapse(source_neuron_id = self.SRN0 , target_neuron_id = MNyh[m] , weight =wts[i])
        #   for m in range(num_of_motorsneuronx):
        #       sim.send_synapse(source_neuron_id = self.SRN1 , target_neuron_id = self.MNx[m] , weight = wts[i])
        #   for m in range(num_of_motorsneurony):
        #       sim.send_synapse(source_neuron_id = self.SRN1 , target_neuron_id = MNy[m] , weight = wts[i]) 
        #   for m in range(num_of_motorsneuronxh):
        #       sim.send_synapse(source_neuron_id = self.SRN1 , target_neuron_id = MNxh[m] , weight =wts[i]) 
        #   for m in range(num_of_motorsneuronyh):
        #       sim.send_synapse(source_neuron_id = self.SRN1 , target_neuron_id = MNyh[m] , weight =wts[i])
        #   for m in range(num_of_motorsneuronx):
        #       sim.send_synapse(source_neuron_id = self.SRN2 , target_neuron_id = self.MNx[m] , weight = wts[i])
        #   for m in range(num_of_motorsneurony):
        #       sim.send_synapse(source_neuron_id = self.SRN2 , target_neuron_id = MNy[m] , weight = wts[i]) 
        #   for m in range(num_of_motorsneuronxh):
        #       sim.send_synapse(source_neuron_id = self.SRN2 , target_neuron_id = MNxh[m] , weight =wts[i]) 
        #   for m in range(num_of_motorsneuronyh):
        #       sim.send_synapse(source_neuron_id = self.SRN2 , target_neuron_id = MNyh[m] , weight =wts[i])
        #   for m in range(num_of_motorsneuronx):
        #       sim.send_synapse(source_neuron_id = self.SRN3 , target_neuron_id = self.MNx[m] , weight = wts[i])
        #   for m in range(num_of_motorsneurony):
        #       sim.send_synapse(source_neuron_id = self.SRN3 , target_neuron_id = MNy[m] , weight = wts[i]) 
        #   for m in range(num_of_motorsneuronxh):
        #       sim.send_synapse(source_neuron_id = self.SRN3 , target_neuron_id = MNxh[m] , weight =wts[i]) 
        #   for m in range(num_of_motorsneuronyh):
        #       sim.send_synapse(source_neuron_id = self.SRN3 , target_neuron_id = MNyh[m] , weight =wts[i])
        #   for m in range(num_of_motorsneuronx):
        #       sim.send_synapse(source_neuron_id = self.SRN4 , target_neuron_id = self.MNx[m] , weight = wts[i])
        #   for m in range(num_of_motorsneurony):
        #       sim.send_synapse(source_neuron_id = self.SRN4 , target_neuron_id = MNy[m] , weight = wts[i]) 
        #   for m in range(num_of_motorsneuronxh):
        #       sim.send_synapse(source_neuron_id = self.SRN4 , target_neuron_id = MNxh[m] , weight =wts[i]) 
        #   for m in range(num_of_motorsneuronyh):
        #       sim.send_synapse(source_neuron_id = self.SRN4 , target_neuron_id = MNyh[m] , weight =wts[i])
        #   for m in range(num_of_motorsneuronx):
        #       sim.send_synapse(source_neuron_id = self.SRN5 , target_neuron_id = self.MNx[m] , weight = wts[i])
        #   for m in range(num_of_motorsneurony):
        #       sim.send_synapse(source_neuron_id = self.SRN5 , target_neuron_id = MNy[m] , weight = wts[i])   
        #   for m in range(num_of_motorsneuronxh):
        #       sim.send_synapse(source_neuron_id = self.SRN5 , target_neuron_id = MNxh[m] , weight =wts[i])   
        #   for m in range(num_of_motorsneuronyh):
        #       sim.send_synapse(source_neuron_id = self.SRN5 , target_neuron_id = MNyh[m] , weight =wts[i]) 
          
