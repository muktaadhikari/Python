# class food:
#     def __init__(self) -> None:
#         print('I want some pizza')
#     #     self.show()
        
#     # def show(self):
#     #         print("show")
            
            
# food()

class  Food:
    def __init__(self,name,topping):
        self.name=name
        self.topping=topping
        
    def __str__(self) -> str:
        return self.name
    # def __eq__(self,object):
    def __ne__(self,object):
    
        return self.name!=object.name
    
pizza=Food("Pizza","Pepperoni")
burger=Food("Pasta","Carbonara")
print(burger!=pizza)