#lambda
kuadrat = lambda x: x*x
print(kuadrat(3))

kali = lambda x, y: x*y
print(kali(4, 3), "\n")


#fungsi
def f(x, y, z):
    return x + y + z
print(f(2, 30, 400))

#lambda
f = lambda x, y, z: x + y + z
print(f(2, 30, 400), "\n")


#lambda
L = [lambda x: x ** 2,
     lambda x: x ** 3,
     lambda x: x ** 4]
for f in L:
    print(f(3))
print(L[0](11))