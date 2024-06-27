a = [1, 3, 5, 7]
b = [2, 4, 6, 8]
c = []

for x in range (len(a)):
    c.append(a[x] + b[x])

print(c)