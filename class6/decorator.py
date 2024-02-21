def star(func):
    def wrapper():
        print('*'*20)
        func()
        print('*'*20)
    return wrapper
# @star
def hello():
    print('hello')
    
    # @star
star(hello)()
    