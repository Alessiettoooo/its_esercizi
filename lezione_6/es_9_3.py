class User : 

    def __init__(self,first_name,last_name,age):

        self.first_name = first_name
        self.last_name = last_name
        self.age = age 

    def describe_user(self) : 

        print(f" il nome è {self.first_name}, il cognome è {self.last_name} e l'età è {self.age}")

    def greet_user(self) : 

        print(f" ciao sei pronto per incontrare {self.first_name} {self.last_name}")

u = User("Alessio","Riboldi Neri",19)
u1 = User("Diego","lanzi",20)

u.describe_user()
u.greet_user()