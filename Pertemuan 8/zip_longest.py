a = ("John", "Charles", "Mike")
b = ("Jenny", "Christy", "Monica", "Vicky")
c = list(zip(a, b))
print(c)

#zip_longest()
import itertools
a = ("John", "Charles", "Mike")
b = ("Jenny", "Christy", "Monica", "Vicky")
c = list(itertools.zip_longest(a, b))
print(c)