x = [10, 20, 30]

#menambah data dalam list

x.append(40) #menambahkan data tunggal di belakang list
print(x)

x.insert(2, 50) #nomor awal menunjukan posisi angka yg dimasukkan ke nomor kedua
print(x)

x.extend([66, 77, 88]) #menambah data banyak secara bersamaan di belakang list
print(x)


#menghapus data dalam list

del x[2] #menghapus nilai yang ada di posisi angka dalam kurung
print(x)

x.remove(20) #menghapus nilai dalam kurung
print(x)

nilai = x.pop() #menghapus nilai terakhir
print(x)

print("")

x = [50, 10, 40, 20, 30]

#membalik data dalam list

x.reverse() #membalik urutan data dalam list tanpa mengurutkan
print(x)


#mengurutkan data dalam list (sorting)

y = sorted(x) #mensorting dengan membuat variabel baru
print(y)

x.sort() #mensorting tanpa membuat variabel baru
print(x)

x.sort(reverse=True)
print(x)

print("")

x = [300, 210, 500, 100]

#mencari nilai minimum dan maksimum

print(min (x)) #mencari nilai minimum dalam list

print(max (x)) #mencari nilai maksimum dalam list