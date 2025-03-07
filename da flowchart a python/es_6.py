n = int(input(f"inserisci numero "))

if n > 0 : 

    fattoriale = 1
    i = 1

    for i in range(1,n+1) : 

        fattoriale = fattoriale * i 
        i = i + 1


    print(f"il numero fattoriale è {fattoriale}")

else : 

    print(f"il numero inserito deve essere positivo")

   
