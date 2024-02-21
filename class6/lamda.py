# def sum(a,b)
# print(a+b)
# sum(1,2)
# sum=lambda a,b:a+b
# # print(sum(1,2))
# def func(n):
#  return lambda x:x*n
# doubler=func(2)
# print(doubler(10))

# tripler
sum=lambda a,b:a+b
def func(n):
    return lambda  x: n * x
tripler= func(3)
print(tripler(5))
