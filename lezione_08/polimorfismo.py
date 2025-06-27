from persona import Persona 
from alieno import Alieno 
#creare un oggetto p della classe persona 
p : Persona = Persona("federico","march",29)

#visualizzare le informazioni dell'oggetto 
print(p)

#creare un oggetto et della classe alieno  
et : Alieno = Alieno("Andromeda")

#visualizzare le informazioni dell'oggetto et 
print(et)


#fare in modo che un oggetto p invochi il metodo speak 

p.speak() 

et.speak()