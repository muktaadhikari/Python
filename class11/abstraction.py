# from abc import ABC, abstractmethod

# class Computer(ABC):
    
#     def run(self,app):
#         self.process(app)
#     @abstractmethod
#     def process(self,app):
#         pass
    
# class laptop(Computer):
#     def process(self,app):
#         print("laptop is running on "+ app)
        
# class mobile(Computer):
#     def process(self,app):
#         print("mobile is running on "+ app)

# acer=laptop()
# acer.run('pubg')

# sumsung=mobile()
# sumsung.run('chrome')

from abc import ABC, abstractmethod
class Cars(ABC):
    
    def colour(self,speed):
        self.process(speed)
    @abstractmethod
    def process(self,speed):
        pass
class Tesla(Cars):
    def process(self,speed):
        print("Tesla is running on "+ speed)
class Lamborgini(Cars):
    def process(self,speed):
        print("Lamborgini is running on "+ speed)
        
Data=Lamborgini()
Data.colour('30000km')


Store=Tesla()
Store.colour('50000km')




        


    