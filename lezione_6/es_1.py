class person : 

    def __init__(self,name,age) : 

        self.name = name 
        self.age = age 


alice = person("Alice",45) 
bob = person("bob",36)

if bob.age > alice.age :

    print(bob.age)

else : 

    print(alice.age)


james = person("james",55)
alessio = person("alessio",19)
francesco = person("francesco",17)

lista = [james,alessio,francesco,alice,bob] 
giovani = lista [0] 
for i in lista : 

    if i.age < giovani.age :

        giovani = i 

print(f" il piu giovane è {giovani.name}")

    

    

