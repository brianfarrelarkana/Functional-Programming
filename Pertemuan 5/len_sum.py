#len()
print("Len()")
x = [10, 20, 30, 40, 50]
len(x)

testList = []
print(testList, 'length is', len(testList))

testList = [1, 2, 3]
print(testList, 'length is', len(testList))

testTuple = (1, 2, 3)
print(testTuple, 'length is', len(testTuple))

testRange = range(1, 10)
print('Length of', testRange, 'is', len(testRange))


#sum()
print("\nSum()")
x = [10, 20, 30, 40, 50]
sum(x)

data_angka = [1, 2, 3, 4, 5, 1, 4, 5]
jml = sum(data_angka)
print(jml)

jml = sum(data_angka, 10)
print(jml)

jml = sum(data_angka)
rataan = jml/len(data_angka)
print(rataan)