def lowercase(func):
    def wrapper():
        func_ret = func()
        change_to_lowercase = func_ret.lower()
        return change_to_lowercase
    return wrapper

def split_sentence(func):
    def wrapper():
        func_ret = func()
        output = func_ret.split()
        return output
    return wrapper

@split_sentence
@lowercase
def hello_function():
    return 'HELLO WORLD'
print(hello_function())