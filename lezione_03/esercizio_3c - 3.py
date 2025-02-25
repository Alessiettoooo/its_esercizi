lista =[]

while len(lista) <= 2 :

    nome = str(input("inserisci penna , matita, quaderno o pane , latte, uova o sedia , tavolo , armadio o telefono , computer , tablet"))
    
    lista.append(nome )

match lista : 
    
    case lista if lista == ["penna","matita","quaderno"] : 
        print(f"materiale scolastico")
    
    case _:
        print(f"categoria sconosciuta")