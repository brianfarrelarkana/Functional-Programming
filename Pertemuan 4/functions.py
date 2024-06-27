# Contoh 1:

x = [1, 2, 3]
def fungsi_sederhana(x):
    x[1] = 42
fungsi_sederhana (x)
print (x)


# Contoh 2:

def tambah (a, b, c):
    return a+b+c
print (tambah(1, 2, 3))


# Contoh 3:

PI = 3,141592
print (5*5*PI)


# Contoh 4:

PI = 3,141592
def luas_lingkaran(r):
    return PI*r*r
print (luas_lingkaran(5))


# *Args & **Kwargs

# *Args:
def tambah(*bilangan):
    total = 0
    for n in bilangan:
        total += n
        return total
print(tambah(1, 2, 3, 4, 5, 6))

# **Kwargs:
def connect(**options):
    conn_params = {
        'host': options.get('host', '127.0.0.1'),
        'port': options.get('port', 5432),
        'user': options.get('user', ''),
        'pwd': options.get('pwd', ''),
        }
    print(conn_params)
connect()
connect(port = 5431, user='ftti', pwd='nimda')


# Nilai minimal

#def minimum(*n):
 #   if n:
  #      mn = n[0]
   #     for value in n[1:]:
    #        if value < mn:
     #           mn = value


# Matrix

def matrix_mul(a, b):
    return[[sum(i * j for i, j in zip(r, c))
            for c in zip(*b)]for r in a]

a = [[1, 2], [3, 4]]
b = [[5, 1], [2, 1]]
c = matrix_mul(a, b)
print(c)