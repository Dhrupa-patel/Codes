# Ques-1 Write a Python program to read a file line by line and store it into a list.

filename = input('Enter File Name with extension (For ex. test.txt):')
f = open(filename,'r')
l=[]
for i in f.readlines(): # will read contents of file line-by-line
    l.append(i.replace('\\n',''))
print(l)
