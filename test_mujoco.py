
import gym
import numpy as np
from gym import wrappers
from policy import Policy
from value_function import NNValueFunction
import scipy.signal
from utils import Logger, Scaler
from datetime import datetime
import os
import argparse
import signal
import time
import tensorflow as tf
import numpy as np
from math import pi,sin,cos
from gym.envs.mujoco.my3_env_LineDirect import MY3EnvLineDirect


env = gym.make('My3LineDirect-v1')
env.set_goals(3)
env.reset()
a= env.action_space.sample()
env.step(a)

'''''
act_dim = env.action_space.shape[0]
print(act_dim)
sim = MY3EnvLineDirect()
sim.reset()
states,states_x,states_y=[],[],[]

for i in range(10):

    action =np.array([5,5,5,5,5 ])
    print(action)
    obs, reward, done, info = sim._step(action)



    xposbefore = sim.get_body_com("cellrobot")[0]
    yposbefore = sim.get_body_com("cellrobot")[1]
    zposbefore = sim.get_body_com("cellrobot")[2]
    print('xposbefore',xposbefore)
    print('yposbefore',yposbefore)
    print('zposbefore',zposbefore)
    state = sim._get_state()


    qpos = sim.data.qpos
    qvel = sim.data.qvel


    print('Initation State:\n')
    print('qpos, shape: %d \n' %(len(qpos)),qpos)
    #print('qvel, shape: %d \n' %(len(qvel)),qvel)
    a = np.concatenate([qpos.flat, qvel.flat])
    print('np.concatenate shape: %d \n' %(len(a)),a)


    print('state',np.concatenate([qpos.flat[0:2]]))
    print('state',state)


    print('ob =',obs)
    print('reward =',reward)
    print('done =',done)
    print('info =',info)

    lala = info['state']
    print(lala)
    state = info['state']
    states.append(state)
    print('states =',states)

    print('i= ',i)

    x =info['state'][0]
    y =info['state'][1]

    states_x = np.append(states_x,x) #提取x位置,扩展向量
    states_y = np.append(states_y,y)

    print('states_x =',states_x)
    print('states_y =', states_y)
    print('-----------------------------')
'''''