class Restaurant : 

    def __init__(self,nome,tipo,number_served = 0 ):

        self.nome = nome 
        self.tipo = tipo
        self.number_served = number_served

    def set_number_served(self) : 
        
        self.number_served = 5

    def describe_restaurant(self) : 

        print(f" il nome del ristorante è {self.nome} e il tipo della cucina è {self.tipo} numeri serviti sono {self.number_served}")

    def open_restaurant(self) : 

        print(f" il ristorante è aperto")

    

    
r1 = Restaurant("alessio pizzas","moderna")

r1.describe_restaurant()
r1.open_restaurant()
r1.set_number_served()