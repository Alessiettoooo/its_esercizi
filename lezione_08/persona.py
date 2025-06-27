class Persona :
    
    def __init__(self,name,lastname,age):

        self.name= name 
        self.lastname = lastname 
        self.age = age

    def setName(self,name) -> None : 

        self.name = name 

    def setLastname(self,lastname) -> None : 

        self.lastname = lastname 

    def setAge(self,age) -> None : 

        if age < 0 or age > 130 : 

            self.age = 0 

        else : 

            self.age = age 

    def getName(self) -> str :

        return self.name 
    
    def getLastname(self) -> str :

        return self.lastname 
    
    def getAge(self) -> int :

        return self.age

