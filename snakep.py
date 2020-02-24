import sys
sys.path.insert(0, '../..')
import pyrosim # noqa
import math
# ARM_LENGTH = 0.5
# ARM_RADIUS = ARM_LENGTH / 10.0
# PI = 3.14159

sim = pyrosim.Simulator(eval_time=1000, debug=True, play_paused= False)

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
Px = [0]*num_of_proprioceptivesensorx
num_of_proprioceptivesensory = num_of_yjoints
Py = [0]*num_of_proprioceptivesensory
num_of_proprioceptivesensorxh = num_of_headxjoint
Pxh = [0]*num_of_proprioceptivesensorxh
num_of_proprioceptivesensoryh = num_of_headyjoint
Pyh = [0]*num_of_proprioceptivesensoryh
PNx=[0]*num_of_proprioceptivesensorx
PNy=[0]*num_of_proprioceptivesensory
PNxh=[0]*num_of_proprioceptivesensorxh
PNyh=[0]*num_of_proprioceptivesensoryh
num_of_motorsneuronx = num_of_xjoints
num_of_motorsneurony = num_of_yjoints
MNx=[0]*num_of_motorsneuronx
MNy=[0]*num_of_motorsneurony
num_of_motorsneuronxh = num_of_headxjoint
num_of_motorsneuronyh = num_of_headyjoint
MNxh=[0]*num_of_motorsneuronxh
MNyh=[0]*num_of_motorsneuronyh
for i in range(num_of_cyls):
    j= i+1
    cyl[i] = sim.send_cylinder(x=(1+.6-.27/2)*(i+1), y=0, z=.6/2, r1=1, r2=0, r3=0, length=1.0, radius=0.27, mass=1.0, collision_group='default', r=.105, g=.105, b=.105, capped=True)
for i in range(num_of_mod):
    mod[i] = sim.send_box(x=(0.73+1+0.73/1.5)+(i*(1+0.73/1.5)), y=0, z=.6/2, mass=1.0, r1=0, r2=0, r3=1, length=0.6, width=0.6, height=0.6, collision_group='default', r=1, g=0, b=0)
for i in range(num_of_modhead):
    modhead[i] = sim.send_box(x=1-.27+((1+.6-.27/2)*(3+1)*i), y=0, z=.7/2, mass=1.0, r1=0, r2=0, r3=1, length=0.7, width=0.7, height=0.7, collision_group='default', r=1, g=0, b=0)
for i in range(num_of_headyjoint): 
    jointheady[i] = sim.send_hinge_joint(first_body_id=cyl[0], second_body_id=modhead[0], x=1, y=0, z=.7/2, n1=0, n2=0, n3=1, lo=(-math.pi / 4.0), hi=(math.pi / 4.0), speed=1.0, torque=10.0, position_control=True)
for i in range(num_of_headxjoint): 
    jointheadx[i] = sim.send_hinge_joint(first_body_id=cyl[-1], second_body_id=modhead[-1], x=1-.27+(1+.6-.27/2)*(3+1)-.27, y=0, z=.7/2, n1=0, n2=1, n3=0, lo=(-math.pi / 4.0), hi=(math.pi / 4.0), speed=1.0, torque=10.0, position_control=True)
for i in range(num_of_xjoints): 
    jointx[i] = sim.send_hinge_joint(first_body_id=cyl[i], second_body_id=mod[i], x=2+(1+.6-.27/2)*i, y=0, z=.6/2, n1=0, n2=1, n3=0, lo=(-math.pi / 4.0), hi=(math.pi / 4.0), speed=1.0, torque=10.0, position_control=True)
for i in range(num_of_yjoints): 
    jointy[i] = sim.send_hinge_joint(first_body_id=cyl[i+1], second_body_id=mod[i], x=2+.6-.27/2+(1+.6-.27/2)*i, y=0, z=.6/2, n1=0, n2=0, n3=1, lo=(-math.pi / 4.0), hi=(math.pi / 4.0), speed=1.0, torque=10.0, position_control=True)
