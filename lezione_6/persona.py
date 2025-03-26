class Persona :

    def __init__(self,name,lastname,age):

        self.name= name 
        self.lastname = lastname 
        self.age = age 

    def displayData(self) -> None: 

        print(f"nome: {self.name} \ncognome: {self.lastname} \netà: {self.age} ")

