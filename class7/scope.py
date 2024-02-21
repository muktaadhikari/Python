a=10
# def hello():
#     a=11
#     print(a)
    


# hello()
# print(a)


def outer():
    a=12
    def inner():
       print('inner sees a as',a)  
    print('outer sees a as',a) 
    inner() 
print ("globally as a")
print(a)