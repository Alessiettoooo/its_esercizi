voto = int(input(f"inserisci il voto "))

match voto: 
    
    case voto if voto == 10 :
        print(f"eccellente")
        
    case voto if voto == 8 or voto == 9 :
        print(f"Molto buono")
        
    case voto if voto == 6 or voto == 7 : 
        print(f"voto sufficiente")
        
    case voto if voto == 5 or voto == 6 :
        print(f"voto insufficiente")
        
    case voto if voto <=3 and voto >= 1 :
        print(f"gravemente insufficiente")
        
    case _:
        print(f"voto non valido")
        