#  S E N S O R S 
# proprioceptive sensor, in joints  
for i in range(num_of_proprioceptivesensorx):
    Px[i]=sim.send_proprioceptive_sensor(joint_id = jointx[i]) 

for i in range(num_of_proprioceptivesensory):
    Py[i]=sim.send_proprioceptive_sensor(joint_id = jointy[i])
for i in range(num_of_proprioceptivesensorxh):
    Pxh[i]=sim.send_proprioceptive_sensor(joint_id = jointheadx[i]) 
for i in range(num_of_proprioceptivesensoryh):
    Pyh[i]=sim.send_proprioceptive_sensor(joint_id = jointheady[i])

Ray0 = sim.send_ray_sensor(body_id=modhead[0], x =.7/2 , y = -.7/8, z = .7/2, r1 = -1, r2 = 0, r3 = 0)
Ray1 = sim.send_ray_sensor(body_id=modhead[0], x =.7, y = -.7/8 , z = .7/2, r1 = 0, r2 =-1, r3 = 0)
Ray2 = sim.send_ray_sensor(body_id=modhead[0], x =.7 , y = -.7/8, z = .7/2, r1 = 0, r2 = 1, r3 = 0)

Ray3 = sim.send_ray_sensor(body_id=modhead[1], x =1-.27+((1+.6-.27/2)*(3+1)) , y = -.7/8, z = .7/2, r1 = 1, r2 = 0, r3 = 0)
Ray4 = sim.send_ray_sensor(body_id=modhead[1], x =1-.27+((1+.6-.27/2)*(3+1)) , y = -.7/8, z = .7/2, r1 = 0, r2 = -1, r3 = 0)
Ray5 = sim.send_ray_sensor(body_id=modhead[1], x =1-.27+((1+.6-.27/2)*(3+1)) , y = -.7/8, z = .7/2, r1 = 0, r2 = 1, r3 = 0)
# Ray0 = sim.send_ray_s-1ensor(body_id=0, x=0, y=0, z=0, r1=0, r2=0, r3=1, max_distance=10)
# N E U R O N S 
        # send neurons to proprioceptive sensor
for i in range(num_of_proprioceptivesensorx):
    PNx[i]= sim.send_sensor_neuron( sensor_id = Px[i])
for i in range(num_of_proprioceptivesensory):
    PNy[i]= sim.send_sensor_neuron( sensor_id = Py[i])
for i in range(num_of_proprioceptivesensorxh):
    PNxh[i]= sim.send_sensor_neuron( sensor_id = Pxh[i])
for i in range(num_of_proprioceptivesensoryh):
    PNyh[i]= sim.send_sensor_neuron( sensor_id = Pyh[i])
RN0 = sim.send_sensor_neuron(sensor_id=Ray0)
RN1 = sim.send_sensor_neuron(sensor_id=Ray1)
RN2 = sim.send_sensor_neuron(sensor_id=Ray2)
RN3 = sim.send_sensor_neuron(sensor_id=Ray3)
RN4 = sim.send_sensor_neuron(sensor_id=Ray4)
RN5 = sim.send_sensor_neuron(sensor_id=Ray5)
        # Motor neuron, in joints
for i in range(num_of_motorsneuronx):
    MNx[i]=sim.send_motor_neuron( joint_id = jointx[i])
for i in range(num_of_motorsneurony):
    MNy[i]=sim.send_motor_neuron( joint_id = jointy[i])
for i in range(num_of_motorsneuronxh):
    MNxh[i]=sim.send_motor_neuron( joint_id = jointheadx[i])
for i in range(num_of_motorsneuronyh):
    MNyh[i]=sim.send_motor_neuron( joint_id = jointheady[i])
    
#SYNAPSE 
    
for m in range(num_of_motorsneuronx):
    for i in range(num_of_proprioceptivesensorx):
        sim.send_synapse(source_neuron_id = PNx[i] , target_neuron_id = MNx[m] , weight = 1)


