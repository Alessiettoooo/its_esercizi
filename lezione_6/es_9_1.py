class Restaurant : 

    def __init__(self,nome,tipo):

        self.nome = nome 
        self.tipo = tipo

    def describe_restaurant(self) : 

        print(f" il nome del ristorante è {self.nome} e il tipo della cucina è {self.tipo}")

    def open_restaurant(self) : 

        print(f" il ristorante è aperto")

    
r1 = Restaurant("alessio pizzas","moderna")

r1.describe_restaurant()
r1.open_restaurant()