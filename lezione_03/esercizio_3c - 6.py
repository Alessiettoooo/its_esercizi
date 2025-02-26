mammifero = ["cane","gatto","cavallo","elefante","leone","balena","delfino"]
rettili =["serpente","lucertola","tartaruga","coccodrillo"]
uccelli =["aquila","pappagallo","gufo","falco","cigno","anatra","gallina","tacchino"]
pesci =["squalo","trota","salmone","carpa"]

animale = str(input(f"inserisci il nome del animale"))
habitat = str(input(f"inserisci l'habitat dell'animale tra aria/acqua/terra"))

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

match diz : 
    
    case diz if diz["nome"] in mammifero and animale in terra :
        print(f" l'animale {animale} è un {animal_type} e vive in {habitat}")
    
    case diz if diz["nome"] in mammifero and animale in acqua :
        print(f"l'animale {animale} è un {animal_type} e può vivere in {habitat}")

    case diz if diz["nome"] in rettili and animale in terra :
        print(f"l'animale {animale} è un {animal_type} e può vivere in {habitat}")

    case diz if diz["nome"] in rettili and animale in acqua :
        print(f"l'animale {animale} è un {animal_type} e può vivere in {habitat}")

    case diz if diz["nome"] in uccelli and animale in aria :
        print(f"l'animale {animale} è un {animal_type} e può vivere in {habitat}")
    
    case diz if diz["nome"] in uccelli and animale in terra :
        print(f"l'animale {animale} è un {animal_type} e può vivere in {habitat}")
    
    case diz if diz["nome"] in pesci and animale in acqua :
        print(f"l'animale {animale} è un {animal_type} e può vivere in {habitat}")
    
    case _:
        print(f"non so dire in quale categoria classificare l'animale {animale}")
        print(f"non sono in grado di fornire informazioni sull'habitat {habitat}")