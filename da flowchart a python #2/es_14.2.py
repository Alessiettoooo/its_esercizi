punteggio = 0 
while True : 

    d1 = int(input(f"inserisci d1 "))
    d2 = int(input(f"inserisci d2 "))

    if d1 > 0 and d1 <= 6 and d2 > 0 and d2 <= 6 : 

        sum = d1 + d2 

        if d1 % 2 == 0 and d2 % 2 == 0 and sum > 8 : 

            punteggio = 100 

        elif d1 == 6 or d2 == 6 or sum == 7 : 

            punteggio += 10
            continue 

        else : 

            punteggio = 0 


        if punteggio >= 100 : 

            print(f"vittoria")
            break

        elif punteggio == 0  : 

            print(f"sconfitta")

        else : 

            print(f"il punteggio è {punteggio}")

        
