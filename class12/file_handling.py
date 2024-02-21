
# happy = input("enter the file: ")

# f= open(happy,'w')
    
# user_input = input("Please enter the data you want to store in the file: ")
      
# f.write(user_input)
    
# print("Data has been successfully stored in",f)

# try:
#     f= open("happy.txt","x")
    
# except FileNotFoundError:
#     print("The file doesn't exist")
while True:
    try:
        happy = input("enter the file: ")
        f= input("enter r,w,a : ")
        file=open(happy,f"{f}") 
        if f=="r":
            print(file.readlines()[1])
            file.close()
        
        elif f=="w":
            write_data = input("\n Enter the data which you want to write into the file")
            file.write(write_data)
            file.close()
        elif f=="a":
            append_data = input("\n enter new data ")
            file.write("\n"+append_data)
            file.close()
            
        
    except FileNotFoundError as e:
        print(f"file not found" +(e))
    
  

    