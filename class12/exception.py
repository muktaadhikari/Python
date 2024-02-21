# while True:
#     try:
#         a=int(input("number"))
#         b=int(input("next"))
        
#         if b==5:
#             raise Exception("5 is not valid")
        
#         print(a/b)
        
#     except ZeroDivisionError:
#         print("a cannot be divided")
        
        
#     except Exception as e:
#         print("smething went wrong",e)



while True:
    try:
    
        a=[1,2,3,4,5]
        b=int(input("Enter number"))
        
        if b==5:
            raise Exception("You can't enter 5")
        print(a[b])
    except Exception as e:
        print("something went wrong",e)
        
        
        
        
        