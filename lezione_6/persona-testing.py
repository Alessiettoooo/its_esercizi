"""
#dal file persona.py importa la classe Persona
from persona import Persona 

ar : Persona = Persona("alessio","riboldi neri",19)
print(ar.name,ar.lastname,ar.age)

ar.displayData()
"""

from persona2 import Persona 

ar : Persona = Persona()

ar.displayData()

print("---------------")

#imposto il nome della persona ar
ar.setName("alessio")
ar.displayData()

print("---------------")

ar.setLastname("riboldi neri")
ar.displayData()

print("---------------")

ar.setAge(18)
ar.displayData()

print(ar.getName())
print(ar.getLastname())
print(ar.getAge())