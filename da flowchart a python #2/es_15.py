n = int(input(f"inserisci valore n "))

if n % 1 == 0 : 

    if n > 0 and n <= 100 : 

        sum = 0 
        i = 1 

        while i < n : 

            if i % 2 == 0 : 

                sum += i 


            i += 1 

        print(f"la somma è {sum} ")

    elif n == 0 or n < 0 : 

        print(f"errore ")

    else : 

        sum = 0 
        i = 1 

        while i < n :

            if i % 2 != 0 : 

                sum += i 


            i += 1 

        print(f" la somma è {sum} ")

         
        