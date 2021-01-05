# Ques-7 Write a script which can read the files line by line with .log ext and print it into afile ,
#while printing the data from the suffix with present date and time of the system.

import glob
from datetime import datetime

files = glob.glob("C:/Users/admin/Desktop/*.txt")
print(files)
fileWrite = open('merged_file.txt','a')

for file in files:
    f = open(file,'r')
    txt = f.readline()
    txt = str(datetime.now())+' '+txt
    print(txt)
    fileWrite.write(txt+'\n')
    f.close()

fileWrite.close()
