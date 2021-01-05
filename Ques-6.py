# Ques-6 Write a Python program to convert an array to an array of machine values andreturn the bytes representation.

from array import *

x = array('i', [1, 2, 3, 4, 5, 6])
print(x.tobytes())
