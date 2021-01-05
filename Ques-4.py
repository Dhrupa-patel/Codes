# Ques-4 Write a Python program to sort a list of dictionaries using Lambda.

l = [{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Mi Max', 'model': 2,'color': 'Gold'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]

sort_l = sorted(l, key = lambda x: x['model'])
print(sort_l)
