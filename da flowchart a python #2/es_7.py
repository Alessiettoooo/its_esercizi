cont = 0 
sum = 0 

while True :

    scelta = input(f"fai la tua scelta si o no ")


    match scelta : 

        case "si" : 

            voto = float(input(f"inserisci voto "))

            if voto > 0 :

                cont = cont + 1
                sum = sum + voto

            else : 

                print(f"errore")
        
        case "no" : 

            if cont > 0 : 

                media = sum / cont
                print(f"la media è : {media}")
                break

            else : 

                print(f"nessuno voto inserito")
                break