giorno = int(input(f"inserisci il numero del giorno " ))
mese = int(input(f"inserisci il numero del mese " ))

data = (giorno,mese)

match data :

    case data if giorno == 1 and mese == 1 : 
        print(f"il {data} è Capodanno !")

    case data if giorno == 14 and mese == 2 : 
        print(f"il {data} è San Valentino !")

    case data if giorno == 2 and mese == 6 : 
        print(f"il {data} è la Festa della Republica Italiana !")

    case data if giorno == 15 and mese == 8 : 
        print(f"il {data} è Ferragosto !")

    case data if giorno == 31 and mese == 10 : 
        print(f"il {data} è Halloween !")

    case data if giorno == 25 and mese == 12 : 
        print(f"il {data} è Natale !")

    case _:
        print(f"nel giorno {data} non c'è nessuna festa importante")

    
