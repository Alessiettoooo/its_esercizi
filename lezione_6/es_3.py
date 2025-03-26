class animal : 

    def __init__(self,nome,habitat,legs):
        
        self.nome = nome 
        self.habitat = habitat
        self.legs = legs

    def name(self) : 

        print(f"il nome dell'animale è {self.nome}")

    
    def setLegs(self) : 

        self.legs += 1 

    def getLegs(self) : 

        return self.legs 
    
    def print(self) : 

        print(f" l'animale si chiama {self.nome} il suo habitat è {self.habitat} e le gambe che possiede sono {self.legs}")


cane = animal("edoardo","oceano",6)
tigre = animal("alessio","mare",6)

cane.name()
tigre.name()

cane.setLegs()
cane.getLegs()

cane.print()















