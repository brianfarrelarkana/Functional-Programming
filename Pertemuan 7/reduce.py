from functools import reduce
data = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
multiplier = lambda x, y : x*y
print (reduce (multiplier, data))

from functools import reduce
numbers = [99, 47, 11, 6, 42, 102, 13, 9]
f = lambda a,b : a if a > b else b
max_value = reduce (f, numbers)
print(max_value)