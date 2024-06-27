a = [10, 20, 30] #tidak memiliki duplikasi datadan data dapat berasal dari list, dictionary, tuple, maupun string
s = set(a)
print (s)
type (s)

print("")

#menambah elemen

s = set ([10, 20, 30])
print(s)

s.add(40) #menambah data tunggal
print(s)

s.update([50, 60, 70]) #menambah data kelompok
print(s)

print("")

#menghapus elemen

s = set ([10, 20, 30])
print(s)

s.discard(20) #menghapus data tunggal
print(s)

s.clear() #menghapus semua data
print(s)

#merubah dengan cara dihapus dulu lalu ditambahkan lagi