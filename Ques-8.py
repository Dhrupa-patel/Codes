# Ques-8 Program to Generate random logs and write in a file , once the file size reaches 2Mbopen new file and continue writing

import os
import random

i=0
logs = ['one', 'two', 'three', 'four', 'five'] #random texts acting as logs value

while True:
    filename = 'test_'+str(i)+'.txt'
    f = open(filename,'a')   
    while os.stat(filename).st_size <2097152:
        f.write(random.choice(logs))
    f.close()
    print(i,'-th file created')
    i+=1
