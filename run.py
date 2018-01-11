import os
from  math import pi
import numpy as np


def sample_goals(num_goals):
    #return np.random.uniform(0.0, 3.0, (num_goals,))  #随机生成目标
    return np.arange(-180,180,360/(num_goals))      #序列生成目标



def SpecGoal():
    itr =40
    num_exp = 1
    goals = sample_goals(num_exp)
    print(goals)

    Model_Name ='A003'
    Scripts_Name ='SpecGoal'
    Param_const = 'itr'+str(itr)


    for i in range(num_exp):
        TXTnote = Model_Name+'-'+Scripts_Name+'-'+Param_const+'-'+'g'+str(int(goals[i]))+'ExpNo'+str(i+1)+'ceshi'

       # print('python ./train_SpecGoal.py My3LineDirect-v1 -n '+ str(itr) +' -go '+str(goals[i])+' -txt '+TXTnote)
        os.system('python ./train_SpecGoal.py My3LineDirect-v1 -n '+ str(itr) +' -go '+str(goals[i])+' -txt '+TXTnote)

os.system("python ./test.py My3LineDirect-v1 -b 200 -txt 'A003'")
#main('My3LineDirect-v1', 1000, 0.995, 0.98, 0.003, 200, 'A003-test')