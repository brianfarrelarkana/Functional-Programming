import functools
def memoize(func):
    func.cache = dict()
    @functools.wraps(func)
    def _memoize(*args):
        if args not in func.cache:
            func.cache[args] = func(*args)
            return func.cache[args]
        return _memoize
    
#@memoize
def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
for i in range(1, 7):
    print('fibonacci %d: %d' % (i, fibonacci(i)))

import functools
def counter(func):
    func.calls = 0
    @functools.wraps(func)
    def _counter(*args, **kwargs):
        func.calls += 1
        return func(*args, **kwargs)
    return _counter

@functools.lru_cache(maxsize=3)
@counter
def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
print(fibonacci(100))