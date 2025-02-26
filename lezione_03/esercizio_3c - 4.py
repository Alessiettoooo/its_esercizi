print(f"inserisci il nome dell'animale")

animale = str(input())

match animale : 

    case animale if animale == "cane" or animale == "gatto" or animale == "cavallo" or animale == "elefante" or animale == "leone" : 
        print(f"{animale} fa parte della categoria Mammiferi")
    
    case animale if animale == "serpente" or animale == "lucertola" or animale == "tartaruga" or animale == "coccodrillo"  : 
        print(f"{animale} fa parte della categoria Rettili")

    case animale if animale == "aquila" or animale == "pappagallo" or animale == "gufo" or animale == "falco" : 
        print(f"{animale} fa parte della categoria Uccelli")

    case animale if animale == "squalo" or animale == "trota" or animale == "salmone" or animale == "capra" : 
        print(f"{animale} fa parte della categoria pesci")
    
    case _:
        print(f"il programma non è in grado di classificare l'animale inseritocane")


