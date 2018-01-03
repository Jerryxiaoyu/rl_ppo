import os

itr ='100000'


for i in range(10):
    TXTnote = 'A003-i'+itr+'-'+str(i+1)
    os.system('python ./train.py My3-v1 -n '+ itr +' -txt '+TXTnote)
    #print('python ./train.py My3-v1 -n '+ itr +' -txt '+TXTnote)


