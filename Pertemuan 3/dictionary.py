d = {1:100, 2:200, 3:300, 4:400, 5:500} #menggunakan key value
print(d)

#mengambil 1 data dalam dictionary

print(d[1]) #cara 1

print(d.get(2)) #cara 2

d = {'satu':100, 'dua':200, 'tiga':300, 'empat':400, 'lima':500}

print(d['tiga']) #cara 3

print("")

#contoh :

pegawai = {
    'nip' : "p001",
    'nama' : "Adi",
    'gaji' : 850000
}

print(pegawai ['nip'])
print(pegawai ['nama'])
print(pegawai ['gaji'])

print("")

#menambah data dalam dictionary

d = {}

d['satu'] = 100
d['dua'] = 200
d['tiga'] = 300
print(d)

print("")

#mengubah data dalam dictionary

d = {'satu':100, 'dua':200, 'tiga':300}
print(d['tiga'])
print(d)

d['tiga'] = 600
print(d['tiga'])
print(d)

print("")

#menghitung panjang/banyak data dalam dictionary

print(len (d))

print("")

#menghapus data dalam dictionary

del d['satu'] #menghapus data tunggal
print(d)

keys = ['dua', 'tiga']
for key in keys :
    del d[key]

print(d)