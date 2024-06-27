def lowercase(func):
    def wrapper():
        func_ret = func()
        change_to_lowercase = func_ret.lower()
        return change_to_lowercase
    return wrapper

def hello_function():
    return 'HELLO WORLD'
decorate = lowercase(hello_function)
print(decorate())

#decorator
@lowercase
def hello_function():
    return 'HELLO WORLD'
print(hello_function())