sum = 0 
cont = 1

while True : 

    n = float(input(f"inserisci il numero "))
    sum = sum + n
    cont += 1

    if cont == 6 :

        print(f"la somma dei numeri è {sum}")
        break
