punteggio = 0 

while punteggio < 100 : 

    d1 = int(input(f"inserisci d1 "))
    d2 = int(input(f"Inserisci d2 "))

    if d1 > 0 and d1 <= 6 and d2 > 0 and d2 <= 6 : 
        
        sum = d1 + d2 

        if d1 % 2 == 0 and d2 % 2 == 0 and sum > 8 : 

            punteggio = 100 

        elif d1 == 6 or d2 == 6 or sum == 7 : 

            punteggio += 10 

        else : 

            punteggio = 0 
            print(f"sconfitta")

print(f"vittoria")