# for m in range(num_of_motorsneurony):
#     for i in range(num_of_proprioceptivesensorx):
#         sim.send_synapse(source_neuron_id = PNx[i] , target_neuron_id = MNy[m] , weight = wt[m][i])    
# for m in range(num_of_motorsneuronxh):
#     for i in range(num_of_proprioceptivesensorx):
#         sim.send_synapse(source_neuron_id = PNx[i] , target_neuron_id = MNxh[m] , weight = wt[m][i])   
# for m in range(num_of_motorsneuronyh):
#     for i in range(num_of_proprioceptivesensorx):
#         sim.send_synapse(source_neuron_id = PNx[i] , target_neuron_id = MNyh[m] , weight = wt[m][i])    
# for m in range(num_of_motorsneuronx):
#     for i in range(num_of_proprioceptivesensorxh):
#         sim.send_synapse(source_neuron_id = PNxh[i] , target_neuron_id = MNx[m] , weight = wt[m][i])
# for m in range(num_of_motorsneurony):
#     for i in range(num_of_proprioceptivesensorxh):
#         sim.send_synapse(source_neuron_id = PNxh[i] , target_neuron_id = MNy[m] , weight = wt[m][i])    
# for m in range(num_of_motorsneuronxh):
#     for i in range(num_of_proprioceptivesensorxh):
#         sim.send_synapse(source_neuron_id = PNxh[i] , target_neuron_id = MNxh[m] , weight = wt[m][i])   
# for m in range(num_of_motorsneuronyh):
#     for i in range(num_of_proprioceptivesensorxh):
#         sim.send_synapse(source_neuron_id = PNxh[i] , target_neuron_id = MNyh[m] , weight = wt[m][i]) 
# for m in range(num_of_motorsneuronx):
#     for i in range(num_of_proprioceptivesensory):
#         sim.send_synapse(source_neuron_id = PNy[i] , target_neuron_id = MNx[m] , weight = wt[m][i])
# for m in range(num_of_motorsneurony):
#     for i in range(num_of_proprioceptivesensory):
#         sim.send_synapse(source_neuron_id = PNy[i] , target_neuron_id = MNy[m] , weight = wt[m][i])    
# for m in range(num_of_motorsneuronxh):
#     for i in range(num_of_proprioceptivesensory):
#         sim.send_synapse(source_neuron_id = PNy[i] , target_neuron_id = MNxh[m] , weight = wt[m][i])   
# for m in range(num_of_motorsneuronyh):
#     for i in range(num_of_proprioceptivesensory):
#         sim.send_synapse(source_neuron_id = PNy[i] , target_neuron_id = MNyh[m] , weight = wt[m][i])                       
# for m in range(num_of_motorsneuronx):
#     for i in range(num_of_proprioceptivesensoryh):
#         sim.send_synapse(source_neuron_id = PNyh[i] , target_neuron_id = MNx[m] , weight = wt[m][i])
# for m in range(num_of_motorsneurony):
#     for i in range(num_of_proprioceptivesensoryh):
#         sim.send_synapse(source_neuron_id = PNyh[i] , target_neuron_id = MNy[m] , weight = wt[m][i])    
# for m in range(num_of_motorsneuronxh):
#     for i in range(num_of_proprioceptivesensoryh):
#         sim.send_synapse(source_neuron_id = PNyh[i] , target_neuron_id = MNxh[m] , weight = wt[m][i])   
# for m in range(num_of_motorsneuronyh):
#     for i in range(num_of_proprioceptivesensoryh):
#         sim.send_synapse(source_neuron_id = PNyh[i] , target_neuron_id = MNyh[m] , weight = wt[m][i])      
# for m in range(num_of_motorsneuronx):
#     sim.send_synapse(source_neuron_id = RN0 , target_neuron_id = MNx[m] , weight = wt[m][i])
# for m in range(num_of_motorsneurony):
#     sim.send_synapse(source_neuron_id = RN0 , target_neuron_id = MNy[m] , weight = wt[m][i])    
# for m in range(num_of_motorsneuronxh):
#     sim.send_synapse(source_neuron_id = RN0 , target_neuron_id = MNxh[m] , weight = wt[m][i])   
# for m in range(num_of_motorsneuronyh):
#     sim.send_synapse(source_neuron_id = RN0 , target_neuron_id = MNyh[m] , weight = wt[m][i]) 
# for m in range(num_of_motorsneuronx):
#     sim.send_synapse(source_neuron_id = RN1 , target_neuron_id = MNx[m] , weight = wt[m][i])
# for m in range(num_of_motorsneurony):
#     sim.send_synapse(source_neuron_id = RN1 , target_neuron_id = MNy[m] , weight = wt[m][i])    
# for m in range(num_of_motorsneuronxh):
#     sim.send_synapse(source_neuron_id = RN1 , target_neuron_id = MNxh[m] , weight = wt[m][i])   
# for m in range(num_of_motorsneuronyh):
#     sim.send_synapse(source_neuron_id = RN1 , target_neuron_id = MNyh[m] , weight = wt[m][i]) 
# for m in range(num_of_motorsneuronx):
#     sim.send_synapse(source_neuron_id = RN2 , target_neuron_id = MNx[m] , weight = wt[m][i])
# for m in range(num_of_motorsneurony):
#     sim.send_synapse(source_neuron_id = RN2 , target_neuron_id = MNy[m] , weight = wt[m][i])    
# for m in range(num_of_motorsneuronxh):
#     sim.send_synapse(source_neuron_id = RN2 , target_neuron_id = MNxh[m] , weight = wt[m][i])   
# for m in range(num_of_motorsneuronyh):
#     sim.send_synapse(source_neuron_id = RN2 , target_neuron_id = MNyh[m] , weight = wt[m][i]) 
# for m in range(num_of_motorsneuronx):
#     sim.send_synapse(source_neuron_id = RN3 , target_neuron_id = MNx[m] , weight = wt[m][i])
# for m in range(num_of_motorsneurony):
#     sim.send_synapse(source_neuron_id = RN3 , target_neuron_id = MNy[m] , weight = wt[m][i])    
# for m in range(num_of_motorsneuronxh):
#     sim.send_synapse(source_neuron_id = RN3 , target_neuron_id = MNxh[m] , weight = wt[m][i])   
# for m in range(num_of_motorsneuronyh):
#     sim.send_synapse(source_neuron_id = RN3 , target_neuron_id = MNyh[m] , weight = wt[m][i]) 
# for m in range(num_of_motorsneuronx):
#     sim.send_synapse(source_neuron_id = RN4 , target_neuron_id = MNx[m] , weight = wt[m][i])
# for m in range(num_of_motorsneurony):
#     sim.send_synapse(source_neuron_id = RN4 , target_neuron_id = MNy[m] , weight = wt[m][i])    
# for m in range(num_of_motorsneuronxh):
#     sim.send_synapse(source_neuron_id = RN4 , target_neuron_id = MNxh[m] , weight = wt[m][i])   
# for m in range(num_of_motorsneuronyh):
#     sim.send_synapse(source_neuron_id = RN4 , target_neuron_id = MNyh[m] , weight = wt[m][i]) 
# for m in range(num_of_motorsneuronx):
#     sim.send_synapse(source_neuron_id = RN5 , target_neuron_id = MNx[m] , weight = wt[m][i])
# for m in range(num_of_motorsneurony):
#     sim.send_synapse(source_neuron_id = RN5 , target_neuron_id = MNy[m] , weight = wt[m][i])    
# for m in range(num_of_motorsneuronxh):
#     sim.send_synapse(source_neuron_id = RN5 , target_neuron_id = MNxh[m] , weight = wt[m][i])   
# for m in range(num_of_motorsneuronyh):
#     sim.send_synapse(source_neuron_id = RN5 , target_neuron_id = MNyh[m] , weight = wt[m][i]) 


sim.start()
sim.wait_to_finish()
sensorData = sim.get_sensor_data( sensor_id = Ray0 )
print(sensorData)