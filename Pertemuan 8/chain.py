a = [2, 3, 0, 1]
b = [1, 9, 2, 2]
c = []
for i in a:
    c.append(i)
for j in b:
    c.append(j)
print(c)

#Chain()
import itertools
a = [2, 3, 0, 1]
b = [1, 9, 2, 2]
print(list(itertools.chain(a, b)))