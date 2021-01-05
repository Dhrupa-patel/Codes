# Ques-5 Write a Python program that takes a text file as input and returns the number ofwords of a given text file.
#Note: Some words can be separated by a comma with no space.

filename = input('Enter File Name with extension (For ex. test.txt):')
f = open(filename,'r')
content = f.read()
content.replace(',', ' ') # This wil handle the edge case of the question

print(len(content.split(' ')))
