n = int(input(f"inserisci numero "))
        
if n % 1 == 0 and n > 0 : 

    sum = 0 
    i = 1 

    while i < n :

        sum = sum + i*i
        i = i + 1

    print(f"la somma è {sum}")
    

else : 

    print(f"errore il numero {n} inserito deve essere positivo")

