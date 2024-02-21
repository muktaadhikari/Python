 # a=float(input("enter the number:"))
# b=float(input("enter the number:"))
# print("you entered:",a,b)

# # calculator
# a=int(input("enter any number"))
# b=int(input("enter any number"))


# operator = input("Enter the operator (+, -, *, /): ")

# if operator=="-":
#     print(a-b)
# elif operator =="+":
#     print(a+b)
# elif operator =="*":
#     print(a*b)
# elif operator=="/":
#     print(a/b)
# else:
#     print("syntax error")
        
    # string slicing
# a=input('Name: ') 
# print(a[::-1]) 
     
    #  slice 
# person={
#     'Name':'Mukta',
#     'Age':'22',
#     'City':'Gaushala',
#     'Family_members':[
#         'father',
#         'mother',
#         'sister',
#         'brother',
#     ]
# }
# print(person['Family_members'][1][2])


# print(person['Family_members'][3][::])

# kwangs
# f_name=input("Enter your Name: ")
# age=int(input('Enter your Age: '))
# address=input('Enter your Address: ')
# def person(**details):
#     print(f'My name is {details['name']}. I am {details['age']} years old. I live in {details['address']}.')
# person(name=f_name, age=age, address=address)
# def sum(*nums):
#     total=0
#     for i in range(len(nums)):
#        for num in nums[i]:
#             total+=num
#     return total


# print(sum([1,2,3],[4,5,6]))





# range 
# start=int(input("Enter the start number: "))
# stop=int(input("Enter the stop number :"))
# step=int(input("Enter the step value  :"))
# def my_range(start, stop, step):
#     while  start < stop:
#         print(start)
#         if step!=0:
#             start+=step
#         else:
#             start +=1
# my_range(start, stop, step)



# calculator
# a = int(input("Enter first numbers: "))
# b = int(input("Enter second numbers: "))
# c = (input("Enter any one operator '+', '-' , '' , '/', '*', '%', '//': "))
# def sum(a,b):
#     print(f"The sum of {a} and {b} is {a + b}")
# def subtract(a,b):
#     print(f"The difference between {a} and {b} is {a - b}")
# def product(a,b):
#     print(f"The product of {a} and {b} is {a * b}")
# def divide(a,b):
#     print(f"{a} divided by {b} is {a / b}")
# def expo(a,b):
#     print(f"{a} raised to the power of {b} is {a ** b}")
# def mod(a,b):
#     print(f"The remainder when {a} is divided by {b} is {a % b}")
# def quotient(a,b):
#     print(f"The quotient when {a} is divided by {b} is {a // b}")
    
# if c=='+':
#     sum(a,b)
# elif c=='-':
#     subtract(a,b)
# elif c=='*':
#     product(a,b)
# elif c=='/':
#     if b==0:
#         print('Divider cannot be 0')
#     else:
#      divide(a,b)
# elif c=='**':
#     expo(a,b)
# elif c=='%':
#     mod(a,b)
# elif c=='//':
#     quotient(a,b)
# else:
#     print('Wrong operator chosen,choose the correct operator')




# # kwargs
# f_name=input("Enter your Name: ")
# age=int(input('Enter your Age: '))
# address=input('Enter your Address: ')
# def person(**details):
#     print(f'My name is {details['name']}. I am {details['age']} years old. I live in {details['address']}.')
# person(name=f_name, age=age, address=address)
    
    
# datatype_method

# fruits=[]
# for i in range(10):
    
#     fruit = input("Enter fruits")
#     fruits.append(fruit)

# print(fruits)




# database=[ 
#     {
#         'name':'ram',
#         'password':'<123456789>',
#         'email':'ram@gmail.com'
    
#     },
#     {  
#         'name':'hari',
#         'password':'<1234567>',
#         'email':'hari@gmail.com'
#     }
# ]
# print(database)
# for i in range(2):

#         name = input("Enter your name: ")
#         email = input("Enter your email: ")
#         password = input("Enter your password: ")
#         user ={
#             'name':name,
#             'email':email,
#             'password':password
#     }
    
# database.append(user)
# print(database)



isLogIn=False
database = [
    {'name':'Mukta Adhikari','email':'muktaadhikari708@gmail.com','passcode':'123','age':'22','address':'Baneshwor'},
    {'name':'Zoey Andrew ','email':'zoey123@gmail.com','passcode':'3214','age':'23','address':'Gaushala'},
    {'name':'Luna Mardara','email':'itsmeluna@gmail.com','passcode':'258','age':'20','address':'Chabahil'},
    {'name':'Ratna Shakya','email':'ratna@gmail.com','passcode':'984','age':'30','address':'Ratopul'},
    {'name':'Binita Bharati','email':'bini100@gmail.com','passcode':'999','age':'21','address':'Setopul'},
]
# print (database)
 
 

def register():
    f_name = input("Enter your first name: ")
    l_name = input("Enter your last name:")
    email = input("Enter your email: ")
    passcode = input("Enter your passcode: ")
    age = input("Enter  your age : ")
    address = input("Enter Your Address: ")
    
    users ={
        'name':f_name+""+l_name,
        'email':email,
        'passcode':passcode,
        'age':age,
        'address':address
        
    }
    

    database.append(users)
    print("your account has been created. now you can login. \n ")
def  userLogin():
     f_name = input("Enter your first name: ")
     l_name = input("Enter your last name: ")
     email = input("Enter your email: ")
     passcode = input("Enter your passcode: ")
     age = input("Enter  your age : ")
     address = input("Enter Your Address: ")
     for data in database:
        if data['name']==f_name+" "+l_name and data['email']==email and data['age']==age and data['passcode']==passcode and data['address']==address:
            global isLogIn
            isLogIn= True
def Listofusers():
    print(f"below  are the list of registered users:\n {database}")

answer=input("Don't have account?\n type'yes' if yes and 'no' if not:").lower()
if answer=='yes':
    print('please register first.')
    register()
    userLogin()
elif answer=='no' or answer=="":
    print("enter your crendicial:\n")
    userLogin()
if isLogIn == True:
    print(f"logged in sucessfully.")
    Listofusers()
else:
    print("enter right user")