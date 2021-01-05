# Ques-3 Write a Python program to convert the Python dictionary object (sort by key) toJSON data.
# Print the object members with indent level 4.

import json

my_dict= {'color':'black', 'type':'four-wheeler', 'brand':'Audi', 'year of purchase':'2018'}
json.dumps(my_dict, sort_keys=True, indent=4)
