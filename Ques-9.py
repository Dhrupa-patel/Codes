# Ques-9 Script to ping and check whether any given IPs are active,
#also whether given set ofsoftware are installed in the existing system ( like java, kubectl, aws etc)


#Part-1
import os, platform
host = '157.32.203.233'

os.system("ping " + ("-n 1 " if  platform.system().lower()=="windows" else "-c 1 ") + host)



#Part2
import subprocess 
  
Data = subprocess.check_output(['wmic', 'product', 'get', 'name']) # traverse the software list 
a = str(Data).split('\\r\\r\\n')[6:]

software = ['excel','python']
ans = [False]*len(software)

j=0
# try block 
try: 
    while j<len(software):
    # arrange the string 
        for i in a: 
            if software[j].lower() in i.lower():
                ans[j]=True
        j+=1
    print(ans)
    
except IndexError as e: 
    print("All Done")
