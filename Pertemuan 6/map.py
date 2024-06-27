#tanpa map
nilai = [1, 2, 3, 4, 5]
pangkat = []
for x in nilai:
    pangkat.append (x ** 2)
print(pangkat, "\n")

#map
nilai = [1, 2, 3, 4, 5]
def pangkat(x) : return x ** 2
print(list(map(pangkat, nilai)), "\n")

my_list = [1, 5, 4, 6, 8, 11, 3, 12]
new_list = list(map(lambda x: x * 2, my_list))
print(new_list)