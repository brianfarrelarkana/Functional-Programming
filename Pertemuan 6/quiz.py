x = [2, 4, 6, 12]
y = [1, 3, 5, 7]
print(sum(list(map(lambda x, y : (((x-y)**2)), x, y)))/len(x))