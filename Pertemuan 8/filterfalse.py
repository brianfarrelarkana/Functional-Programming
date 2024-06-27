fruit = ["Apple", "Banana", "Pear", "Apricot", "Orange"]
filter_object = filter(lambda s: s[0] == "A", fruit)
print(list(filter_object))

#filterfalse()
from itertools import filterfalse
fruit = ["Apple", "Banana", "Pear", "Apricot", "Orange"]
filter_false = filterfalse(lambda s: s[0] == "A", fruit)
print(list(filter_false))