from functools import partial
def func_multiply(x, y):
    return x*y

print (func_multiply(3,4))
partial_multiply = partial(func_multiply, 4)
print (partial_multiply(4))

print (partial_multiply(3))