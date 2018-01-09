import os
from  math import pi
import numpy as np


def sample_goals(num_goals):
    #return np.random.uniform(0.0, 3.0, (num_goals,))  #随机生成目标
    return np.arange(-180,180,360/(num_goals))      #序列生成目标



itr =20
num_exp = 1
goals = sample_goals(num_exp)
print(goals)

Model_Name ='A003'
Scripts_Name ='SpecGoal'
Param_const = 'itr'+str(itr)


for i in range(num_exp):
    TXTnote = Model_Name+'-'+Scripts_Name+'-'+Param_const+'-'+'g'+str(int(goals[i]))+'ExpNo'+str(i+1)

    print('python ./train_SpecGoal.py My3LineDirect-v1 -n '+ str(itr) +' -go '+str(goals[i])+' -txt '+TXTnote)
   # os.system('python ./train_SpecGoal.py My3LineDirect-v1 -n '+ str(itr) +' -go '+str(goals[i])+' -txt '+TXTnote)