import math

def calculateCharges(ore):

    costo = 2
    supplemento = 0 
    ore_agg = 0

    ore = float(input(f"inserisci le ore di permanenza nel parcheggio "))

    if ore <= 3 : 

        print(f"il costo per {ore} ore è di {costo}")

    elif ore == 24 : 

        costo = 10
        print(f"il costo per {ore} ore è di {costo}")

    else : 

        ore_agg = ore - 3
        supplemento = ore_agg * 0.50
        costo = costo + supplemento
        costo = round(costo,0)

        print(f"il costo per {ore} ore è di {costo} ")

calculateCharges("Car"  "Hours"  "Charge")
calculateCharges("1",)