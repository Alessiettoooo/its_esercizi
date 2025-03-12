while True : 
    n = float(input(f"Inserisci N "))

    if n > 0 : 

        if n % 1 == 0 : 

            cont = 0 
            i = 0 

            while i != 10: 

                x = int(input(f"inserisci x "))

                if x % n == 0 : 

                    cont = cont + 1 

                else : 

                    i = i + 1

            print(f"cont è {cont}")
            break

        else : 

            print(f" n deve essere intero positivo")

    print(f"n deve essere positivo")

