from calculator import *
while True:
    a=int(input("Enter the first number:"))
    b=int(input("Enter the second number:"))
    c=input("enter any operator' +, - , / , *, //, % : ")
    if c=='+':
        add(a,b)
    elif c=='-':
        subtract(a,b)
    elif c=='*':
        multiply(a,b)
    elif c=='/':
        if b!=0:
            division(a/float(b))
        else:
            print('Division by zero is not allowed.')
    elif c=="%":
        reminder(a,b)
    elif c=="//":
        quotient(a,b)
    else :
     print('Invalid Operator, please choose the correct one')
     

    