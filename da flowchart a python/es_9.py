nome = input(f"inserisci nome")
vendite = float(input(f"inserisci vendite"))

max = vendite
max_nome = nome 
min_nome= nome 
min = vendite 
cont = 0

for cont in range(1,20+1) :

    new_nome = input(f"insersci nuovo nome")
    new_vendite = float(input(f"inserisci nuova vendita"))

    if new_vendite > max : 

        max_nome = new_nome
        max = new_vendite

    elif new_vendite < min : 

        min_nome = new_nome
        min = new_vendite

    else : 

        cont = cont + 1


print(f" il nome è {max_nome} e il massimo delle vendite è {max} ")
print(f" il nome è {min_nome} e il minimo delle vendite è {min}")

