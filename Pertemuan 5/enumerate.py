barang = ['roti', 'susu', 'coklat']
enumerateBarang = enumerate(barang)
print(type(enumerateBarang))

print(list(enumerateBarang))

enumerateBarang = enumerate(barang, 10)
print(list(enumerateBarang))

print('\n')

grocery = ['bread', 'milk', 'butter']
for item in enumerate(grocery):
    print(item)
    print('\n')
for count, item in enumerate(grocery):
    print(count, item)
    print('\n')
for count, item in enumerate(grocery, 100):
    print(count, item)