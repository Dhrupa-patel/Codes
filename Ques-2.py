# Ques-2 Write a Python program to calculate the number of days between two dates.
#Sample dates : (20200702), (20200711)

from datetime import date

input_1 = input('Enter starting date in format(yyyymmdd):')
input_2 = input('Enter end date in format(yyyymmdd):')

#will create date object based on the string provided by the user
date1 = date(int(input_1[:4]),int(input_1[4:6]),int(input_1[6:8]))
date2 = date(int(input_2[:4]),int(input_2[4:6]), int(input_2[6:8]))
print(abs((date2-date1).days))
