voto = int(input(f"inserisci il numero in centesimi"))

match voto : 

    case voto if voto <= 110 and voto >= 106 :
        print(f"il voto è  GPA 4.0")

    case voto if voto <= 105 and voto >= 101 : 
        print(f" il voto è GPA 3.7")

    case voto if voto <= 100 and voto >= 96 : 
        print(f" il voto è GPA 3.3")

    case voto if voto <= 95 and voto >= 91 : 
        print(f" il voto è GPA 3.0")

    case voto if voto <= 90 and voto >= 86 : 
        print(f" il voto è GPA 2.7")

    case voto if voto <= 85 and voto >= 81 : 
        print(f" il voto è GPA 2.3")

    case voto if voto <= 80 and voto >= 76 : 
        print(f" il voto è GPA 2.0")

    case voto if voto <= 75 and voto >= 70 : 
        print(f" il voto è GPA 1.7")

    case voto if voto <= 69 and voto >= 66 : 
        print(f" il voto è GPA 1.0")

    case _: 
        print(f" Voto non valido")