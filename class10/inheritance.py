class grandfather:
    house='big'
    def __init__(self):
        print("caste is important") 
    
class father(grandfather):
    
    car='lambo'
    
    
class mother:
    jwellery='diamond'
    
    

class son(father,mother):
    console='Ps25'

    def __init__(self):
        super().__init__()
        print(self.console)
    


son=son()
# print("The son has a",son.console,"and drives a",son.car)
# print(son.jwellery)
