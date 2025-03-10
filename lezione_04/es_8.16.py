''' #1 
import import_function

car = import_function.make_car("lamborghini","sesto elemento",colore = "nera", finestrini = "oscurati")
print(car)

'''


'''#2 
from import_function import make_car

car = make_car("lamborghini","sesto elemento",colore = "nera", finestrini = "oscurati")
print(car)  
'''


'''#3       

from import_function import make_car as ciao

car = ciao("lamborghini","sesto elemento",colore = "nera", finestrini = "oscurati")
print(car)
'''

'''#4

import import_function as ciao 

car = ciao.make_car("lamborghini","sesto elemento",colore = "nera", finestrini = "oscurati")
print(car)
'''

'''#5

from import_function import*

car = make_car("lamborghini","sesto elemento",colore = "nera", finestrini = "oscurati")
print(car)
'''
