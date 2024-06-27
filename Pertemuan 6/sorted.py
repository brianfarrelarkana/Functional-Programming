#sorted
pyList = ['e', 'a', 'u', 'o', 'i']
print(sorted(pyList), "\n")

pyString = 'Python'
print(sorted(pyString), "\n")

pyTuple = ('e', 'a', 'u', 'o', 'i')
print(sorted(pyTuple), "\n")

data_set = {'e', 'a', 'u', 'o', 'i'}
print(sorted(data_set, reverse=True), "\n")

data_dict = {'e' : 1, 'a' : 2, 'u' : 3, 'o' : 4, 'i' : 5}
print(sorted(data_dict, reverse=True), "\n")

def takeSecond(elem):
    return elem[1]
random = [(2, 2), (3, 4), (4, 1), (1, 3)]
sortedList = sorted(random, key=takeSecond)
print('Sorted list : ', sortedList, "\n")