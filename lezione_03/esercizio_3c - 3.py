lista =[]

while len(lista) <= 2 :

    nome = str(input("inserisci penna , matita, quaderno o pane , latte, uova o sedia , tavolo , armadio o telefono , computer , tablet"))
    
    lista.append(nome )

match lista : 
    
    case lista if lista == ["penna","matita","quaderno"] : 
        print(f"materiale scolastico")
    
    case lista if lista == ["pane","latte","uova"] :
        print(f"Prodotti alimentari")

    case lista if lista == ["sedia","tavolo","armadio"] :
        print(f"Mobili")

    case lista if lista == ["telefono","computer","tablet"] : 
        print(f"Dispositivi elettronici")

    case _:
        print(f"categoria sconosciuta")