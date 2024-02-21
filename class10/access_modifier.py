class person:
    def __init__(self,name,age,password):
        self.name=name
        self.age=age
        self.__password=password
        
@property
def password(self):
        return self.__password
        
@password.setter
def password(self,password):
        self.__password=password
person=person('name',12,'password')
print(person.password)
