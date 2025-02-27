mammifero = ["cane","gatto","cavallo","elefante","leone","balena","delfino"]
rettili =["serpente","lucertola","tartaruga","coccodrillo"]
uccelli =["aquila","pappagallo","gufo","falco","cigno","anatra","gallina","tacchino"]
pesci =["squalo","trota","salmone","carpa"]

animale = str(input(f"inserisci il nome del animale  "))
habitat = str(input(f"inserisci l'habitat dell'animale tra aria/acqua/terra  ") )

match animale :

    case animale if animale in mammifero : 
        print(f"l'animale fa parte dei mammiferi")
        animal_type = "mammiferi"

    case animale if animale in rettili : 
        print(f"l'animale fa parte dei rettili")
        animal_type = "rettili"

    case animale if animale in uccelli : 
        print(f"l'animale fa parte degli uccelli")
        animal_type = "uccelli"

    case animale if animale in pesci : 
        print(f"l'animale fa parte dei pesci")
        animal_type = "pesci"

    case _:
        print(f"non so dire di che categoria sia l'animale {animale}")
        animal_type = "unknown"

acqua =["balena","delfino","tartaruga","coccodrillo","cigno","anatra","squalo","trota","salmone","carpa"]
aria =["aquila","pappagallo","gufo","falco"]
terra =["cane","gatto","cavallo","elefante","leone","serpente","lucertola","tartaruga","coccodrillo","gallina","tacchino"]


diz = {"nome":animale,"categoria":animal_type,"habitat":habitat}

match habitat:
    case "acqua":
        match animale:
            case animale if animale in acqua:
                print(f"l'animale {animale} è un {animal_type} e può vivere in acqua")
            case _:
                print(f"l'animale {animale} non può vivere in acqua")
    case "aria":
        match animale:
            case animale if animale in aria:
                print(f"l'animale {animale} è un {animal_type} e può vivere in aria")
            case _:
                print(f"l'animale {animale} non può vivere in aria")
    case "terra":
        match animale:
            case animale if animale in terra:
                print(f"l'animale {animale} è un {animal_type} e può vivere sulla terra")
            case _:
                print(f"l'animale {animale} non può vivere sulla terra")
    case _:
        print(f"Non sono sicuro di quale habitat {habitat} sia.")

    
    